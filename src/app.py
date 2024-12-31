from flask import Flask, request, jsonify, render_template, redirect, url_for
from src.main.services.facebook_group_service import FacebookGroupEngagementService
from src.main.repositories.facebook_group_repository import FacebookGroupRepository
from src.main.models.interaction import Interaction

# Initialize Flask app
app = Flask(__name__)

# Initialize service and repository
repository = FacebookGroupRepository()
engagement_service = FacebookGroupEngagementService(repository)

# Routes
@app.route('/')
def dashboard():
    """Dashboard displaying summary and logged interactions."""
    summary = engagement_service.analyze_interactions()
    interactions = engagement_service.get_logged_interactions()
    return render_template('dashboard.html', summary=summary, interactions=interactions)

@app.route('/log_interaction', methods=['GET', 'POST'])
def log_interaction():
    """Log a new interaction."""
    if request.method == 'POST':
        interaction_type = request.form['type']
        group_name = request.form['group']
        content = request.form['content']
        timestamp = request.form['timestamp']
        metadata = {"likes": int(request.form.get('likes', 0)), "comments": int(request.form.get('comments', 0))}
        interaction = Interaction(interaction_type, group_name, content, timestamp, metadata)
        engagement_service.register_interaction(interaction)
        return redirect(url_for('dashboard'))
    return render_template('log_interaction.html')

@app.route('/export')
def export_interactions():
    """Export logged interactions to a CSV file."""
    engagement_service.export_interactions_to_csv("interactions.csv")
    return jsonify({"message": "Export successful", "file": "interactions.csv"})

@app.route('/generate_report')
def generate_report():
    """Generate a summary report."""
    report = engagement_service.generate_weekly_report()
    return jsonify({"report": report})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
