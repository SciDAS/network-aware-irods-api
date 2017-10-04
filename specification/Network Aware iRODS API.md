## Network Aware iRODS API

getLogicalLocation

```
@description 
- get complete iRODS logical path from filename
@param
- filename - unique iRODS logical filename, required
- match_exact - match filename exactly, optional, default = false
- include_trash - include trash in search path, optional, default = false
@response {JSON array}  
- irods_file - complete iRODS logical path

getLogicalLocation(filename, match_exact, include_trash): 

{
  "irods_filenames": [
    "string"
  ]
}
```

getReplicas

```
@description
- get replica information from iRODS filename
@param {string} 
- filename - unique iRODS logical filename
@response {json string} 
- resource_name - iRODS resources
- number - replication number
- path - path on physical disk
- status - replication status

getReplicas(filename): 

{
  "replicas": [
    {
      "resource_name": "string",
      "number": 0,
      "path": "string",
      "status": 0
    }
  ]
}
```

getHostNode

```
@description
- get host node from iRODS resource name
@param {string} 
- resource_name - unique iRODS resource node
@ret {json string} 
- hostnode - returns resource host node

getHostNode(resource_name):

{
  "hostnode": "string"
}
```

getHostSite

```
@description
- get host site from iRODS resource name
@param {string} 
- resnode - unique iRODS resource node
@response {json string} 
- site - returns name of site

getHostSite(resource_node):

{
  "site": {
    "perfsonar_node": "string",
    "sitename": "string"
  }
}
```

getHostSite

```
/**
* get site node
* @param {string} resnode - unique iRODS resource node
* @ret {json string} site- returns name of site
*/
getHostSite(resnode): site
"site”: {perfSONARnode: “string", sitename: “string”}
```