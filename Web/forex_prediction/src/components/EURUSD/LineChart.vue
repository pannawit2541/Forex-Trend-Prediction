<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {};
  },
  mounted() {
    this.renderChart(
      {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [
          {
            label: "SMA_predict",
            data: [2, 10, 5, 9, 0, 6],
            backgroundColor: "transparent",
            borderColor: "#63dbff",
            pointBackgroundColor: "#63dbff",
            lineTension: 0.4,
          },
          {
            label: "SMA_true",
            data: [4, 12, 3, 7, 1, 5],
            backgroundColor: "transparent",
            borderColor: "#ffa8c4",
            pointBackgroundColor: "#ffa8c4",
            lineTension: 0.4,
            spanGaps: true,
          },
        ],
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          position: "bottom",
          align: "start",
        },
      }
    );
  },
};
</script>