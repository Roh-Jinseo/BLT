<template>
  <div ref="chart" style="width: 100%; height: 400px;"></div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'BarChart',
  props: {
    chartData: {
      type: Object,
      required: true
    },
    chartOptions: {
      type: Object,
      default: () => ({})
    }
  },
  mounted() {
    this.initChart()
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$refs.chart)
      this.updateChart()
    },
    updateChart() {
      const option = {
        xAxis: {
          type: 'category',
          data: this.chartData.labels,
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: '기본 금리',
            type: 'bar',
            data: this.chartData.baseRates,
            itemStyle: {
              color: '#42A5F5'
            }
          },
          {
            name: '최고 우대 금리',
            type: 'bar',
            data: this.chartData.preferredRates,
            itemStyle: {
              color: '#66BB6A'
            }
          }
        ],
        ...this.chartOptions
      }
      this.chart.setOption(option)
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler() {
        this.updateChart()
      }
    }
  }
}
</script>

<style scoped>
.chart {
  width: 100%;
  height: 400px;
}
</style>
