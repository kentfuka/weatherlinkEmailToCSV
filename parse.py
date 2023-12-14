from lxml import etree
import re
s = """
<!DOCTYPE html>
<html lang='en'>
	<head>
		<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
		<meta name='viewport' content='width=device-width, initial-scale=1.0' />
		<title>Alarm email</title>
	</head>
	<body>
		<div style='letter-spacing: 596px; line-height: 0; mso-hide: all'>&nbsp;</div>
		<table width='550' cellpadding='0' cellspacing='0' border='0' align='center' bgcolor='#f3f3f3'>
			<tbody>
				<tr>
					<td>
						<table width='100%' cellpadding='0' cellspacing='0' border='0'>
							<tbody>
								<tr>
									<td>
										<table width='532' align='center' border='0' cellpadding='0' cellspacing='0'>
											<tbody>
												<tr>
													<td>
														<table width='532' align='left' border='0' cellpadding='0' cellspacing='0'>
															<tbody>
																<tr>
																	<td width='100%' height='7' bgcolor='#f3f3f3' style='font-size:1px; line-height:1px; mso-line-height-rule: exactly;'>&nbsp;</td>
																</tr>
																<tr>
																	<td width='100%' bgcolor='#ffffff'>
																		<table width='153' align='left' border='0' cellpadding='0' cellspacing='0'>
																			<tbody>
																				<tr>
																					<td width='153' height='45' align='left'>
																						<img src='http://static.weatherlink.com/images/email/commons/davis_logo.png' alt='' border='0' width='153' height='45' style='display:block; border:none; outline:none; text-decoration:none;'>
																						</td>
																					</tr>
																				</tbody>
																			</table>
																			<table width='350' align='right' border='0' cellpadding='0' cellspacing='0'>
																				<tbody>
																					<tr>
																						<td width='153' height='45' align='left' style='vertical-align: bottom; text-align: right; font-family: arial, serif; font-size: 12px; color: #3c464c;'>
																							<span style='display: inline-block; padding:3px 15px;'>As of 11:00 PM, Sun Aug 13 2023</span>
																						</td>
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																</tbody>
															</table>
															<table width='100%' cellpadding='0' cellspacing='0' border='0'>
																<tbody>
																	<tr>
																		<td>
																			<table width='532' align='center' cellspacing='0' cellpadding='0' border='0'>
																				<tbody>
																					<tr>
																						<td align='center' height='4' style='font-size:1px; line-height:1px;'>&nbsp;</td>
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																</tbody>
															</table>
															<table id="contentBlock" width='532' align='center' border='0' cellpadding='0' cellspacing='0' bgcolor='#ffffff'>
																<tbody>
																	<tr>
																		<td width='100%' height='13' style='font-size:1px; line-height:1px; mso-line-height-rule: exactly;'>&nbsp;</td>
																	</tr>
																	<tr>
																		<td height='36' style='font-family: arial, serif; font-size: 12px; line-height: 18px; color: #3c464c; text-align:left; padding-left: 15px;'>
																			<table width='200' align='left' border='0' cellpadding='0' cellspacing='0'>
																				<tbody>
																					<tr>
																						<td id='stationNameLabel' style='font-family: arial, serif; font-size: 12px;'>Station: Lamy Ridge Observatory</td>
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																	<tr>
																		<td width='100%' height='13' style='font-size:1px; line-height:1px; mso-line-height-rule: exactly;'>&nbsp;</td>
																	</tr>
																	<tr>
																		<td>
																			<table id="allSensorData" width='500' align='center' border='0' cellpadding='0' cellspacing='0' bgcolor='#ffffff' style='border: 1px solid #4c464c; border-collapse: collapse;'>
																				<thead>
																					<tr>
																						<th colspan='2' height='26' width='50%' style='text-align: left; font-family: arial, serif; font-size: 12px; background-color: #3c464c; padding-left: 15px; color: #ffffff;'> Weather Station </th>
																					</tr>
																				</thead>
																				<tbody>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Temp</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>68 &deg;F</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>High Temp</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>84 &deg;F at 2:17 PM</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Low Temp</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>59 &deg;F at 6:41 AM</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Hum</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>59 %</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Inside Temp</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>78 &deg;F</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Inside Hum</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>32 %</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Heat Index</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>68 &deg;F</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Wind Chill</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>69 &deg;F</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Dew Point</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>53 &deg;F</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Barometer</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>29.88 in Hg</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Wind Speed</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>4 mph</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Wind Direction</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>NNE</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>High Wind Speed</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>25 mph at 6:43 PM</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>10 Min Avg Wind</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>4 mph</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Rain Rate</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>0.00 in/h</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Day Rain</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>0.00 in</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Month Rain</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>0.19 in</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Year Rain</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>4.51 in</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>Solar Rad</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>0 W/m^2</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>High Solar Rad</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>1222 W/m^2 at 2:10 PM</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>UV Index</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>0</td>
																					</tr>
																					<tr>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px;border: 1px solid #e6e7e8'>High UV Index</td>
																						<td height='35' width='50%' style='font-family: arial, serif; font-size: 14px; padding-left: 15px; border: 1px solid #e6e7e8; text-align: center; color: #00a98e;'>7 at 12:43 PM</td>
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																	<tr>
																		<td width='100%' height='37' style='font-size:1px; line-height:1px; mso-line-height-rule: exactly;'>&nbsp;</td>
																	</tr>
																</tbody>
															</table>
															<table width='100%' cellpadding='0' cellspacing='0' border='0'>
																<tbody>
																	<tr>
																		<td>
																			<table width='532' align='center' cellspacing='0' cellpadding='0' border='0'>
																				<tbody>
																					<tr>
																						<td align='center' height='18' style='font-size:1px; line-height:1px;'>&nbsp;</td>
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
										</td>
									</tr>
								</tbody>
							</table>
							<table width='100%' cellpadding='0' cellspacing='0' border='0'>
								<tbody>
									<tr>
										<td>
											<table width='532' cellpadding='0' cellspacing='0' border='0' align='center'>
												<tbody>
													<tr>
														<td width='100%' height='13'></td>
													</tr>
													<tr>
														<td align='center' valign='middle' style='font-family: arial, serif; font-size: 12px; color: #808285'> This email has been sent to kent@kncl.com at your request. </td>
													</tr>
													<tr>
														<td width='100%' height='5'></td>
													</tr>
													<tr>
														<td align='center' valign='middle' style='font-family: arial, serif; font-size: 12px; color: #808285'> Davis Instruments Inc., 3465 Diablo Ave, Hayward, CA 94545 </td>
													</tr>
													<tr>
														<td width='100%' height='18'></td>
													</tr>
													<tr>
														<td align='center' valign='middle' style='font-family: arial, serif; font-size: 12px; color: #808285'>
															<a href=https://www.weatherlink.com/unsubscribe/1/19771/3:6e702d59:e835078c96cc>Unsubscribe</a>
														</td>
													</tr>
													<tr>
														<td width='100%' height='18'></td>
													</tr>
												</tbody>
											</table>
										</td>
									</tr>
								</tbody>
							</table>
						</td>
					</tr>
				</tbody>
			</table>
		</body>
	</html>
"""

span = etree.HTML(s).xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/span")
datetext = str(span[0].text).strip()
print('{')
print('"date":"'+datetext+'",')
target_id = 'allSensorData'
results = etree.HTML(s).xpath("//table[@id = '%s']/tbody/tr" % target_id)
if not results:
    raise Exception("target_id does not exist")

rows = iter(results)
for row in rows:
    for tr in row.iter('tr'):         
        text0 = str(tr[0].text).strip()
        text1 = str(tr[1].text).strip()
        print('"'+text0+'":"'+text1+'",')
print('"end":""')
print('},')
