sms_r = "FRST;22A;5;4af3d5;drc;20240327104124;-8.7912;25.8572;3;0;10;245;287;15;14;0;5;5;4;4;9;0;2;1;firstsmsend;SCND;22A;5;4af3d5;drc;20240327104124;-8.7912;25.8572;3;0;10;245;287;15;14;0;5;5;4;4;9;0;2;1;secondsmsend"
sms_rt = "ACAS;34A;14;be208e;drc;20240417144143;47.5097;19.2157;14;12;233;4505;9664;20240418;2;12;34;56;78;901;23;45;67;89;01;234;56;78;90;12;34;56;78;20240419"
long_sms = len(sms_rt)
first_part = sms_r[:160]
scnd_part = sms_r[160:]
cnt_first_part = len(first_part)
print(f"until 160: {first_part}")
print(f"the rest of it: {scnd_part}")
print(f"count the long sms: {long_sms}")
print(f"count first part: {cnt_first_part}")

sms_1 = ("TESTfrst;22A;5;4af3d5;drc;20240327104124;-8.7912;25.8572;3;0;10;245;287;15;14;0;5;5;4;4;9;0;2;1;firstsmsend;")
cnt_1 = len(sms_1)
print(cnt_1)

