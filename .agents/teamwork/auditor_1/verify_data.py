import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== FORENSIC DATA RECALCULATION & AUDIT ===")
    
    with open('data/tiktok_studio_metrics.json', 'r', encoding='utf-8') as f:
        metrics = json.load(f)

    with open('data/published_audio_registry.json', 'r', encoding='utf-8') as f:
        registry = json.load(f)

    print("\n[1] RAW METRICS VERIFICATION:")
    print("Timestamp:", metrics.get('timestamp'))
    print("Total posts badge:", metrics.get('total_posts_badge'))
    
    videos = metrics.get('recent_videos', [])
    print(f"Total recent videos in JSON: {len(videos)}")
    
    for i, v in enumerate(videos, 1):
        print(f"  #{i}: [{v.get('duration')}] Views: {v.get('views')}, Likes: {v.get('likes')}, Cmts: {v.get('comments')}, Date: {v.get('date')}")
        print(f"       Title: {v.get('title')[:60]}...")

    overview = metrics.get('analytics_overview', {})
    parsed = overview.get('parsed', {})
    print("\n[2] PARSED OVERVIEW:")
    for k, v in parsed.items():
        print(f"  {k}: {v}")

    raw_text = overview.get('raw_text_excerpt', '')
    print("\n[3] RAW TEXT EXCERPT VERIFICATION:")
    # Check traffic percentages
    for line in raw_text.split('\n'):
        if any(term in line for term in ['Đề xuất', 'Tìm kiếm', 'Hồ sơ cá nhân', 'Đã follow', 'Âm thanh', '7,7K', '138', '34', '6']):
            print("  Excerpt line:", line.strip())

    viewers_text = overview.get('viewers_text', '')
    print("\n[4] VIEWERS DEMOGRAPHICS TEXT:")
    for line in viewers_text.split('\n'):
        if any(term in line for term in ['Nữ', 'Nam', '18-24', '25-34', '709', '697', 'VTV']):
            print("  Demographics line:", line.strip())

    followers_text = overview.get('followers_text', '')
    print("\n[5] FOLLOWERS DEMOGRAPHICS TEXT:")
    for line in followers_text.split('\n'):
        if any(term in line for term in ['2.5K', '-4', 'Nam', 'Nữ', '18-24', '25-34']):
            print("  Follower line:", line.strip())

    print("\n[6] DROP-OFF RATE CALCULATIONS:")
    # Nang dau thuc tinh:
    # P1: index 6 (89 views), P2: index 5 (85 views), P3: index 4 (39 views)
    p1_ndtt = videos[6]['views']
    p2_ndtt = videos[5]['views']
    p3_ndtt = videos[4]['views']
    drop_p1_p2_ndtt = (p1_ndtt - p2_ndtt) / p1_ndtt * 100
    drop_p2_p3_ndtt = (p2_ndtt - p3_ndtt) / p2_ndtt * 100
    total_drop_ndtt = (p1_ndtt - p3_ndtt) / p1_ndtt * 100
    print(f"Nang Dau Thuc Tinh: P1={p1_ndtt}, P2={p2_ndtt}, P3={p3_ndtt}")
    print(f"  Drop P1 -> P2: {drop_p1_p2_ndtt:.2f}% (Expect ~4.49%)")
    print(f"  Drop P2 -> P3: {drop_p2_p3_ndtt:.2f}% (Expect ~54.12%)")
    print(f"  Total Drop P1 -> P3: {total_drop_ndtt:.2f}% (Expect ~56.18%)")

    # Mat the ky bang ha:
    # P1: index 3 (72 views), P2: index 2 (67 views), P3: index 1 (66 views)
    p1_mt = videos[3]['views']
    p2_mt = videos[2]['views']
    p3_mt = videos[1]['views']
    drop_p1_p2_mt = (p1_mt - p2_mt) / p1_mt * 100
    drop_p2_p3_mt = (p2_mt - p3_mt) / p2_mt * 100
    total_drop_mt = (p1_mt - p3_mt) / p1_mt * 100
    print(f"Mat The Ky Bang Ha: P1={p1_mt}, P2={p2_mt}, P3={p3_mt}")
    print(f"  Drop P1 -> P2: {drop_p1_p2_mt:.2f}% (Expect ~6.94%)")
    print(f"  Drop P2 -> P3: {drop_p2_p3_mt:.2f}% (Expect ~1.49%)")
    print(f"  Total Drop P1 -> P3: {total_drop_mt:.2f}% (Expect ~8.33%)")

    print("\n[7] REGISTRY VERIFICATION:")
    print("Total registered:", registry.get('total_registered'))
    print("Published titles count:", len(registry.get('published_titles', [])))
    print("Published history count:", len(registry.get('published_history', [])))
    print("Published episodes count:", len(registry.get('published_episodes', [])))

    print("\n[8] SUBAGENT REPORTS AUDIT:")
    import glob
    reports = glob.glob('.agents/teamwork/subagent_*/report.md')
    reports.sort()
    print(f"Total subagent report.md files found: {len(reports)}")
    for r in reports:
        with open(r, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.splitlines()
        first_line = lines[0] if lines else "EMPTY"
        print(f"  {r}: {len(lines)} lines | {len(content):,} bytes | {first_line[:60]}")

    print("\n[9] SUBAGENT 10 & MASTER DELIVERABLE AUDIT:")
    handoff_10 = '.agents/teamwork/subagent_10_master_strategist/handoff.md'
    with open(handoff_10, 'r', encoding='utf-8') as f:
        h10 = f.read()
    print(f"  Subagent 10 handoff: {len(h10.splitlines())} lines | {len(h10):,} bytes")

    master_path = 'docs/BAO_CAO_PHAN_TICH_TIKTOK_RETENTION_10_AGENTS.md'
    with open(master_path, 'r', encoding='utf-8') as f:
        master = f.read()
    m_lines = master.splitlines()
    print(f"  Master Deliverable: {len(m_lines)} lines | {len(master):,} bytes")
    print(f"  Title: {m_lines[0] if m_lines else 'EMPTY'}")

if __name__ == '__main__':
    main()
