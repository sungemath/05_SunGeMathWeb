import googleapiclient.discovery
import json

# --- 這裡請填入你的資訊 ---
API_KEY = "AIzaSyAGTvplgLQiWwkX2Jb1a8NO6C1yNOCD-6k"
CHANNEL_ID = "UCdsQqTM1of410-OlBgqQ8ag" 
# -----------------------

def get_channel_videos(api_key, channel_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    
    videos = []
    next_page_token = None
    
    print("開始連線 YouTube 抓取資料，請稍候...")
    
    while True:
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token,
            type="video"
        )
        response = request.execute()
        
        for item in response['items']:
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            # 只抓取標題含有 atx_ 的影片 (不分大小寫)
            if "武陵高中" in title.lower():
                videos.append({
                    "title": title,
                    "url": f"https://www.youtube.com/watch?v={video_id}",
                    "id": video_id
                })
        
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
            
    return videos

if __name__ == "__main__":
    video_data = get_channel_videos(API_KEY, CHANNEL_ID)
    with open("videos.json", "w", encoding="utf-8") as f:
        json.dump(video_data, f, ensure_ascii=False, indent=4)
    print(f"✅ 完成！共抓取到 {len(video_data)} 部題目影片，已存入 videos.json")