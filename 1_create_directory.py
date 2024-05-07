import subprocess
import os

def create_directory(directory_name):
    """
    지정된 이름으로 디렉토리를 생성합니다.
    
    Args:
    directory_name (str): 생성할 디렉토리의 이름.
    """
    try:
        # 디렉토리 생성
        os.mkdir(directory_name)
        print(f"디렉토리 '{directory_name}' 생성 성공.")
    except FileExistsError:
        print(f"디렉토리 '{directory_name}'는 이미 존재합니다.")
    except Exception as e:
        print(f"디렉토리 생성 실패: {e}")


def git_clone(repo_url, directory=None):
    """
    Git repository를 클론합니다.
    
    Args:
    repo_url (str): 클론할 Git 리포지토리의 URL.
    directory (str, optional): 리포지토리를 클론할 디렉토리. 기본값은 None으로, 현재 디렉토리에 클론합니다.
    """
    command = ['git', 'clone', repo_url]
    if directory:
        command.append(directory)
    
    try:
        # subprocess.run을 사용하여 명령어 실행
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Git clone 성공:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Git clone 실패:", e.stderr)

# 사용 예시
create_directory("starcoder2_3b")

git_clone("https://github.com/Asimofe/starcoder2.git", "starcoder2_3b")

