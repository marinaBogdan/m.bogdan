property_transfer_xml = """
<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';
//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento'; 
//urn:multiCall/sessionId['?']</con:targetPath>
"""




#Find the sourcePath
startSourcePath = '<con:sourcePath>'
endSourcePath = '</con:sourcePath>'
sourcePath = (property_transfer_xml.split(startSourcePath))[1].split(endSourcePath)[0]

#Find the targetPath
startTargetPath = '<con:targetPath>'
endTargetPath = '</con:targetPath>'
targetPath = (property_transfer_xml.split(startTargetPath))[1].split(endTargetPath)[0]

print('The sourcePath is: ' + sourcePath)
print('And the targetPath is: ' + targetPath)
