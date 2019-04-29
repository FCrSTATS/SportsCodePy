from xml.etree import ElementTree as ET
import pandas as pd

def players_as_rows(dat, period1_start, period2_start, player,
                 team, time, lead_time, lag_time, metric_val,
                 period_id, ID, metric_label,
                 export_filename, period3_start = 0,
                 period4_start = 0,):

    df = pd.DataFrame()
    df['ID'] = dat[ID].astype(str)
    df['period'] = dat[period_id].astype(int)
    df['player_name'] = dat[player]
    df['team_name'] = dat[team]
    df['time'] = dat[time].astype(int)
    df['metric'] = dat[metric_val]

    periods = [period1_start, period2_start, period3_start, period4_start]

    new_starts = []
    new_ends = []

    for row in range(0,len(df)):
        new_time = df.iloc[row]['time'] + periods[df.iloc[row]['period']-1]
        new_start = new_time - lead_time
        new_end = new_time + lag_time
        new_starts.append(new_start)
        new_ends.append(new_end)

    df['start'] = new_starts
    df['end'] = new_ends

    # build a tree structure
    root = ET.Element("file")
    header1 = ET.SubElement(root, "SORT_INFO")
    header1.text = ""
    header2 = ET.SubElement(header1, "sort_type")
    header2.text = "sort order"
    instances = ET.SubElement(root, "ALL_INSTANCES")

    for i in range(0, len(df)):

        instances_mini = ET.SubElement(instances, "instance")

        instances_ID = ET.SubElement(instances_mini, "ID")
        instances_ID.text = df.iloc[i]['ID']

        instances_code = ET.SubElement(instances_mini, "code")
        instances_code.text = df.iloc[i]['player_name']

        instances_start = ET.SubElement(instances_mini, "start")
        instances_start.text = str(df.iloc[i]['start'])

        instances_end = ET.SubElement(instances_mini, "end")
        instances_end.text = str(df.iloc[i]['end'])

        instances_label = ET.SubElement(instances_mini, "label")
        instances_metric = ET.SubElement(instances_label, "group")
        instances_metric.text = metric_label
        instances_metricB = ET.SubElement(instances_label, "text")
        instances_metricB.text = metric_label + ": " + str(df.iloc[i]['metric'])

        instances_label2 = ET.SubElement(instances_mini, "label")
        instances_metric2 = ET.SubElement(instances_label2, "group")
        instances_metric2.text = "Team"
        instances_metric3 = ET.SubElement(instances_label2, "text")
        instances_metric3.text = str(df.iloc[i]['team_name'])


#         <label><group>Team</group><text>Barcelona</text></label>

    # wrap it in an ElementTree instance, and save as XML
    tree = ET.ElementTree(root)

    tree.write(export_filename,
               xml_declaration=True,
               encoding='utf-8',
               method="xml")

    return("XML created successfully")
