import numpy as np


def data_preprocessing(data, longitude, latitude):
    pi = 3.1416
    phi = latitude * pi / 180
    psi = longitude * pi / 180
    gamma_bt = 0.74
    rho = 0.2
    noct = 48

    hour_angle = []
    for i in data["timeofday"].index:
        time_zone = -5
        hour_angle.append(
            (
                (data["timeofday"][i] + data["minute"][i] / 60 - 12) * 15
                + (longitude - time_zone * 15)
            )
            * pi
            / 180
        )
    data["hour_angle_omega"] = hour_angle
    data["declination_angle_delta"] = (
        2 * pi * 23.45 / 360 * np.sin(2 * pi * (284 + data["dayofyear"]) / 365)
    )
    data["elevation_alpha"] = (90 - data["zenith"]) * pi / 180
    azimuth = []
    for i in range(len(data)):
        ans = (
            np.sin(data["declination_angle_delta"][i]) * np.cos(latitude * pi / 180)
            - np.cos(data["declination_angle_delta"][i])
            * np.sin(latitude * pi / 180)
            * np.cos(data["hour_angle_omega"][i])
        ) / np.cos(data["elevation_alpha"][i])
        if ans < -1:
            ans = -1
        ans = np.arccos(ans)
        if data["hour_angle_omega"][i] > 0:
            azimuth.append(pi * 2 - ans)
        else:
            azimuth.append(ans)
    data["azimuth"] = azimuth
    data["DirHI"] = data["DNI"] * gamma_bt * np.sin(data["elevation_alpha"])
    return data
