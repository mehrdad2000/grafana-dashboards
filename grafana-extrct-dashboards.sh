#!/bin/bash
#this bashscript extract dashboards of grafana from grafana.db and store in this path /tmp/dashboards

# Directory where grafana.db is located

DB_DIR="/var/lib/grafana"
DB_FILE="$DB_DIR/grafana.db"

# Directory to save JSON files
OUTPUT_DIR="/tmp/dashboards"
mkdir -p $OUTPUT_DIR

# Function to export a dashboard by ID and name
export_dashboard() {
    local dashboard_id=$1
    local dashboard_name=$2
    local output_file="$OUTPUT_DIR/${dashboard_name}.json"

    # Extract the dashboard JSON and clean it up
    sqlite3 $DB_FILE <<EOF | sed -n '/{"annotations"/,/"weekStart":""}/p' | sed 's/.*{"annotations"/{"annotations"/' | sed 's/"weekStart":""}.*/"weekStart":""}/' > $output_file
.mode json
SELECT * FROM dashboard WHERE id=$dashboard_id;
EOF
}

# Get all dashboard IDs and names
dashboard_info=$(sqlite3 $DB_FILE "SELECT id, title FROM dashboard;")

# Export each dashboard
while IFS='|' read -r id name; do
    # Replace spaces with underscores in the dashboard name
    name=$(echo $name | tr ' ' '_')
    echo "Exporting dashboard ID $id with name $name..."
    export_dashboard $id $name
done <<< "$dashboard_info"

echo "Export completed. JSON files are saved in $OUTPUT_DIR."
