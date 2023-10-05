import re

pattern = re.compile(
    r'(?P<firstGroup>[a-zA-Z0-9]*)\t(?P<secondGroup>\d*)\t(?P<thirdGroup>\d*)\t(?P<fourthGroup>\*\d*)\t(?P<fifthGroup>\*\*)\t(?P<sixthGroup>[A-Z]*)')

portInfo = "tcp6	32	3	*443	**	LISTEN"
if pattern.match(portInfo).group('sixthGroup') == "LISTEN":
    print("A porta 443 está à escuta")
else:
    print("A porta 443 não está à escuta")
