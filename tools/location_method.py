def create_EWS_location_info_json(query_result):
    if query_result:
        resp = {
            "code": 200,
            "SN": query_result.SN,
            "Model": query_result.modelName,
            "MAC": query_result.MAC,
            "area": query_result.area,
            "line": query_result.line,
            "row": query_result.row,
            "number": query_result.number,
            "created_time": query_result.created_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
    else:
        resp = {
            "code": 1004,
            "note": "Query is not exists"
        }
    return resp
