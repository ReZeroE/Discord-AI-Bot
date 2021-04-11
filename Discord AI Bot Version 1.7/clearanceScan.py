# clearance level one
admin = []
admin.append(0)

# clearance level two
mods = []
mods.append(273474320544694274)
mods.append(624227532685967380)
mods.append(405049915719286794)
mods.append(331908049822547978)
mods.append(640921854478909465)
mods.append(395791302026985482)
mods.append(342116502440247297)

# no clearance
public_user = []
class clearanceScan:
    def clearanceScan(self, userID):
        for i in admin:
            if i == userID:
                return 'C1'
        
        for j in mods:
            if j == userID:
                return 'C2'

        return 'None'

