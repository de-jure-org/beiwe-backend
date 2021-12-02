from constants.data_stream_constants import (ACCELEROMETER, AMBIENT_AUDIO, ANDROID_LOG_FILE,
    BLUETOOTH, CALL_LOG, DEVICEMOTION, GPS, GYRO, IDENTIFIERS, IMAGE_FILE, IOS_LOG_FILE,
    MAGNETOMETER, POWER_STATE, PROXIMITY, REACHABILITY, SURVEY_ANSWERS, SURVEY_TIMINGS, TEXTS_LOG,
    VOICE_RECORDING, WIFI)


# dictionary for printing PROCESSED data streams for frontend
# necessary even with the complete data stream dict for parsing data from the backend
PROCESSED_DATA_STREAM_DICT = {
    "responsiveness": "Responsiveness",
    "outgoing_calllengths": "Outgoing Call Lengths",
    "call_indegree": "Call In Degree",
    "incoming_calllengths": "Incoming Call Lengths",
    "reciprocity": "Reciprocity",
    "call_outdegree": "Call Out Degree",
    "incoming_calls": "Incoming Calls",
    "outgoing_calls": "Outgoing Calls",
    "outgoing_textlengths": "Outgoing Text Lengths",
    "text_indegree": "Text In Degree",
    "incoming_textlengths": "Incoming Text Lengths",
    "text_outdegree": "Text Out Degree",
    "incoming_texts": "Incoming Texts",
    "outgoing_texts": "Outgoing Texts",
    "RoG_km": "RoG (km)",
    "MaxDiam_km": "Maximum Diameter (km)",
    "StdFlightDur_min": "Standard Flight Duration (min)",
    "AvgFlightLen_km": "Average Flight Length (km)",
    "Hometime_hrs": "Home Time (hours)",
    "AvgFlightDur_min": "Average Flight Duration (min)",
    "DistTravelled_km": "Distance Travelled (km)",
    "StdFlightLen_km": "Standard Flight Length (km)",
    "MaxHomeDist_km": "Maximum Home Distance (km)",
}


# dictionary for printing ALL data streams (processed and bytes)
COMPLETE_DATA_STREAM_DICT = {
    "responsiveness": "Responsiveness",
    "outgoing_calllengths": "Outgoing Call Lengths",
    "call_indegree": "Call In Degree",
    "incoming_calllengths": "Incoming Call Lengths",
    "reciprocity": "Reciprocity",
    "call_outdegree": "Call Out Degree",
    "incoming_calls": "Incoming Calls",
    "outgoing_calls": "Outgoing Calls",
    "outgoing_textlengths": "Outgoing Text Lengths",
    "text_indegree": "Text In Degree",
    "incoming_textlengths": "Incoming Text Lengths",
    "text_outdegree": "Text Out Degree",
    "incoming_texts": "Incoming Texts",
    "outgoing_texts": "Outgoing Texts",
    "RoG_km": "RoG (km)",
    "MaxDiam_km": "Maximum Diameter (km)",
    "StdFlightDur_min": "Standard Flight Duration (min)",
    "AvgFlightLen_km": "Average Flight Length (km)",
    "Hometime_hrs": "Home Time (hours)",
    "AvgFlightDur_min": "Average Flight Duration (min)",
    "DistTravelled_km": "Distance Travelled (km)",
    "StdFlightLen_km": "Standard Flight Length (km)",
    "MaxHomeDist_km": "Maximum Home Distance (km)",
    ACCELEROMETER: "Accelerometer (bytes)",
    AMBIENT_AUDIO: "Ambient Audio Recording (bytes)",
    ANDROID_LOG_FILE: "Android Log File (bytes)",
    BLUETOOTH: "Bluetooth (bytes)",
    CALL_LOG: "Call Log (bytes)",
    DEVICEMOTION: "Device Motion (bytes)",
    GPS: "GPS (bytes)",
    GYRO: "Gyro (bytes)",
    IDENTIFIERS: "Identifiers (bytes)",
    IMAGE_FILE: "Image Survey (bytes)",
    IOS_LOG_FILE: "iOS Log File (bytes)",
    MAGNETOMETER: "Magnetometer (bytes)",
    POWER_STATE: "Power State (bytes)",
    PROXIMITY: "Proximity (bytes)",
    REACHABILITY: "Reachability (bytes)",
    SURVEY_ANSWERS: "Survey Answers (bytes)",
    SURVEY_TIMINGS: "Survey Timings (bytes)",
    TEXTS_LOG: "Text Log (bytes)",
    VOICE_RECORDING: "Audio Recordings (bytes)",
    WIFI: "Wifi (bytes)",
}
