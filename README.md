# IEC62056-Slave-Simulator
IEC62056 Electricity Meter Protocol Simulator 

This software package can be used as a simulation enviroment for returning virtual readout data.

Master Device (Datalogger, Gateway, AMR Agents) can read numerous readout data by using this test software.

Electricity meter brands which are very common in Turkey are implemented in software (LUNA, VIKO, MAKEL and KOHLER)

User can configure serial communication settings, meter brands and serial numbers by using AMRParams.json file.

By configuring "CommunicationEnable" JSON object, user should enable/disable the communication of selected electricty meter.
