import os

# use absolute path to this entry file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Optional local directory.
DATA_DIR = os.path.join(BASE_DIR, 'data')


def run(
    json_data={}, 
    query_params={}, 
    path='/', 
    form_data={},
    file=None, 
    metadata={},
    method='POST',
    headers={},
    *args, 
    **kwargs):
    response = {
        "json_data": json_data,
        "query_params": query_params,
        "path": path,
        "method": method,
        "form_data": form_data,
        "metadata": metadata,
        "headers": headers
    }
    '''
    This function is called on any given request to your hosted tight.ai project version (app). 

    Parameters:
        json_data (dict): JSON data pushed to this endpoint. 
        query_params (dict): Query paramters pushed to this endpoint
        path (str): request path called such as "/", "/predict", "/status/lookup"
        method (str): HTTP method used calling this endpoint
        form_data (dict): Any non-file submitted as form data
        file (File): file (image, csv, pdf, etc) uploaded to this endpoint.
        metadata (dict): related metadata for this endpoint
        headers (dict): HTTP headers passed when calling this endpoint.

    Returns:
        response (dict): Return a json-ready Python dictionary with data. 
        response['status'] (int): Use this to change HTTP Status Code response.
    '''
    if file != None:
        response['has_file'] = True
    if len(json_data) == 0 and len(form_data) == 0 and len(query_params) == 0: 
        response['message'] = 'No data submitted.'
        response['status'] = 400 
    return response
