<template>
  <div class="record">
    <div id="myChart" :style="{width: '800px', height: '500px'}">

    </div>
    <el-row display="margin-top:10px">
      <el-input id="original_name" placeholder="请输入原始标识" value="172.30.4.21:9008"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input id="show_name" placeholder="请输入要展示的名称" value="支付中心"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="modifyRecord()" style="float:left; margin: 2px;">新增或修改</el-button>
    </el-row>
    <el-row>
      <el-table :data="recordList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template scope="scope"> {{ scope.row.pk }} </template>
        </el-table-column>
        <el-table-column prop="name" label="原始标识" min-width="100">
          <template scope="scope"> {{ scope.row.fields.original_name }} </template>
        </el-table-column>
        <el-table-column prop="name" label="展示名称" min-width="100">
          <template scope="scope"> {{ scope.row.fields.show_name }} </template>
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
      modifyRecord() {
        var service_rec = {
          'original_name': document.getElementById("original_name").value,
          'show_name': document.getElementById("show_name").value,
        };
        this.axios.post('http://127.0.0.1:8000/api/modify_mapper', service_rec)
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
        this.axios.get('http://127.0.0.1:8000/api/show_mapper')
          .then((response) => {
            var res = response.data
            if (res.error_code == 0) {
              this.recordList = res['list']
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
