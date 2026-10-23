import json
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_math():
    with open(r"c:\Users\duydo\OneDrive\Tài liệu\idk\data\tiktok_studio_metrics.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Loaded tiktok_studio_metrics.json successfully.")
    
    # 1. Check overview metrics
    parsed = data["analytics_overview"]["parsed"]
    views_raw = 7700
    likes = int(parsed["likes"])
    profile_views = int(parsed["profile_views"])
    shares = int(parsed["shares"])
    
    like_rate = likes / views_raw * 100
    profile_rate = profile_views / views_raw * 100
    share_rate = shares / views_raw * 100
    
    print(f"Likes: {likes}, Like rate: {like_rate:.4f}% (Report: 1.79%)")
    print(f"Profile views: {profile_views}, Profile rate: {profile_rate:.4f}% (Report: 0.44%)")
    print(f"Shares: {shares}, Share rate: {share_rate:.4f}% (Report: 0.078%)")
    
    # 2. Check 7 recent videos data
    recent = data["recent_videos"]
    print(f"Total recent videos in JSON: {len(recent)}")
    for idx, v in enumerate(recent):
        print(f"#{idx+1}: {v['title'][:40]}... | Duration: {v['duration']} | Views: {v['views']} | Likes: {v['likes']} | Comments: {v['comments']}")
        
    # Check drop-offs
    # Nang dau thuc tinh: Part 1 = 89, Part 2 = 85, Part 3 = 39
    p1_nd, p2_nd, p3_nd = 89, 85, 39
    drop_nd_12 = (p1_nd - p2_nd) / p1_nd * 100
    drop_nd_23 = (p2_nd - p3_nd) / p2_nd * 100
    drop_nd_13 = (p1_nd - p3_nd) / p1_nd * 100
    print(f"Nang Dau Drop 1->2: {drop_nd_12:.2f}% (Report: 4.49%)")
    print(f"Nang Dau Drop 2->3: {drop_nd_23:.2f}% (Report: 54.12%)")
    print(f"Nang Dau Drop 1->3: {drop_nd_13:.2f}% (Report: 56.18%)")
    
    # Mat The: Part 1 = 72, Part 2 = 67, Part 3 = 66
    p1_mt, p2_mt, p3_mt = 72, 67, 66
    drop_mt_12 = (p1_mt - p2_mt) / p1_mt * 100
    drop_mt_23 = (p2_mt - p3_mt) / p2_mt * 100
    drop_mt_13 = (p1_mt - p3_mt) / p1_mt * 100
    print(f"Mat The Drop 1->2: {drop_mt_12:.2f}% (Report: 6.94%)")
    print(f"Mat The Drop 2->3: {drop_mt_23:.2f}% (Report: 1.49%)")
    print(f"Mat The Drop 1->3: {drop_mt_13:.2f}% (Report: 8.33%)")
    
    # Average drops
    avg_drop_12 = (drop_nd_12 + drop_mt_12) / 2
    avg_drop_23 = (drop_nd_23 + drop_mt_23) / 2
    avg_drop_13 = (drop_nd_13 + drop_mt_13) / 2
    print(f"Avg Drop 1->2: {avg_drop_12:.2f}% (Report: 5.72%)")
    print(f"Avg Drop 2->3: {avg_drop_23:.2f}% (Report: 27.81%)")
    print(f"Avg Drop 1->3: {avg_drop_13:.2f}% (Report: 32.26%)")

    # Demographics
    # 18-24: 49.8%, 25-34: 41.6% -> sum = 91.4%
    print(f"Demographics 18-34: {49.8 + 41.6:.1f}% (Report: 91.4%)")
    
    # Check total watch time calculation
    # Video #7: 89 views, 5.5s avg -> 489.5s = 8.1583 min
    print(f"Video 7 total watch time: 89 * 5.5 = {89 * 5.5}s = {89*5.5/60:.2f} min (Report: 8.16p)")

if __name__ == "__main__":
    test_math()
