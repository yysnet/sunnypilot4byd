from cereal import car
from openpilot.selfdrive.car.byd.values import CAR

Ecu = car.CarParams.Ecu

FW_VERSIONS = {
  CAR.HAN_DM_20_21: {
    (Ecu.engine, 0x7b0, None): [
      b'F152607060\x00\x00\x00\x00\x00\x00',
    ],
  },
  
  CAR.HAN_EV_20_21: {
    (Ecu.engine, 0x7b0, None): [
      b'F152607060\x00\x00\x00\x00\x00\x00',
    ],
  },
}
