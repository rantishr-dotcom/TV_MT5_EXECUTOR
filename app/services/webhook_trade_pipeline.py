class WebhookTradePipeline:

    def process(self, signal):

        return {
            "status": "pipeline_received",
            "symbol": getattr(signal, "symbol", None),
            "side": getattr(signal, "side", None)
        }\n