from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform, VivadoProgrammer


_io_common = [
    ("led1", 0, Pins("A17"), IOStandard("LVCMOS33")),
    ("led2", 0, Pins("C16"), IOStandard("LVCMOS33")),

    ("btn0", 0, Pins("A18"), IOStandard("LVCMOS33")),
    ("btn1", 0, Pins("B18"), IOStandard("LVCMOS33")),

    ("clk100", 0, Pins("L17"), IOStandard("LVCMOS33")),

    # ("serial", 0,
    #     Subsignal("rx", Pins("N13")),  # FPGA input, schematics TxD_2V5
    #     Subsignal("tx", Pins("N17")),  # FPGA output, schematics RxD_2V5
    #     IOStandard("LVCMOS25")
    # ),
    #
    # ("vusb_present", 0, Pins("M17"), IOStandard("LVCMOS25")),
    #
    # ("sfp_ctl", 0,
    #     Subsignal("mod_def1", Pins("U7")),
    #     Subsignal("mod_def2", Pins("T3")),
    #     Subsignal("los", Pins("P15")),
    #     Subsignal("mod_present", Pins("U16")),
    #     Subsignal("rate_select", Pins("N15")),
    #     Subsignal("tx_disable", Pins("R14")),
    #     Subsignal("tx_fault", Pins("N14")),
    #     Subsignal("led", Pins("P16")),
    #     IOStandard("LVCMOS25")
    # ),
    # ("i2c", 0,
    #     Subsignal("scl", Pins("J16")),
    #     Subsignal("sda", Pins("F15")),
    #     IOStandard("LVCMOS25")
    # ),
    #
    # ("spiflash", 0,
    #     Subsignal("cs_n", Pins("T19")),
    #     Subsignal("dq", Pins("P22 R22 P21 R21")),
    #     # "clk" is on CCLK
    #     IOStandard("LVCMOS25")
    # ),
    # ("spiflash2x", 0,
    #     Subsignal("cs_n", Pins("T19")),
    #     Subsignal("dq", Pins("P22 R22")),
    #     Subsignal("wp", Pins("P21")),
    #     Subsignal("hold", Pins("R21")),
    #     # "clk" is on CCLK
    #     IOStandard("LVCMOS25")
    # ),
    # ("ddram", 0,
    #     Subsignal("a", Pins(
    #         "L6 M5 P6 K6 M1 M3 N2 M6 "
    #         "P1 P2 L4 N5 L3 R1 N3"),
    #         IOStandard("SSTL15")),
    #     Subsignal("ba", Pins("L5 M2 N4"), IOStandard("SSTL15")),
    #     Subsignal("ras_n", Pins("J4"), IOStandard("SSTL15")),
    #     Subsignal("cas_n", Pins("J6"), IOStandard("SSTL15")),
    #     Subsignal("we_n", Pins("K3"), IOStandard("SSTL15")),
    #     # Subsignal("cs_n", Pins(""), IOStandard("SSTL15")),
    #     Subsignal("dm", Pins("G2 E2"), IOStandard("SSTL15")),
    #     Subsignal("dq", Pins(
    #         "G3 J1 H4 H5 H2 K1 H3 J5 "
    #         "G1 B1 F1 F3 C2 A1 D2 B2"),
    #         IOStandard("SSTL15"),
    #         Misc("IN_TERM=UNTUNED_SPLIT_50")),
    #     Subsignal("dqs_p", Pins("K2 E1"), IOStandard("DIFF_SSTL15")),
    #     Subsignal("dqs_n", Pins("J2 D1"), IOStandard("DIFF_SSTL15")),
    #     Subsignal("clk_p", Pins("P5"), IOStandard("DIFF_SSTL15")),
    #     Subsignal("clk_n", Pins("P4"), IOStandard("DIFF_SSTL15")),
    #     Subsignal("cke", Pins("L1"), IOStandard("SSTL15")),
    #     Subsignal("odt", Pins("K4"), IOStandard("SSTL15")),
    #     Subsignal("reset_n", Pins("G4"), IOStandard("LVCMOS15")),
    #     Misc("SLEW=FAST"),
    # ),
]


_connectors = [
    # ("eem0", {
    #     "d0_cc_n": "T4",
    #     "d0_cc_p": "R4",
    #     "d1_n": "R2",
    #     "d1_p": "R3",
    #     "d2_n": "U1",
    #     "d2_p": "T1",
    #     "d3_n": "V2",
    #     "d3_p": "U2",
    #     "d4_n": "Y1",
    #     "d4_p": "W1",
    #     "d5_n": "Y2",
    #     "d5_p": "W2",
    #     "d6_n": "AB1",
    #     "d6_p": "AA1",
    #     "d7_n": "AA4",
    #     "d7_p": "Y4",
    # }),
]


class Platform(XilinxPlatform):
    default_clk_name = "clk100"
    default_clk_period = 10.0

    def __init__(self):
        XilinxPlatform.__init__(
                self, "xc7a15t-cpg236-1", _io_common, _connectors,
                toolchain="vivado")
        self.toolchain.bitstream_commands.extend([
            "set_property BITSTREAM.GENERAL.COMPRESS True [current_design]",
            "set_property BITSTREAM.CONFIG.CONFIGRATE 33 [current_design]",
            "set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 2 [current_design]",
            "set_property CFGBVS VCCO [current_design]",
            "set_property CONFIG_VOLTAGE 3.3 [current_design]",
            ])

    def create_programmer(self):
        return VivadoProgrammer()