try:
    import mh_z19
    def get_co2_level():
        try:
            return mh_z19.read_all()['co2']
        except:
            return -1
except:
    def get_co2_level():
        return -1
