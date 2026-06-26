"""
telegram/views.py
--------------------------------------------------
A.D.A.M Telegram UI

Generates every Telegram page.

No callbacks.
No keyboards.
No database queries.
"""

from services.dashboard_services import DashboardService

DIVIDER = "━━━━━━━━━━━━━━━━━━━━"


# ==================================================
# HOME
# ==================================================

def home_view(user_name="Operator"):

    stats = DashboardService.get_stats()
    health = DashboardService.system_health()

    return (

        "🛡️ <b>A.D.A.M SECURITY CONSOLE</b>\n"
        "<i>Autonomous Directive and Arbitration Machine</i>\n\n"

        f"{DIVIDER}\n\n"

        f"{health}\n\n"

        "🧠 <b>AI Engine</b>\n"
        "READY\n\n"

        f"📡 <b>Connected Devices</b>\n"
        f"{stats['devices']}\n\n"

        f"🚨 <b>Total Alerts</b>\n"
        f"{stats['alerts']}\n\n"

        f"📨 <b>Pending Commands</b>\n"
        f"{stats['pending']}\n\n"

        f"{DIVIDER}\n\n"

        f"👋 Welcome back, <b>{user_name}</b>\n\n"

        "Awaiting your command."
    )


# ==================================================
# DASHBOARD
# ==================================================

def dashboard_view():

    stats = DashboardService.get_stats()

    last = stats["last_event"]

    if last:

        last_text = (
            f"{last['event_type']}\n"
            f"{last['device_id']}\n"
            f"{last['created_at']}"
        )

    else:

        last_text = "No recent activity"

    return (

        "📊 <b>LIVE SYSTEM METRICS</b>\n\n"

        f"{DIVIDER}\n\n"

        "🟢 <b>Core Status</b>\n"
        "ONLINE\n\n"

        "🧠 <b>AI Engine</b>\n"
        "READY\n\n"

        f"📡 <b>Devices</b>\n"
        f"{stats['devices']}\n\n"

        f"📈 <b>Total Events</b>\n"
        f"{stats['events']}\n\n"

        f"🚨 <b>Total Alerts</b>\n"
        f"{stats['alerts']}\n\n"

        f"📨 <b>Pending Queue</b>\n"
        f"{stats['pending']}\n\n"

        "🕒 <b>Last Activity</b>\n"
        f"{last_text}\n\n"

        f"{DIVIDER}\n\n"

        "🟢 System Operational"
    )


# ==================================================
# EVENT LOG
# ==================================================

def event_log_view():

    events = DashboardService.get_recent_events()

    text = "📜 <b>EVENT LOG</b>\n\n"

    text += DIVIDER + "\n\n"

    if not events:

        text += "No events recorded."

        return text

    for event in events:

        text += (

            f"📍 {event['device_id']}\n"

            f"⚡ {event['event_type']}\n"

            f"🕒 {event['created_at']}\n\n"

        )

    return text


# ==================================================
# DEVICES
# ==================================================

def devices_view():

    devices = DashboardService.get_devices()

    text = "📡 <b>CONNECTED DEVICES</b>\n\n"

    text += DIVIDER + "\n\n"

    if not devices:

        text += "No devices connected."

        return text

    for device in devices:

        text += (

            f"🟢 <b>{device['device_id']}</b>\n"

            f"Last Seen\n"

            f"{device['last_seen']}\n\n"

            f"Events\n"

            f"{device['total_events']}\n\n"

        )

    return text


# ==================================================
# INTELLIGENCE
# ==================================================

def intelligence_view():

    return (

        "🧠 <b>AI ENGINE</b>\n\n"

        f"{DIVIDER}\n\n"

        "Detection Model\n"
        "Rule Engine V1\n\n"

        "Decision Engine\n"
        "ACTIVE\n\n"

        "Confidence Threshold\n"
        "90%\n\n"

        "Status\n"
        "READY"
    )


# ==================================================
# SETTINGS
# ==================================================

def settings_view():

    return (

        "⚙️ <b>SETTINGS</b>\n\n"

        f"{DIVIDER}\n\n"

        "Telegram\n"
        "Connected\n\n"

        "Backend\n"
        "Online\n\n"

        "Version\n"
        "1.0 MVP"
    )


# ==================================================
# ABOUT
# ==================================================

def about_view():

    return (

        "🛡️ <b>ABOUT A.D.A.M</b>\n\n"

        f"{DIVIDER}\n\n"

        "Autonomous Directive and Arbitration Machine\n\n"

        "AI-assisted IoT Security Platform\n\n"

        "Real-time monitoring\n"

        "Threat detection\n"

        "Remote response\n\n"

        f"{DIVIDER}\n\n"

        "Version\n"

        "1.0 MVP\n\n"

        "Developer\n"

        "Ð R ƛ K E N 他"
    )
