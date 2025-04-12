from artiq.coredevice.core import Core
from artiq.coredevice.urukul import CPLD
from artiq.experiment import *
from artiq.test.hardware_testbench import ExperimentCase

# Set to desired devices
# CPLD = "urukul1_cpld"


@nac3
class UrukulExp(EnvExperiment):
    core: KernelInvariant[Core]
    urukul1_cpld: KernelInvariant[CPLD]

    def build(self, runner):
        self.setattr_device("core")
        self.setattr_device("urukul1_cpld")
        # self.cpld = self.get_device("urukul0_cpld")
        self.runner = runner

    def run(self):
        getattr(self, self.runner)()

    # @rpc
    # def report_int32(self, name: str, data: int32):
    #     self.set_dataset(name, data)

    # @rpc
    # def report_float(self, name: str, data: float):
    #     self.set_dataset(name, data)

    @kernel
    def instantiate(self):
        pass

    # @kernel
    # def init(self):
    #     self.core.break_realtime()
    #     self.cpld.init()

    # @kernel
    # def cfg_write(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     self.cpld.cfg_write(self.cpld.cfg_reg)

    # @kernel
    # def sta_read(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     sta = self.cpld.sta_read()
    #     self.report_int32("sta", sta)
    #     # self.set_dataset("sta", sta)

    # @kernel
    # def switches(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     self.cpld.io_rst()
    #     self.cpld.cfg_sw(0, False)
    #     self.cpld.cfg_sw(0, True)
    #     self.cpld.cfg_sw(3, True)
    #     self.cpld.cfg_switches(0b1010)

    # @kernel
    # def switch_speed(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     n = 10
    #     t0 = self.core.get_rtio_counter_mu()
    #     for i in range(n):
    #         self.cpld.cfg_sw(3, bool(i & 1))
    #     self.set_dataset(
    #         "dt", self.core.mu_to_seconds(self.core.get_rtio_counter_mu() - t0) / n
    #     )

    # @kernel
    # def switches_readback(self):
    #     self.core.reset()  # clear switch TTLs
    #     self.cpld.init()
    #     sw_set = 0b1010
    #     self.cpld.cfg_switches(sw_set)
    #     sta_get = self.cpld.sta_read()
    #     self.set_dataset("sw_set", sw_set)
    #     self.set_dataset("sta_get", sta_get)

    # @kernel
    # def att(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     # clear backing state
    #     self.cpld.att_reg = 0
    #     att_set = 0x12345678
    #     self.cpld.set_all_att_mu(att_set)
    #     # confirm that we can set all attenuators and read back
    #     att_get = self.cpld.get_att_mu()
    #     # confirm backing state
    #     att_reg = self.cpld.att_reg
    #     self.set_dataset("att_set", att_set)
    #     self.set_dataset("att_get", att_get)
    #     self.set_dataset("att_reg", att_reg)

    # @kernel
    # def att_channel(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     # clear backing state
    #     self.cpld.att_reg = 0
    #     att_set = int32(0x87654321)
    #     # set individual attenuators
    #     self.cpld.set_att_mu(0, 0x21)
    #     self.cpld.set_att_mu(1, 0x43)
    #     self.cpld.set_att_mu(2, 0x65)
    #     self.cpld.set_att_mu(3, 0x87)
    #     # confirm that we can set all attenuators and read back
    #     att_get = self.cpld.get_att_mu()
    #     # confirm backing state
    #     att_reg = self.cpld.att_reg
    #     self.set_dataset("att_set", att_set)
    #     self.set_dataset("att_get", att_get)
    #     self.set_dataset("att_reg", att_reg)

    # @kernel
    # def att_channel_get(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     # clear backing state
    #     self.cpld.att_reg = 0
    #     att_set = [int32(0x21), int32(0x43), int32(0x65), int32(0x87)]
    #     # set individual attenuators
    #     for i in range(len(att_set)):
    #         self.cpld.set_att_mu(i, att_set[i])
    #     # confirm that we can set all attenuators and read back
    #     att_get = [0 for _ in range(len(att_set))]
    #     for i in range(len(att_set)):
    #         self.core.break_realtime()
    #         att_get[i] = self.cpld.get_channel_att_mu(i)
    #     # confirm backing state
    #     att_reg = self.cpld.att_reg
    #     self.set_dataset("att_set", att_set)
    #     self.set_dataset("att_get", att_get)
    #     self.set_dataset("att_reg", att_reg)

    # @kernel
    # def att_speed(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     n = 10
    #     t0 = self.core.get_rtio_counter_mu()
    #     for i in range(n):
    #         self.cpld.set_att(3, 30 * dB)
    #     self.set_dataset(
    #         "dt", self.core.mu_to_seconds(self.core.get_rtio_counter_mu() - t0) / n
    #     )

    # @kernel
    # def io_update(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     self.cpld.io_update.pulse_mu(int64(8))

    # @kernel
    # def sync(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     self.cpld.set_sync_div(2)

    # @kernel
    # def profile(self):
    #     self.core.break_realtime()
    #     self.cpld.init()
    #     self.cpld.set_profile(7)
    #     self.cpld.set_profile(0)


class UrukulTest(ExperimentCase):
    def test_instantiate(self):
        self.execute(UrukulExp, "instantiate")

    # def test_init(self):
    #     self.execute(UrukulExp, "init")

    # def test_cfg_write(self):
    #     self.execute(UrukulExp, "cfg_write")

    # def test_sta_read(self):
    #     self.execute(UrukulExp, "sta_read")
    #     sta = self.dataset_mgr.get("sta")
    #     print(hex(sta))
    #     self.assertEqual(urukul.urukul_sta_ifc_mode(sta), 0b0001)

    # def test_switches(self):
    #     self.execute(UrukulExp, "switches")

    # def test_switch_speed(self):
    #     self.execute(UrukulExp, "switch_speed")
    #     dt = self.dataset_mgr.get("dt")
    #     print(dt)
    #     self.assertLess(dt, 5 * us)

    # def test_switches_readback(self):
    #     self.execute(UrukulExp, "switches_readback")
    #     sw_get = urukul.urukul_sta_rf_sw(self.dataset_mgr.get("sta_get"))
    #     sw_set = self.dataset_mgr.get("sw_set")
    #     self.assertEqual(sw_get, sw_set)

    # def test_att(self):
    #     self.execute(UrukulExp, "att")
    #     att_set = self.dataset_mgr.get("att_set")
    #     self.assertEqual(att_set, self.dataset_mgr.get("att_get"))
    #     self.assertEqual(att_set, self.dataset_mgr.get("att_reg"))

    # def test_att_channel(self):
    #     self.execute(UrukulExp, "att_channel")
    #     att_set = self.dataset_mgr.get("att_set")
    #     self.assertEqual(att_set, self.dataset_mgr.get("att_get"))
    #     self.assertEqual(att_set, self.dataset_mgr.get("att_reg"))

    # def test_att_channel_get(self):
    #     self.execute(UrukulExp, "att_channel_get")
    #     att_set = self.dataset_mgr.get("att_set")
    #     self.assertListEqual(att_set, self.dataset_mgr.get("att_get"))
    #     att_reg = self.dataset_mgr.get("att_reg")
    #     for att in att_set:
    #         self.assertEqual(att, att_reg & 0xFF)
    #         att_reg >>= 8

    # def test_att_speed(self):
    #     self.execute(UrukulExp, "att_speed")
    #     dt = self.dataset_mgr.get("dt")
    #     print(dt)
    #     self.assertLess(dt, 5 * us)

    # def test_io_update(self):
    #     self.execute(UrukulExp, "io_update")

    # def test_sync(self):
    #     self.execute(UrukulExp, "sync")

    # def test_profile(self):
    #     self.execute(UrukulExp, "profile")
