<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props:{
    date: Array,
    sma_predict : Array,
    sma_true : Array
  },
  methods: {
  },

  async mounted() {
    this.renderChart(
      {
        labels: this.date,
        datasets: [
          {
            label: "SMA_predict",
            data: this.sma_predict,
            backgroundColor: "#63dbff",
            borderColor: "#63dbff",
            borderWidth: 3,
            fill: false,
            pointRadius : 0,
          },
          {
            label: "SMA_true",
            data: this.sma_true,
            backgroundColor: "transparent",
            borderColor: "#ffa8c4",
            pointBackgroundColor: "#ffa8c4",
            fill: false,
            pointRadius : 0,
          },
        ],
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          position: "bottom",
          align: "start",
          
          labels:{
            fontColor: "rgba(77, 79, 92, 0.5)",
            boxWidth : 30
          }
        },
        scales: {
          
          xAxes: [
            {
              
              gridLines: {
                display: false,
              },
              ticks: {
                fontColor: "#7C828A",
                 padding : 25,
              },
            },
          ],
          yAxes: [
            {
              gridLines: {
                display: true,
                color: "rgba(77, 79, 92, 0.1)",
                drawBorder : false
              },
              ticks: {
                padding : 25,
                fontColor: "#7C828A",
                maxTicksLimit : 6
              },
            },
          ],
        },
      }
    );
  },
};
</script>
