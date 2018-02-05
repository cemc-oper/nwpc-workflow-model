import os

from nwpc_work_flow_model.sms.sms_status_analyzer import SmsStatusAnalyzer


class TestSmsStatusAnalyzer:
    @classmethod
    def setup_class(cls):
        pass

    def test_normal_suite(self):
        with open(os.path.dirname(__file__) + "/data/cdp/status/normal_status.txt") as f:
            cdp_output = f.readlines()
            analyzer = SmsStatusAnalyzer()
            node_status_list = analyzer.analyse_node_status(cdp_output)
            for node_status in node_status_list:
                print(node_status['path'])
