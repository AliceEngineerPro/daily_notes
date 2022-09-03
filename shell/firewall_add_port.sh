#!/bin/bash

firewalld_port_add() {
  local ports=("${hdfs_ports[@]}" "${yarn_ports[@]}" "${spark_ports[@]}" "${hbase_ports[@]}" "${hive_ports[@]}" "${zookeeper_ports[@]}" "${mysql_ports[@]}" "${other_ports[@]}")
  if [ $(whoami) == root ]; then
    for port in "${ports[@]}"; do
      local port_status=$(firewall-cmd --list-port | grep $port | wc -l)
      if [ $port_status -eq 1 ]; then
        echo -e "端口号:$port\t已添加"
      else
        local result_add=$(firewall-cmd --add-port="${port}"/tcp --permanent --zone=public)
        echo -e "端口号:$port\t添加成功"
      fi
    done
    local firewalld_status_refresh=$(firewall-cmd --reload)
    echo -e "防火墙规则刷新: $firewalld_status_refresh\n现开启的防火墙端口号如下:"
    firewall-cmd --list-port
  else
    echo "权限不足, 请切换root用户再试一次"
  fi
}

firewalld_state() {
  local firewalld_status=$(systemctl status firewalld | grep -i "running" | wc -l)
  if [ $firewalld_status -eq 1 ]; then
    echo "防火墙处于开启状态, 开始执行!!!"
    firewalld_port_add
  else
    echo "防火墙未开启, 请开启防火墙后再试"

  fi
}

# 端口号  # 不用的可以选择注释
hdfs_ports=(50010 50075 50475 50020 50070 50470 8020 8485 8480 8019)
yarn_ports=(8032 8031 8088 8040 8042 8041 10020 19888)
spark_ports=(8081 7077 8080 4040 4041)
hbase_ports=(60000 60020 60030)
hive_ports=(9083 10000)
zookeeper_ports=(2181 2888 3888)
mysql_ports=(3306)
# 其他端口号, 多个端口号用空格隔开
other_ports=()
# 判断防火墙是否开启, 脚本初始化
firewalld_state
