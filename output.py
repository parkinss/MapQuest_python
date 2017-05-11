class STEPS:
    def output(self, result: dict) -> str:
        to_return = "DIRECTIONS\n"
        for i in result['Steps']:
            to_return += i + '\n'
        return to_return

class TOTALDISTANCE:
    def output(self, result: dict) -> str:
        to_return = "TOTAL DISTANCE: "
        to_return += str(result['TotalDistance'])
        return to_return + "\n"

class TOTALTIME:
    def output(self, result: dict) -> str:
        to_return = "TOTAL TIME: "
        to_return += str(int(result['TotalTime']/60))
        return to_return + "\n"

class LATLONG:
    def output(self, result: dict) -> str:
        to_return = "LATLONGS\n"
        for i in result['LatLong']:
            line = ""
            if i[0] < 0:
                line += "%.2f" % -i[0] + "S "
            else:
                line += "%.2f" % i[0] + "N "
            if i[1] < 0:
                line += "%.2f" % -i[1] + "W\n"
            else:
                line += "%.2f" % i[1] + "E\n"
            to_return += line
        return to_return
                       
class ELEVATION:
    def output(self, result: dict) -> str:
        to_return = "ELEVATIONS\n"
        for i in result['Elevation']:
            to_return+= str(i) + '\n'

        return to_return
