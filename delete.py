RESULT = {
    "tabName": RES,
    "tabKey": "RES",
    "percentageType": ROW_CLICK,
    "pageType": RESULT_PAGE,
    'filterType': 'all',
    "mertrics": [
        VIEWS,
        REVENUE,
        CLICKS,
        CLICK_SENT
    ],
    "csv_columns": ["day", "tab", "clk", "score", "level", "vw"],


    "threshold_metrics": {
        AVERAGE_TQ: {
            "divide": None,
            "invert": 0,
            "weight": 3,
            "use": None,
            "flag_metric": CLICKS_WITH_TQ
        },
        # TQ: {
        #     "divide": CLICKS_WITH_TQ,
        #     "invert": 0,
        #     "weight": 3,
        #     "use": None,
        # },
        SPAM_CLICK: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 3,
            "use": None,
        },
        CLICK_WITH_ROBOTIC_ACTIVITY: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        FAST_CLICKS: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        NO_AD_FOCUS: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        ROBOTIC_ACTIVITY: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        BACKGROUND_WINDOW_CLICK: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        # AD_CLICK_POSITION: {
        #     "divide": CLICKS,
        #     "invert": 1,
        #     "weight": 0,
        #     "use": SPAM_CLICK,
        # },
        AD_OUTSIDE_WINDOW: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        PHANTOM: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        KNOWN_OFFENDERS: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        BLACKLISTED_IP: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        PUBLISHER_CLICK_BAD: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        SPOOFED_IDENTITY_CLICK: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        IP_SPOOFING: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        FAKE_BROWSER: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SPAM_CLICK,
        },
        MULTIPLE_CLICKS_2: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 2,
            "use": None,
        },
        BOT: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 2,
            "use": SPAM_CLICK,
        },
        SUSPECTED_SESSION_ACTIVITY: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 2,
            "use": None,
        },
        GREATER_THAN_5_CLICKS_PER_VIEW: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_SESSION_ACTIVITY,
        },
        MOUSE_OUT_VIEWPORT: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_SESSION_ACTIVITY,
        },
        HIGH_ACTIVITY: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_SESSION_ACTIVITY,
        },
        ONLY_CLICK_ACTIVITY: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_SESSION_ACTIVITY,
        },
        CACHED_BROWSER_FP: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_SESSION_ACTIVITY,
        },
        COOKIES_DISABLED: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_SESSION_ACTIVITY,
        },
        SUSPECTED_VISITOR_ACTIVITY: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 2,
            "use": None,
        },
        HIGH_FREQUECY_IP_CLICK: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_VISITOR_ACTIVITY,
        },
        CO_VISTATION_CLICK: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_VISITOR_ACTIVITY,
        },
        AFFILIATION_CLK_BAD: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_VISITOR_ACTIVITY,
        },
        CROWD_SOURCING_CLICK: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": SUSPECTED_VISITOR_ACTIVITY,
        },

        CLICK_PAID: {
            "divide": CLICK_SENT,
            "invert": 0,
            "weight": 3,
            "use": None,
        },
        CLICK_SENT: {
            "divide": CLICKS,
            "invert": 0,
            "weight": 3,
            "use": None,
        },
        AD_CLICKS_INVALID: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": None
        },
        AD_CLICKS_SUSPECTED: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 0,
            "use": None
        }
    },
    "additional_threshold_metrics": {
        CLICKS: {
            "divide": None,
            "invert": 0,
            "weight": 0,
            "use": None,
            "outlier": "iqr"
        },
        VIEWS: {
            "divide": None,
            "invert": 0,
            "weight": 0,
            "use": None,
            "outlier": "iqr"
        },
        REVENUE: {
            "divide": None,
            "invert": 0,
            "weight": 0,
            "use": None,
            "outlier": "iqr"
        },
        PAID_REF_CLICKS: {
            "divide": CLICKS,
            "invert": 0,
            "weight": 0,
            "use": None
        },
        AFFILIATION_CLK_GOOD: {
            "divide": CLICKS,
            "invert": 0,
            "weight": 1,
            "use": SUSPECTED_VISITOR_ACTIVITY,
        },
        TRF_NULL_RATE: {
            "divide": CLICKS,
            "invert": 1,
            "weight": 1,
            "use": None
        },
        AVERAGE_REVENUE_PER_CLICK: {
            "divide": None,
            "invert": 0,
            "weight": 1,
            "use": None
        },
        MAX_SPAM_PERCENTAGE: {
            "divide": None,
            "invert": 1,
            "weight": 1,
            "use": None
        },
        L2R: {
            "divide": None,
            "invert": 0,
            "weight": 0,
            "use": None,
            "outlier": "iqr"
        },
        R2A: {
            "divide": None,
            "invert": 0,
            "weight": 0,
            "use": None,
            "outlier": "iqr"
        },
        RPC: {
            "divide": None,
            "invert": 0,
            "weight": 0,
            "use": None,
            "outlier": "iqr"
        },
        STABILITY_SCORE: {
            "divide": None,
            "invert": 0,
            "weight": 0,
            "use": None
        }

    },
    "threshold_filter": {
        "metric": CLICKS,
        "value": 100,
    },
    "threshold_volume": VIEWS,

    "threshold": [
        { 'key': SPAM_CLICK },
        { 'key': CLICK_WITH_ROBOTIC_ACTIVITY },
        { 'key': FAST_CLICKS },
        { 'key': NO_AD_FOCUS },
        { 'key': ROBOTIC_ACTIVITY },
        { 'key': BACKGROUND_WINDOW_CLICK },
        # { 'key': AD_CLICK_POSITION },
        { 'key': AD_OUTSIDE_WINDOW },
        { 'key': PHANTOM },
        { 'key': KNOWN_OFFENDERS },
        { 'key': BLACKLISTED_IP },
        { 'key': PUBLISHER_CLICK_BAD },
        { 'key': SPOOFED_IDENTITY_CLICK },
        { 'key': IP_SPOOFING }, #
        { 'key': FAKE_BROWSER }, #
        { 'key': MULTIPLE_CLICKS_2 },
        { 'key': BOT },
        { 'key': SUSPECTED_SESSION_ACTIVITY },
        { 'key': GREATER_THAN_5_CLICKS_PER_VIEW },
        { 'key': MOUSE_OUT_VIEWPORT }, #
        { 'key': HIGH_ACTIVITY }, #
        { 'key': ONLY_CLICK_ACTIVITY },
        { 'key': CACHED_BROWSER_FP }, #
        { 'key': COOKIES_DISABLED },
        { 'key': SUSPECTED_VISITOR_ACTIVITY },
        { 'key': HIGH_FREQUECY_IP_CLICK  },
        { 'key': CO_VISTATION_CLICK },
        { 'key': AFFILIATION_CLK_BAD  },
        { 'key': CROWD_SOURCING_CLICK  },
        { 'key': CLICK_PAID  },
        { 'key': CLICK_SENT  },
    ],
    "sort": VIEWS,
}