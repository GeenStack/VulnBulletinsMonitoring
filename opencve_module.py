from config import OPENCVE_HEADER
import requests

def get_opencve_data(cve):
    url = "https://www.opencve.io/api/cve/{}".format(cve)
    headers = {"Authorization":OPENCVE_HEADER}
    r = requests.get(url, headers=headers)
    data = r.json()

    summary = data["summary"]
    cwe = data["cwes"]
    cvss2 = data['raw_nvd_data']['impact']['baseMetricV2']
    cvss3 = data['raw_nvd_data']['impact']['baseMetricV3']
    nvd_tags = []
    for ref in data['raw_nvd_data']['cve']['references']['reference_data']:
        pass


    '''
        data['raw_nvd_data']['impact']
    '''




    return r.json()