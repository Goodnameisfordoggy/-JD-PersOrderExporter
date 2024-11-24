'''
Author: HDJ
StartDate: 2024-05-15 00:00:00
LastEditTime: 2024-11-21 01:09:12
FilePath: \pythond:\LocalUsers\Goodnameisfordoggy-Gitee\JD-Automated-Tools\JD-PersDataExporter\src\dataPortector.py
Description: 

                *       写字楼里写字间，写字间里程序员；
                *       程序人员写程序，又拿程序换酒钱。
                *       酒醒只在网上坐，酒醉还来网下眠；
                *       酒醉酒醒日复日，网上网下年复年。
                *       但愿老死电脑间，不愿鞠躬老板前；
                *       奔驰宝马贵者趣，公交自行程序员。
                *       别人笑我忒疯癫，我笑自己命太贱；
                *       不见满街漂亮妹，哪个归得程序员？    
Copyright (c) 2024 by HDJ, All Rights Reserved. 
'''
import os
import json
from src.logger import get_logger
LOG = get_logger()

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(WORKING_DIRECTORY_PATH, "config\config.json")

class OrderExportConfig:
    def __init__(
        self,
        *,
        data_retrieval_mode: str = "",
        high_search: str = "",
        date_search: str = "",
        status_search: str = "",
        headers: list[str] = [],
        masking_intensity: dict[str, int] = {},
        excel_storage_settings: dict[any] = {},
    ):
        self.data_retrieval_mode = data_retrieval_mode
        self.high_search = high_search
        self.date_search = date_search
        self.status_search = status_search
        self.headers = headers
        self.masking_intensity = masking_intensity
        self.excel_storage_settings = excel_storage_settings

    @classmethod
    def from_json_file(cls, file_path: str = CONFIG_PATH) -> "OrderExportConfig":
        """从配置文件初始化配置对象"""
        with open(file_path, "r", encoding="utf-8") as file:
            config_data = json.load(file)  # 假设配置文件是 JSON 格式
        return cls(
            data_retrieval_mode=config_data.get("data_retrieval_mode", ""),
            high_search=config_data.get("high_search", ""),
            date_search=config_data.get("date_search", ""),
            status_search=config_data.get("status_search", ""),
            headers=config_data.get("headers", []),
            masking_intensity=config_data.get("masking_intensity", {}),
            excel_storage_settings=config_data.get("excel_storage_settings", {}),
        )

    def validate(self):
        """验证配置是否符合要求"""
        if not self.data_retrieval_mode or not isinstance(self.data_retrieval_mode, str):
            raise ValueError("data_retrieval_mode 必须是非空字符串")
        if not isinstance(self.headers, list) or not all(isinstance(header, str) for header in self.headers):
            raise ValueError("headers 必须是包含字符串的非空列表")
        if not isinstance(self.masking_intensity, dict):
            raise ValueError("masking_intensity 必须是字典")
        if not isinstance(self.excel_storage_settings, dict):
            raise ValueError("excel_storage_settings 必须是字典")
        return True

    def get_headers_settings(self) -> dict[str, any]:
        """返回 Excel 表头配置信息"""
        return self.excel_storage_settings.get("headers_settings", {})

    def get_masking_level(self, field: str) -> int:
        """获取指定字段的屏蔽级别"""
        return self.masking_intensity.get(field, 0)

    def __repr__(self):
        return (
            "<OrderExportConfig("
            f"data_retrieval_mode={self.data_retrieval_mode}, "
            f"high_search={self.high_search}, "
            f"date_search={self.date_search}, "
            f"status_search={self.status_search}, "
            f"masking_intensity={self.masking_intensity}, "
            f"excel_storage_settings={self.excel_storage_settings}, "
            ")>"
        )
    