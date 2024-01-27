from IssaScope import Ui_MainWindow
from Settings import *


def Opto_Arrays(self):
    self.ui.Opto_nLED = 4

    self.ui.Opto_LED_toggleButton = [self.ui.Opto1_toggleButton,
                                    self.ui.Opto2_toggleButton,
                                    self.ui.Opto3_toggleButton,
                                    self.ui.Opto4_toggleButton
                                    ]

    self.ui.Opto_LED_Slider = [self.ui.Opto1_Slider,
                               self.ui.Opto2_Slider,
                               self.ui.Opto3_Slider,
                               self.ui.Opto4_Slider
                               ]

    self.ui.Opto_LED_Value = [self.ui.Opto1_Value,
                              self.ui.Opto2_Value,
                              self.ui.Opto3_Value,
                              self.ui.Opto4_Value
                              ]

    self.ui.Opto_LED_toggleButton_layout = [self.ui.Opto1_toggleButton_layout,
                                            self.ui.Opto2_toggleButton_layout,
                                            self.ui.Opto3_toggleButton_layout,
                                            self.ui.Opto4_toggleButton_layout
                                            ]

    self.ui.Opto_Dataframe = ["Opto1",
                              "Opto2",
                              "Opto3",
                              "Opto4"
                              ]

    Opto_df_LED01 = None
    Opto_df_LED02 = None
    Opto_df_LED03 = None
    Opto_df_LED04 = None

    self.ui.Opto_Df = [Opto_df_LED01,
                       Opto_df_LED02,
                       Opto_df_LED03,
                       Opto_df_LED04
                      ]


    self.ui.Opto_Brush = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]
                          ]


def White_Arrays(self):
    self.ui.White_nLED = 4

    self.ui.White_LED_toggleButton = [self.ui.White1_toggleButton,
                                      self.ui.White2_toggleButton,
                                      self.ui.White3_toggleButton,
                                      self.ui.White4_toggleButton,
                                      self.ui.AllWhite_toggleButton
                                      ]

    self.ui.White_LED_Slider = [self.ui.White1_Slider,
                                self.ui.White2_Slider,
                                self.ui.White3_Slider,
                                self.ui.White4_Slider,
                                self.ui.AllWhite_Slider
                            ]

    self.ui.White_LED_Value = [self.ui.White1_Value,
                               self.ui.White2_Value,
                               self.ui.White3_Value,
                               self.ui.White4_Value,
                               self.ui.AllWhite_Value
                               ]

    self.ui.White_LED_toggleButton_layout = [self.ui.White1_toggleButton_layout,
                                             self.ui.White2_toggleButton_layout,
                                             self.ui.White3_toggleButton_layout,
                                             self.ui.White4_toggleButton_layout,
                                             self.ui.AllWhite_toggleButton_layout
                                             ]


def IR_Arrays(self):
    self.ui.IR_nLED = 4

    self.ui.IR_LED_toggleButton = [self.ui.IR1_toggleButton,
                                   self.ui.IR2_toggleButton,
                                   self.ui.IR3_toggleButton,
                                   self.ui.IR4_toggleButton,
                                   self.ui.AllIR_toggleButton
                                   ]

    self.ui.IR_LED_Slider = [self.ui.IR1_Slider,
                             self.ui.IR2_Slider,
                             self.ui.IR3_Slider,
                             self.ui.IR4_Slider,
                             self.ui.AllIR_Slider
                             ]

    self.ui.IR_LED_Value = [self.ui.IR1_Value,
                            self.ui.IR2_Value,
                            self.ui.IR3_Value,
                            self.ui.IR4_Value,
                            self.ui.AllIR_Value
                            ]

    self.ui.IR_LED_toggleButton_layout = [self.ui.IR1_toggleButton_layout,
                                          self.ui.IR2_toggleButton_layout,
                                          self.ui.IR3_toggleButton_layout,
                                          self.ui.IR4_toggleButton_layout,
                                          self.ui.AllIR_toggleButton_layout
                                          ]
