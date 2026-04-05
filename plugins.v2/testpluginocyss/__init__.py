from typing import Any, Dict, List, Tuple

from app.plugins import _PluginBase


class TestPluginOcyss(_PluginBase):
    # 插件名称
    plugin_name = "自用测试插件"
    # 插件描述
    plugin_desc = "Ocyss自用"
    # 插件图标
    plugin_icon = "https://raw.githubusercontent.com/ocyss/TMoviePilot-Plugins/main/icons/icon.jpg"
    # 插件版本
    plugin_version = "0.0.1"
    # 插件作者
    plugin_author = "ocyss"
    # 作者主页
    author_url = "https://github.com/ocyss"
    # 插件配置项ID前缀
    plugin_config_prefix = "testpluginocyss_"
    # 加载顺序
    plugin_order = 99999999
    # 可使用的用户级别
    auth_level = 0

    # 私有属性
    _enabled = False

    _old_set_and_check_auth_level = None

    def init_plugin(self, config: dict | None = None):
        if config:
            from app.utils import PluginManager

            self._enabled = config.get("enabled")

            if self._enabled:
                self._old_set_and_check_auth_level = (
                    PluginManager._PluginManager__set_and_check_auth_level
                )
                PluginManager._PluginManager__set_and_check_auth_level = (
                    lambda *args, **kwargs: True
                )
            elif self._old_set_and_check_auth_level:
                PluginManager._PluginManager__set_and_check_auth_level = (
                    self._old_set_and_check_auth_level
                )
                self._old_set_and_check_auth_level = None

    def get_api(self) -> List[Dict[str, Any]]:
        return []

    def get_service(self) -> List[Dict[str, Any]]:
        return []

    def get_page(self) -> List[dict]:
        return []

    def get_form(self) -> Tuple[List[dict], Dict[str, Any]]:
        return [
            {
                "component": "VForm",
                "content": [
                    {
                        "component": "VRow",
                        "content": [
                            {
                                "component": "VCol",
                                "props": {"cols": 12, "md": 6},
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "enabled",
                                            "label": "启用插件",
                                        },
                                    }
                                ],
                            }
                        ],
                    },
                ],
            }
        ], {"enabled": True}

    @staticmethod
    def get_command() -> List[Dict[str, Any]]:
        return []

    def stop_service(self):
        pass
