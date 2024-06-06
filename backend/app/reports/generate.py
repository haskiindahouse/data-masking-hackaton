from flask import request, jsonify
from app.reports import bp

@bp.route('/generate', methods=['GET'])
def generate_report():
    report_type = request.args.get('reportType')
    date_range = request.args.get('dateRange')

    # Implement your report generation logic here
    report_data = {
        "reportType": report_type,
        "dateRange": date_range
    }

    return jsonify(report_data), 200