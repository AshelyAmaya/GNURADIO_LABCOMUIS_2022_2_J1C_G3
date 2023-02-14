#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: MultiplexaPAM
# Author: Ashely_Amaya_Otto_Andrade_J1C_G3
# Copyright: UIS
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from ModuladorPAM import ModuladorPAM  # grc-generated hier_block
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class MultiplexaPAM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "MultiplexaPAM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MultiplexaPAM")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "MultiplexaPAM")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.fs = fs = 2000
        self.fm = fm = 100
        self.GTX = GTX = 1
        self.Fc = Fc = 50000000
        self.D3 = D3 = 75
        self.D2 = D2 = 50
        self.D1 = D1 = 25
        self.D = D = 25
        self.Am = Am = 1

        ##################################################
        # Blocks
        ##################################################
        self._fs_range = Range(0, 10000, 1, 2000, 200)
        self._fs_win = RangeWidget(self._fs_range, self.set_fs, "Frecuencia de pulsos", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fs_win)
        self._fm_range = Range(0, 10000, 10, 100, 200)
        self._fm_win = RangeWidget(self._fm_range, self.set_fm, "Frecuencia mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self._D3_range = Range(0, 100, 1, 75, 200)
        self._D3_win = RangeWidget(self._D3_range, self.set_D3, "Retardo 3", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D3_win)
        self._D2_range = Range(0, 100, 1, 50, 200)
        self._D2_win = RangeWidget(self._D2_range, self.set_D2, "Retardo 2", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D2_win)
        self._D1_range = Range(0, 100, 1, 25, 200)
        self._D1_win = RangeWidget(self._D1_range, self.set_D1, "Retardo 1", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D1_win)
        self._D_range = Range(0, 50, 1, 25, 200)
        self._D_win = RangeWidget(self._D_range, self.set_D, "Ancho pulso", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_win)
        self._Am_range = Range(0, 10, 0.1, 1, 200)
        self._Am_win = RangeWidget(self._Am_range, self.set_Am, "Amplitud mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Am_win)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
            1024*4, #size
            samp_rate, #samp_rate
            "", #name
            4, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024*4, #size
            samp_rate, #samp_rate
            "", #name
            5, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_delay_5 = blocks.delay(gr.sizeof_float*1, 100-D3)
        self.blocks_delay_4 = blocks.delay(gr.sizeof_float*1, 100-D2)
        self.blocks_delay_3 = blocks.delay(gr.sizeof_float*1, 100-D1)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_float*1, D2)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, D3)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 100-0)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, D1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_3 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, Am, 0, 0)
        self.ModuladorPAM_3 = ModuladorPAM(
            d=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_2 = ModuladorPAM(
            d=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_1_0_2 = ModuladorPAM(
            d=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_1_0_1 = ModuladorPAM(
            d=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_1_0_0 = ModuladorPAM(
            d=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_1_0 = ModuladorPAM(
            d=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_1 = ModuladorPAM(
            d=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_0 = ModuladorPAM(
            d=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self._GTX_range = Range(0, 30, 1, 1, 200)
        self._GTX_win = RangeWidget(self._GTX_range, self.set_GTX, "Ganancia del transmisor", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._GTX_win)
        self._Fc_range = Range(50000000, 2000000000, 1000000, 50000000, 200)
        self._Fc_win = RangeWidget(self._Fc_range, self.set_Fc, "Frecuencia portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Fc_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModuladorPAM_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.ModuladorPAM_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.ModuladorPAM_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ModuladorPAM_1_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.ModuladorPAM_1_0_0, 0), (self.qtgui_time_sink_x_2, 1))
        self.connect((self.ModuladorPAM_1_0_1, 0), (self.qtgui_time_sink_x_2, 2))
        self.connect((self.ModuladorPAM_1_0_2, 0), (self.qtgui_time_sink_x_2, 3))
        self.connect((self.ModuladorPAM_2, 0), (self.blocks_delay_2, 0))
        self.connect((self.ModuladorPAM_3, 0), (self.blocks_delay_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.ModuladorPAM_1, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.ModuladorPAM_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.ModuladorPAM_2, 0))
        self.connect((self.analog_sig_source_x_3, 0), (self.ModuladorPAM_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_delay_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_delay_4, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_delay_5, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.ModuladorPAM_1_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_1, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_delay_2, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_2, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_3, 0), (self.ModuladorPAM_1_0_0, 0))
        self.connect((self.blocks_delay_4, 0), (self.ModuladorPAM_1_0_1, 0))
        self.connect((self.blocks_delay_5, 0), (self.ModuladorPAM_1_0_2, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "MultiplexaPAM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.ModuladorPAM_0.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_1.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_1_0.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_1_0_0.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_1_0_1.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_1_0_2.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_2.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_3.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.ModuladorPAM_0.set_fs(self.fs)
        self.ModuladorPAM_1.set_fs(self.fs)
        self.ModuladorPAM_1_0.set_fs(self.fs)
        self.ModuladorPAM_1_0_0.set_fs(self.fs)
        self.ModuladorPAM_1_0_1.set_fs(self.fs)
        self.ModuladorPAM_1_0_2.set_fs(self.fs)
        self.ModuladorPAM_2.set_fs(self.fs)
        self.ModuladorPAM_3.set_fs(self.fs)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)
        self.analog_sig_source_x_1.set_frequency(self.fm)
        self.analog_sig_source_x_2.set_frequency(self.fm)
        self.analog_sig_source_x_3.set_frequency(self.fm)

    def get_GTX(self):
        return self.GTX

    def set_GTX(self, GTX):
        self.GTX = GTX

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc

    def get_D3(self):
        return self.D3

    def set_D3(self, D3):
        self.D3 = D3
        self.blocks_delay_1.set_dly(self.D3)
        self.blocks_delay_5.set_dly(100-self.D3)

    def get_D2(self):
        return self.D2

    def set_D2(self, D2):
        self.D2 = D2
        self.blocks_delay_2.set_dly(self.D2)
        self.blocks_delay_4.set_dly(100-self.D2)

    def get_D1(self):
        return self.D1

    def set_D1(self, D1):
        self.D1 = D1
        self.blocks_delay_0.set_dly(self.D1)
        self.blocks_delay_3.set_dly(100-self.D1)

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.ModuladorPAM_0.set_d(self.D)
        self.ModuladorPAM_1.set_d(self.D)
        self.ModuladorPAM_1_0.set_d(self.D)
        self.ModuladorPAM_1_0_0.set_d(self.D)
        self.ModuladorPAM_1_0_1.set_d(self.D)
        self.ModuladorPAM_1_0_2.set_d(self.D)
        self.ModuladorPAM_2.set_d(self.D)
        self.ModuladorPAM_3.set_d(self.D)

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
        self.analog_sig_source_x_0.set_amplitude(self.Am)
        self.analog_sig_source_x_1.set_amplitude(self.Am)
        self.analog_sig_source_x_2.set_amplitude(self.Am)
        self.analog_sig_source_x_3.set_amplitude(self.Am)




def main(top_block_cls=MultiplexaPAM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
