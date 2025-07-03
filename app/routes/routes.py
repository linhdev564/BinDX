from flask import render_template, request, jsonify, send_file
from TikTokApi import TikTokApi
import io

def init_routes(app):
    @app.route('/')
    def home():
        return render_template('download_page.html')
    
    @app.route('/api/download', methods=['POST'])
    async def api_download():
        data = request.get_json()
        tiktok_url = data.get('tiktok_url')
        if not tiktok_url:
            return jsonify({'error': 'No TikTok URL provided'}), 400
        try:
            async with TikTokApi() as api:
                await api.create_sessions()
                video = await api.video(url=tiktok_url)
                video_bytes = await video.bytes()
            #trả về file video cho client 
            return send_file(
                io.BytesIO(video_bytes),
                mimetype="video/mp4",
                as_attachment=True,
                download_name="tiktok_video.mp4"
            )
            # Nếu bạn muốn trả về thông báo thành công và kích thước video
            # return jsonify({'message': "tải thành công!", 'size': len(video_bytes)}), 200
        except Exception as e:
            # Debugging line to log the error
            print(f"Error downloading video: {str(e)}")
            import traceback; traceback.print_exc()
            return jsonify({'message': f'Lỗi: {str(e)}'}), 500