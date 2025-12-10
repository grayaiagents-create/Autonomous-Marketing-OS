import requests
import json

ACCESS_TOKEN = "EAAVxBOdQXBYBQLwJ0qzr6Pj6jwR3mCFGDMO2Hsz7vq8VIt1t54ZBwfNv9aj7NSZAWxXRYLZAKATBhVWKqAZA0KYlmGDiDdlbzvEt27rerBkFLPr3XEqeQXyByzmocmeZBsuPo19UrpFVawxwnbhyZBcnFCqDBZCZBDtZCTU4DwldxQFbK0x7BGIvByI5ykrt1Km7YbCSxZAZAfZBlnau2rOha5G89NsSdvHmZARX1oR48UTnLCwsRYuBkYAF8R0ZAzLg4YcBDtAm8HM5213JWpbFM1p6vOZBd0L1ACSx2oEHZCkoaQZDZD"

def test_political_ads():
    """Test Ads Library with required parameters for political ads"""
    
    print("Testing Meta Ads Library for POLITICAL ADS...")
    print("=" * 60)
    
    # URL for v19.0 (use v20.0 if this doesn't work)
    url = "https://graph.facebook.com/v19.0/ads_archive"
    
    # REQUIRED parameters for political ads
    params = {
        'access_token': ACCESS_TOKEN,
        'search_terms': 'vote election',  # Political terms work
        'ad_reached_countries': '["US", "IN"]',  # JSON string format
        'ad_active_status': 'ALL',
        'fields': 'id,ad_creation_time,ad_creative_body,page_name,ad_delivery_start_time,ad_delivery_stop_time',
        'limit': 5,
        'ad_type': 'POLITICAL_AND_ISSUE_ADS'  # CRITICAL: Only this works without full access
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            total_count = data.get('summary', {}).get('total_count', 0)
            ads_found = len(data.get('data', []))
            
            print(f"\n✅ SUCCESS! Found {total_count} total ads, showing {ads_found}")
            
            if data.get('data'):
                print("\n📊 Sample Ads Found:")
                for i, ad in enumerate(data['data'], 1):
                    print(f"\nAd {i}:")
                    print(f"  Page: {ad.get('page_name', 'Unknown')}")
                    print(f"  Created: {ad.get('ad_creation_time', 'N/A')}")
                    if ad.get('ad_creative_body'):
                        print(f"  Text: {ad.get('ad_creative_body', '')[:80]}...")
            else:
                print("\n⚠️  No ads returned. Try different search terms:")
                print("   - 'climate change'")
                print("   - 'healthcare'")
                print("   - 'education'")
                print("   - 'voting rights'")
                
        else:
            error_data = response.json()
            error_msg = error_data.get('error', {}).get('message', 'Unknown')
            error_code = error_data.get('error', {}).get('code', 'Unknown')
            
            print(f"\n❌ Error {error_code}: {error_msg}")
            
            if error_code == 10:
                print("\n🔧 Required Actions:")
                print("1. Your app needs Business Verification")
                print("2. Go to: https://business.facebook.com/settings")
                print("3. Complete 'Business Verification'")
                print("4. Submit for 'ads_read' permission review")
                print("\n📝 Note: Until then, you can ONLY access political/issue ads")
                
    except Exception as e:
        print(f"\n❌ Exception: {e}")

def test_with_specific_political_terms():
    """Test with various political terms that should work"""
    
    print("\n" + "=" * 60)
    print("Testing Different Political Search Terms")
    print("=" * 60)
    
    url = "https://graph.facebook.com/v19.0/ads_archive"
    
    political_terms = [
        "vote",
        "election",
        "climate change",
        "healthcare",
        "education reform",
        "voting rights",
        "gun control",
        "abortion",
        "immigration"
    ]
    
    for term in political_terms:
        params = {
            'access_token': ACCESS_TOKEN,
            'search_terms': term,
            'ad_reached_countries': '["US"]',
            'ad_active_status': 'ALL',
            'limit': 2,
            'ad_type': 'POLITICAL_AND_ISSUE_ADS'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                count = len(data.get('data', []))
                print(f"✅ '{term}': Found {count} ads")
                if count > 0:
                    print(f"   Example: {data['data'][0].get('page_name', 'Unknown')}")
            else:
                print(f"❌ '{term}': Error {response.status_code}")
        except:
            print(f"❌ '{term}': Failed")

def get_app_info():
    """Get detailed app information"""
    
    print("\n" + "=" * 60)
    print("App Information & Next Steps")
    print("=" * 60)
    
    # Get app details
    url = f"https://graph.facebook.com/v19.0/831271746382587"  # Your App ID
    params = {'access_token': ACCESS_TOKEN, 'fields': 'name,category'}
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            app_data = response.json()
            print(f"App Name: {app_data.get('name')}")
            print(f"Category: {app_data.get('category')}")
    except:
        pass
    
    print("\n📋 To Get Commercial Ads Access:")
    print("1. Go to: https://developers.facebook.com/apps/831271746382587/dashboard/")
    print("2. Navigate to: App Review → Permissions and Features")
    print("3. Find 'ads_read' and click 'Request Advanced Access'")
    print("4. Complete Business Verification (if prompted)")
    print("5. Submit required documents for review")
    print("\n⏱️  This process can take 2-7 days")

if __name__ == "__main__":
    test_political_ads()
    test_with_specific_political_terms()
    get_app_info()