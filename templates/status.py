def get_page(d: dict):
    html_code = """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Task Details</title>
            <link rel="icon" href="/images/icon.ico" type="image/x-icon">
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
            
                th, td {
                    
                    padding: 8px;
                    font-weight: normal;
                }
                .horizontal-line {
                    border-top: 1px solid #000;
                }
            </style>
        </head>
        <body>
        <div style="border: 1px solid #000; padding: 10px; margin-bottom: 10px; width: 30%; margin: 0 auto;">
            <table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <th style="float: left;">Task ID</th>
                    <th style="float: center;">Details</th>
                    <th style="float: right;">Status</th>
                    
                </tr>
                
    """

    for id, item in d.items():
        html_code += f"""
                <tr class="horizontal-line">
                    <td style="float: left; text-align: center;">{id}</td>
                    <td style="float: center; text-align: center;">{" ".join(map(str, item["details"]))}</td>
                    <td style="float: right; text-align: center;">{item["status"]}</td>
                </tr>
        """



    html_code += """
            </table>
        </div>
        </body>
        </html>
    """
    return html_code