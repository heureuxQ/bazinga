<template>
  <div class="record">
    <div id="myChart" :style="{width: '800px', height: '500px'}">

    </div>
    <el-row display="margin-top:10px">
      <el-input id="system_name" placeholder="请输入系统标识" value="gu-bei"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="service_name" placeholder="请输入服务标识" value="clotho"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="service_interface" placeholder="请输入服务接口标识" value="/ex/check"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="total_num" placeholder="请输入调用总数" value="10"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="slow_num" placeholder="请输入慢调用数" value="1"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="slow_proportion" placeholder="请输入慢调用占比" value="0.1"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="fail_num" placeholder="请输入异常调用数" value="1"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="fail_proportion" placeholder="请输入异常调用占比" value="0.1"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="avg_delay_sec" placeholder="请输入平均耗时" value="6.2"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="longest_delay_sec" placeholder="请输入最长耗时" value="60"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="shortest_delay_sec" placeholder="请输入最短耗时" value="0.1"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="start_time" placeholder="请输入统计开始时间" value="2018-12-27 17:00:00"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="end_time" placeholder="请输入统计结束时间" value="2018-12-27 18:00:00"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="addRecord()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
      <el-table :data="recordList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template scope="scope"> {{ scope.row.pk }} </template>
        </el-table-column>
        <el-table-column prop="name" label="系统" min-width="100">
          <template scope="scope"> {{ scope.row.fields.system_name }} </template>
        </el-table-column>
        <el-table-column prop="created_at" label="添加时间" min-width="100">
          <template scope="scope"> {{ scope.row.fields.created_at }} </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'record', data() {
      return {
        input: '', recordList: [], lineXAxisList: [],
      }
    }, mounted: function () {
      this.showRecords()
    }, methods: {
      addRecord() {
        var service_rec = {
          'system_name': document.getElementById("system_name").value,
          'service_name': document.getElementById("service_name").value,
          'service_interface': document.getElementById("service_interface").value,
          'total_num': document.getElementById("total_num").value,
          'slow_num': document.getElementById("slow_num").value,
          'slow_proportion': document.getElementById("slow_proportion").value,
          'fail_num': document.getElementById("fail_num").value,
          'fail_proportion': document.getElementById("fail_proportion").value,
          'avg_delay_sec': document.getElementById("avg_delay_sec").value,
          'longest_delay_sec': document.getElementById("longest_delay_sec").value,
          'shortest_delay_sec': document.getElementById("shortest_delay_sec").value,
          'shortest_delay_sec': document.getElementById("shortest_delay_sec").value,
          'start_time': document.getElementById("start_time").value,
          'end_time': document.getElementById("end_time").value,
        };
        this.axios.post('http://127.0.0.1:8000/api/add_record', service_rec)
          .then((response) => {
            var res = response.data
            if (res.error_code == 0) {
              this.showRecords()
            } else {
              this.$message.error('新增记录失败，请重试')
              console.log(res['msg'])
            }
          })
      },
      showRecords() {
        this.axios.get('http://127.0.0.1:8000/api/show_record')
          .then((response) => {
            var res = response.data
            if (res.error_code == 0) {
              this.recordList = res['list']
              this.recordList.forEach((item, index) => {
                console.log(item.fields.service_name)
              })
              let myChart = this.$echarts.init(document.getElementById('myChart'))
              myChart.setOption({
                title: {
                  text: ''
                },
                tooltip: {},
                legend: {
                  data:['销量', '设计']
                },
                xAxis: {
                  data: ['2018-01-01', '2018-09-01', '2018-09-09']
                },
                yAxis: {},
                series: [{
                  name: '销量',
                  type: 'bar',
                  data: [10, 11, 9]
                },
                  {
                    name: '设计',
                    type: 'bar',
                    data: [30, 20, 25]
                  }]
              });
            } else {
              this.$message.error('查询记录失败')
              console.log(res['msg'])
            }
          })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
