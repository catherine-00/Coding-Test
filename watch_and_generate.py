import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

WATCH_DIR = r"c:\Users\Admin\Desktop\Github\Coding-Test"  # 로컬에 클론한 Coding-Test 경로
TARGET_FILENAMES = {"README.md"}
EXTENSIONS = {".py", ".sql"}  # 정답 코드 확장자

class GitRepoWatcher(FileSystemEventHandler):
    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

    def process(self, event):
        if event.is_directory:
            return

        filename = os.path.basename(event.src_path)
        dirname = os.path.dirname(event.src_path)

        if filename in TARGET_FILENAMES or os.path.splitext(filename)[1] in EXTENSIONS:
            time.sleep(1.5)  # 파일 쓰기 완료 대기

            files = os.listdir(dirname)
            readme = next((f for f in files if f == "README.md"), None)
            code = next((f for f in files if os.path.splitext(f)[1] in EXTENSIONS), None)

            if readme and code:
                readme_path = os.path.join(dirname, readme)
                code_path = os.path.join(dirname, code)
                output_path = os.path.join(dirname, "output.html")

                print(f"\n📄 감지됨: {readme_path} + {code_path}")
                print("🚀 blogpost.py 실행 중...")

                try:
                    subprocess.run(["python", "blogpost.py", readme_path, code_path, output_path], check=True)
                    print("✅ output.html 생성 완료!\n")
                except subprocess.CalledProcessError as e:
                    print("❌ blogpost.py 실행 실패:", e)

if __name__ == "__main__":
    event_handler = GitRepoWatcher()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=True)
    observer.start()

    print(f"👀 '{WATCH_DIR}' 감시 중... (Ctrl+C로 종료)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
