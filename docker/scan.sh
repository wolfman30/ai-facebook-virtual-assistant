#!/bin/bash
# Set the image name
IMAGE_NAME="facebook-group-engagement"

# Scan the Docker image and save the report
trivy image $IMAGE_NAME > trivy_scan_report.txt

# Output summary
echo "Trivy scan completed. Report saved to trivy_scan_report.txt."
