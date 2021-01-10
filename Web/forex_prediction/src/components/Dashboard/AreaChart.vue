<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      EURUSD: null,
      GBPUSD: null,
      USDJPY: null,
    };
  },
  mounted() {
    this.EURUSD = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);
    this.GBPUSD = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);
    this.USDJPY = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);

    this.EURUSD.addColorStop(0,"rgb(85,216,254,1)");
    this.EURUSD.addColorStop(0.5, "rgb(85,216,254,0.25)");
    this.EURUSD.addColorStop(1, "rgb(85,216,254,0.05)");

    this.GBPUSD.addColorStop(0, "rgb(163,160,251,0.1)");
    this.GBPUSD.addColorStop(0.5, "rgb(163,160,251,0.25)");
    this.GBPUSD.addColorStop(1, "rgb(163,160,251,0.05)");

    this.USDJPY.addColorStop(0, "rgba(255, 167, 196, 1)");
    this.USDJPY.addColorStop(0.5, "rgba(255, 167, 196, 0.25)");
    this.USDJPY.addColorStop(1, "rgba(255, 167, 196, 0.05)");

    this.renderChart(
      {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "EURUSD",
            borderColor: "#55D8FB",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "#55D8FB",
            backgroundColor: this.EURUSD,
            data: [40, 39, 10, 40, 39, 80, 40],
          },
          {
            label: "GBPUSD",
            borderColor: "#A3A0FB",
            pointBackgroundColor: "white",
            pointBorderColor: "#A3A0FB",
            borderWidth: 1,
            backgroundColor: this.GBPUSD,
            data: [60, 55, 32, 10, 2, 12, 53],
          },
          {
            label: "USDJPY",
            borderColor: "#FFA7C4",
            pointBackgroundColor: "white",
            pointBorderColor: "#FFA7C4",
            borderWidth: 1,
            backgroundColor: this.gradient2,
            data: [65, 52, 30, 7, 6, 6, 40],
          }
        ],
      },
      { responsive: true, maintainAspectRatio: false }
    );
  },
};
</script>
