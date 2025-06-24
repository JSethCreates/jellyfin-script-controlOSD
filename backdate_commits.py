import os
import shutil
import subprocess

# List of historical HTML versions with backdated timestamps and messages
commit_data = [
    ("sethsUI2.0.2.html", "2024-10-19T02:47:00", "Initial"),
    ("sethsUI2.1.2sound.html", "2024-10-19T03:34:00", "Highlights"),
    ("sethsUI3.0.1nav cleaner.html", "2024-10-19T04:01:00", "Navigation tracking"),
    ("sethsUI - MASTER.html", "2024-10-21T16:39:00", "SPA Nav Tracking"),
    ("sethsUI25back.html", "2024-12-02T13:18:00", "Selectors"),
    ("sethsUI25BUUUU.html", "2024-12-04T11:47:00", "Adjustments"),
    ("sethsUI4.0.1.html", "2024-12-07T15:22:00", "Selector adjustments"),
    ("SethsUI4.1.html", "2024-12-10T10:50:00", "MD3 Colors"),
    ("sethsUI2 - Copy.html", "2024-12-13T17:25:00", "RGB depreciated"),
    ("sethsUI419.html", "2024-12-16T03:03:00", "iframe highlighting"),
    ("sethsUI422.html", "2024-12-19T15:27:00", "iframe adjustments"),
    ("SethsUI501.html", "2024-12-22T01:18:00", "Color consolidation"),
    ("sethsUI521.html", "2024-12-27T08:41:00", "Focus adjustments"),
    ("sethsUI540.html", "2024-12-30T06:08:00", "Style changes"),
    ("sethsUI601.html", "2025-01-03T21:32:00", "OSD changes"),
    ("sethsUI611.html", "2025-01-05T22:45:00", "Selector adjustments"),
    ("sethsUI612.html", "2025-01-07T23:07:00", "OSD Pause button tracking"),
    ("sethsUI620.html", "2025-01-10T01:01:00", "OSD Slider adjust"),
    ("sethsUI621.html", "2025-01-12T03:04:00", "SPA Nav Tracking"),
    ("sethsUI640.html", "2025-01-14T07:19:00", "OSD tracking"),
    ("sethsUI642.html", "2025-01-17T19:39:00", "OSD Extras vs simple mode"),
    ("sethsUI643.html", "2025-01-20T23:38:00", "OSD Extras plot"),
    ("sethsUI650.html", "2025-01-23T00:50:00", "OSD Extras sliders"),
    ("sethsUI651.html", "2025-01-26T05:20:00", "OSD Extras pause"),
    ("sethsUI652.html", "2025-01-29T07:02:00", "iframe adjustments"),
    ("sethsUI653.html", "2025-02-01T22:18:00", "OSD Extras fonts"),
    ("sethsUI655.html", "2025-02-04T04:49:00", "Font import adjustments"),
    ("sethsUI661.html", "2025-02-07T10:44:00", "Adjustments"),
    ("SethsUI662.html", "2025-02-10T21:36:00", "Code formatting"),
    ("SethsUI663.html", "2025-02-13T01:07:00", "Debugging function"),
    ("SethsUI664.html", "2025-02-17T06:23:00", "Nav adjustments"),
    ("sethsUI665.html", "2025-02-21T07:19:00", "Threshold detection"),
    ("sethsUI667.html", "2025-02-25T07:19:00", "Adjustments"),
    ("SethsUI681.html", "2025-03-01T23:38:00", "Iframe handling"),
    ("SethsUI682.html", "2025-03-04T00:28:00", "OSD auth"),
    ("SethsUI684.html", "2025-03-07T03:15:00", "Code formatting"),
    ("SethsUI690.html", "2025-03-11T15:25:00", "Import MD3 styles"),
    ("SethsUI693x.html", "2025-03-14T15:25:00", "Adjustments"),
    ("SethsUI694.html", "2025-03-18T00:50:00", "Import MD3 styles"),
    ("SethsUI695.html", "2025-03-23T03:29:00", "Style injection font changes"),
    ("SethsUI696.html", "2025-03-28T04:06:00", "OSD icons"),
    ("SethsUI697.html", "2025-04-03T07:24:00", "OSD icon text"),
    ("SethsUI700.html", "2025-06-12T22:26:00", "Color unification"),
    ("SethsUI701.html", "2025-06-17T00:03:00", "OSD icons")
]

# Initial documentation commit date
initial_date = "2024-10-18T18:00:00"

# Initial commit
subprocess.run(["git", "add", "README.md", "LICENSE", ".gitignore", ".gitattributes"])
env = os.environ.copy()
env["GIT_COMMITTER_DATE"] = initial_date
env["GIT_AUTHOR_DATE"] = initial_date
subprocess.run(["git", "commit", "-m", "Initial commit with documentation and metadata"], env=env)

# Apply historical commits
for filename, dt, msg in commit_data:
    if os.path.exists("spotlight.html"):
        os.remove("spotlight.html")
    shutil.copyfile(filename, "spotlight.html")
    subprocess.run(["git", "add", "spotlight.html"])
    env["GIT_COMMITTER_DATE"] = dt
    env["GIT_AUTHOR_DATE"] = dt
    subprocess.run(["git", "commit", "-m", msg], env=env)

print("Backdate commits complete.")
