import speedtest
st = speedtest.Speedtest()
while True:
    choice = int(input('''Choose an option:
    1) Download Speed
    2) Upload Speed
    3) Ping
    Your Choice: '''))
    if choice == 1:
        print(f"Download Speed: {st.download() / 1_000_000:.2f} Mbps")
    elif choice == 2:
        print(f"Upload Speed: {st.upload() / 1_000_000:.2f} Mbps")
    elif choice == 3:
        st.get_best_server()
        print(f"Ping: {st.results.ping} ms")
    else:
        print("Invalid choice!")
