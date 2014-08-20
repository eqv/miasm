#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Machine(object):
    """Abstract machine architecture to restrict architecture dependant code"""

    __dis_engine = None   # Disassembly engine
    __mn = None           # Machine instance
    __ira = None          # IR analyser

    __available = ["arm", "armt", "sh4", "x86_16", "x86_32", "x86_64", "msp430",
                   "mips32b", "mips32l"]


    def __init__(self, machine_name):

        # Import on runtime for performance issue
        if machine_name == "arm":
            from miasm2.arch.arm.disasm import dis_arm as dis_engine
            from miasm2.arch.arm.arch import mn_arm as mn
            from miasm2.arch.arm.ira import ir_a_arm as ira
        elif machine_name == "armt":
            from miasm2.arch.arm.disasm import dis_armt as dis_engine
            from miasm2.arch.arm.arch import mn_armt as mn
            from miasm2.arch.arm.ira import ir_a_armt as ira
        elif machine_name == "sh4":
            from miasm2.arch.sh4.disasm import dis_sha4 as dis_engine
            from miasm2.arch.sh4.arch import mn_sh4 as mn
            from miasm2.arch.sh4.ira import ir_a_sh4 as ira
        elif machine_name == "x86_16":
            from miasm2.arch.x86.disasm import dis_x86_16 as dis_engine
            from miasm2.arch.x86.arch import mn_x86 as mn
            from miasm2.arch.x86.ira import ir_a_x86_16 as ira
        elif machine_name == "x86_32":
            from miasm2.arch.x86.disasm import dis_x86_32 as dis_engine
            from miasm2.arch.x86.arch import mn_x86 as mn
            from miasm2.arch.x86.ira import ir_a_x86_32 as ira
        elif machine_name == "x86_64":
            from miasm2.arch.x86.disasm import dis_x86_64 as dis_engine
            from miasm2.arch.x86.arch import mn_x86 as mn
            from miasm2.arch.x86.ira import ir_a_x86_64 as ira
        elif machine_name == "msp430":
            from miasm2.arch.msp430.disasm import dis_msp430 as dis_engine
            from miasm2.arch.msp430.arch import mn_msp430 as mn
            from miasm2.arch.msp430.ira import ir_a_msp430 as ira
        elif machine_name == "mips32b":
            from miasm2.arch.mips32.disasm import dis_mips32b as dis_engine
            from miasm2.arch.mips32.arch import mn_mips32b as mn
            from miasm2.arch.mips32.ira import ir_a_mips32 as ira
        elif machine_name == "mips32l":
            from miasm2.arch.mips32.disasm import dis_mips32l as dis_engine
            from miasm2.arch.mips32.arch import mn_mips32l as mn
            from miasm2.arch.mips32.ira import ir_a_mips32 as ira
        else:
            raise ValueError('Unknown machine: %s' % machine_name)

        self.__dis_engine = dis_engine
        self.__mn = mn
        self.__ira = ira

    def get_dis_engine(self):
        return self.__dis_engine
    dis_engine = property(get_dis_engine)

    def get_mn(self):
        return self.__mn
    mn = property(get_mn)

    def get_ira(self):
        return self.__ira
    ira = property(get_ira)

    @classmethod
    def available_machine(cls):
        "Return a list of supported machines"
        return cls.__available