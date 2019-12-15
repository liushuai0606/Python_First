import platform


def get_ifname(ifname):
    if platform.system() == "Linux":
        return ifname
    elif platform.system() == "Windows":
        from WIN_IFNAME import win_from_name_get_id
        return win_from_name_get_id(ifname)
    else:
        return None


if __name__ == "__main__":
    print(get_ifname("ens37"))