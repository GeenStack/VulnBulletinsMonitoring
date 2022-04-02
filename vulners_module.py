import vulners


vulners_api = vulners.VulnersApi(api_key="")


def get_bulletins(cve):
    result = {"metadata":{"bulletinFamily":{}}, "bulletins":{}}
    vulners_response = vulners_api.get_bulletin_references(cve)
    for i in vulners_response:
        for bulletin in vulners_response[i]:
            if bulletin["bulletinFamily"] not in result["metadata"]["bulletinFamily"]:
                result["metadata"]["bulletinFamily"].update({bulletin["bulletinFamily"]:1})
                result["bulletins"].update({bulletin["bulletinFamily"]:[]})
                result["bulletins"][bulletin["bulletinFamily"]].append(
                    {
                        "id": bulletin["id"],
                        "title": bulletin["title"],
                        "type": bulletin["type"],
                        "href": bulletin["href"]
                    }
                )
            else:
                result["metadata"]["bulletinFamily"][bulletin["bulletinFamily"]] += 1

                result["bulletins"][bulletin["bulletinFamily"]].append(
                    {
                     "id":bulletin["id"],
                     "title":bulletin["title"],
                     "type":bulletin["type"],
                     "href":bulletin["href"]
                 }
              )

    return result