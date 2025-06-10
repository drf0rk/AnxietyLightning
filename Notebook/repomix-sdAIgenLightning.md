This file is a merged representation of the entire codebase, combined into a single document by Repomix.
The content has been processed where line numbers have been added, security check has been disabled.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Line numbers have been added to the beginning of each line
- Security check has been disabled - content may contain sensitive information
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
__configs__/
  A1111/
    config.json
    ui-config.json
  Classic/
    config.json
    ui-config.json
  ComfyUI/
    Comfy-Manager/
      config.ini
    workflows/
      anxety-workflow.json
    comfy.settings.json
    install-deps.py
  Forge/
    config.json
    ui-config.json
  ReForge/
    config.json
    ui-config.json
  SD-UX/
    config.json
    ui-config.json
  gradio-tunneling.py
  styles.csv
  user.css
.Docs/
  SVG/
    en/
      colab-en.svg
      discord-en.svg
      kaggle-en.svg
    ru/
      colab-ru.svg
      discord-ru.svg
      kaggle-ru.svg
    Boosty_Logo_Color.svg
    DA_Logo_Color.svg
CSS/
  auto-cleaner.css
  download-result.css
  main-widgets.css
JS/
  main-widgets.js
modules/
  __season.py
  CivitaiAPI.py
  json_utils.py
  Manager.py
  TunnelHub.py
  webui_utils.py
  widget_factory.py
Notebook/
  LightningAnxiety.ipynb
scripts/
  en/
    downloading-en.py
    widgets-en.py
  ru/
    downloading-ru.py
    widgets-ru.py
  UIs/
    A1111.py
    Classic.py
    ComfyUI.py
    Forge.py
    ReForge.py
    SD-UX.py
  _loras-data.py
  _models-data.py
  _xl-models-data.py
  auto-cleaner.py
  cleaner_gui.py
  download-result.py
  launch.py
  setup.py
LICENSE
lightning_installer_complete.py
README-ru-RU.md
Readme.md
README.md
```

# Files

## File: __configs__/A1111/config.json
```json
  1: {
  2:     "sd_vae": "None",
  3:     "CLIP_stop_at_last_layers": 2,
  4:     "ad_max_models": 6,
  5:     "control_net_unit_count": 6,
  6:     "quicksettings_list": [
  7:         "sd_model_checkpoint",
  8:         "sd_vae",
  9:         "CLIP_stop_at_last_layers"
 10:     ],
 11:     "ui_tab_order": [
 12:         "txt2img",
 13:         "img2img",
 14:         "Image Info",
 15:         "SuperMerger",
 16:         "HUB",
 17:         "Infinite image browsing",
 18:         "CivitAI Browser+",
 19:         "Tagger",
 20:         "Settings",
 21:         "Extensions"
 22:     ],
 23:     "ui_reorder_list": [
 24:         "override_settings",
 25:         "inpaint",
 26:         "sampler",
 27:         "dimensions",
 28:         "cfg",
 29:         "seed",
 30:         "checkboxes",
 31:         "hires_fix",
 32:         "extra_options",
 33:         "batch",
 34:         "scripts"
 35:     ],
 36:     "hide_samplers": [
 37:         "UniPC",
 38:         "PLMS",
 39:         "LMS"
 40:     ],
 41:     "hidden_tabs": [
 42:         "Extras",
 43:         "PNG Info",
 44:         "Train",
 45:         "Checkpoint Merger"
 46:     ],
 47:     "extra_networks_default_multiplier": 0.7,
 48:     "samples_filename_pattern": "M=[model_name]_S=[seed]_D=[date]",
 49:     "grid_extended_filename": true,
 50:     "grid_text_active_color": "#ffffff",
 51:     "grid_background_color": "#0b0b0b",
 52:     "show_progress_grid": true,
 53:     "show_progress_every_n_steps": 2,
 54:     "live_previews_image_format": "webp",
 55:     "live_preview_content": "Prompt",
 56:     "live_preview_refresh_period": 100.0,
 57:     "live_preview_fast_interrupt": true,
 58:     "extra_networks_card_width": 200.0,
 59:     "extra_networks_card_height": 300.0,
 60:     "extra_networks_card_text_scale": 0.8,
 61:     "state_txt2img": [
 62:         "prompt",
 63:         "negative_prompt",
 64:         "styles",
 65:         "sampling",
 66:         "scheduler",
 67:         "sampling_steps",
 68:         "width",
 69:         "height",
 70:         "batch_count",
 71:         "batch_size",
 72:         "cfg_scale",
 73:         "seed"
 74:     ],
 75:     "state_img2img": [
 76:         "prompt",
 77:         "negative_prompt",
 78:         "styles",
 79:         "sampling",
 80:         "scheduler",
 81:         "sampling_steps",
 82:         "width",
 83:         "height",
 84:         "batch_count",
 85:         "batch_size",
 86:         "cfg_scale",
 87:         "denoising_strength",
 88:         "seed"
 89:     ],
 90:     "state_extensions": [
 91:         "control-net",
 92:         "adetailer"
 93:     ],
 94:     "state_ui": [
 95:         "Reset Button",
 96:         "Import Button",
 97:         "Export Button"
 98:     ],
 99:     "tac_maxResults": 12.0,
100:     "tac_showWikiLinks": true,
101:     "custom_api_key": "65b66176dcf284b266579de57fbdc024",
102:     "aria2_flags": "--header=\"User-Agent: Mozilla/5.0\" --allow-overwrite=true --console-log-level=error --stderr=true -c -x16 -s16 -k1M -j5",
103:     "unpack_zip": true
104: }
```

## File: __configs__/A1111/ui-config.json
```json
 1: {
 2:     "txt2img/Styles/value": [
 3:         "ANXETY V2"
 4:     ],
 5:     "customscript/sampler.py/txt2img/Sampling method/value": "Euler a",
 6:     "customscript/sampler.py/txt2img/Schedule type/value": "Karras",
 7:     "customscript/sampler.py/txt2img/Sampling steps/value": 28,
 8:     "txt2img/CFG Scale/value": 5.0,
 9:     "txt2img/Upscaler/value": "None",
10:     "txt2img/Denoising strength/value": 0.45,
11:     "txt2img/Control Mode/value": "My prompt is more important",
12:     "img2img/Styles/value": [
13:         "ANXETY V2"
14:     ],
15:     "customscript/sampler.py/img2img/Sampling method/value": "Euler a",
16:     "customscript/sampler.py/img2img/Schedule type/value": "Karras",
17:     "customscript/sampler.py/img2img/Sampling steps/value": 40,
18:     "img2img/Inpaint area/value": "Only masked",
19:     "img2img/Denoising strength/value": 0.4,
20:     "img2img/Control Mode/value": "My prompt is more important",
21:     "customscript/xyz_grid.py/txt2img/Include Sub Images/value": true,
22:     "customscript/prompt_matrix.py/txt2img/Grid margins (px)/value": 8,
23:     "customscript/xyz_grid.py/txt2img/Grid margins (px)/value": 8,
24:     "civitai_interface/NSFW content/value": true,
25:     "civitai_interface/Tile count:/value": 28,
26:     "customscript/wildcard_recursive.py/txt2img/Enable UmiAI/value": false
27: }
```

## File: __configs__/Classic/config.json
```json
  1: {
  2:     "show_scheduler": true,
  3:     "sd_checkpoint_dropdown_use_short": true,
  4:     "hires_fix_show_sampler": true,
  5:     "sd_vae": "None",
  6:     "CLIP_stop_at_last_layers": 2,
  7:     "ad_max_models": 6,
  8:     "control_net_unit_count": 6,
  9:     "quicksettings_list": [
 10:         "sd_model_checkpoint",
 11:         "sd_vae",
 12:         "CLIP_stop_at_last_layers"
 13:     ],
 14:     "ui_tab_order": [
 15:         "txt2img",
 16:         "img2img",
 17:         "Image Info",
 18:         "HUB",
 19:         "Infinite image browsing",
 20:         "CivitAI Browser+",
 21:         "Settings",
 22:         "Extensions"
 23:     ],
 24:     "ui_reorder_list": [
 25:         "override_settings",
 26:         "inpaint",
 27:         "sampler",
 28:         "dimensions",
 29:         "cfg",
 30:         "seed",
 31:         "checkboxes",
 32:         "hires_fix",
 33:         "extra_options",
 34:         "batch",
 35:         "scripts"
 36:     ],
 37:     "hide_samplers": [
 38:         "UniPC",
 39:         "PLMS",
 40:         "LMS"
 41:     ],
 42:     "hidden_tabs": [
 43:         "Extras",
 44:         "PNG Info",
 45:         "Train"
 46:     ],
 47:     "extra_networks_default_multiplier": 0.7,
 48:     "samples_filename_pattern": "M=[model_name]_S=[seed]_D=[date]",
 49:     "grid_extended_filename": true,
 50:     "grid_text_active_color": "#ffffff",
 51:     "grid_background_color": "#0b0b0b",
 52:     "show_progress_grid": true,
 53:     "show_progress_every_n_steps": 2,
 54:     "live_previews_image_format": "webp",
 55:     "live_preview_content": "Prompt",
 56:     "live_preview_refresh_period": 100.0,
 57:     "live_preview_fast_interrupt": true,
 58:     "extra_networks_card_width": 200.0,
 59:     "extra_networks_card_height": 300.0,
 60:     "extra_networks_card_text_scale": 0.8,
 61:     "state_txt2img": [
 62:         "prompt",
 63:         "negative_prompt",
 64:         "styles",
 65:         "sampling",
 66:         "scheduler",
 67:         "sampling_steps",
 68:         "width",
 69:         "height",
 70:         "batch_count",
 71:         "batch_size",
 72:         "cfg_scale",
 73:         "seed"
 74:     ],
 75:     "state_img2img": [
 76:         "prompt",
 77:         "negative_prompt",
 78:         "styles",
 79:         "sampling",
 80:         "scheduler",
 81:         "sampling_steps",
 82:         "width",
 83:         "height",
 84:         "batch_count",
 85:         "batch_size",
 86:         "cfg_scale",
 87:         "denoising_strength",
 88:         "seed"
 89:     ],
 90:     "state_extensions": [
 91:         "control-net",
 92:         "adetailer"
 93:     ],
 94:     "state_ui": [
 95:         "Reset Button",
 96:         "Import Button",
 97:         "Export Button"
 98:     ],
 99:     "tac_maxResults": 12.0,
100:     "tac_showWikiLinks": true,
101:     "custom_api_key": "65b66176dcf284b266579de57fbdc024",
102:     "aria2_flags": "--header=\"User-Agent: Mozilla/5.0\" --allow-overwrite=true --console-log-level=error --stderr=true -c -x16 -s16 -k1M -j5",
103:     "unpack_zip": true
104: }
```

## File: __configs__/Classic/ui-config.json
```json
 1: {
 2:     "txt2img/Styles/value": [
 3:         "ANXETY V2"
 4:     ],
 5:     "customscript/sampler.py/txt2img/Sampling Method/value": "Euler a",
 6:     "customscript/sampler.py/txt2img/Schedule Type/value": "Karras",
 7:     "customscript/sampler.py/txt2img/Sampling Steps/value": 28,
 8:     "txt2img/CFG Scale/value": 5.0,
 9:     "txt2img/Upscaler/value": "None",
10:     "txt2img/Denoising strength/value": 0.45,
11:     "txt2img/Control Mode/value": "My prompt is more important",
12:     "img2img/Styles/value": [
13:         "ANXETY V2"
14:     ],
15:     "customscript/sampler.py/img2img/Sampling Method/value": "Euler a",
16:     "customscript/sampler.py/img2img/Schedule Type/value": "Karras",
17:     "customscript/sampler.py/img2img/Sampling Steps/value": 40,
18:     "img2img/Inpaint area/value": "Only masked",
19:     "img2img/Denoising strength/value": 0.4,
20:     "img2img/Control Mode/value": "My prompt is more important",
21:     "customscript/xyz_grid.py/txt2img/Include Sub Images/value": true,
22:     "customscript/prompt_matrix.py/txt2img/Grid margins (px)/value": 8,
23:     "customscript/xyz_grid.py/txt2img/Grid margins (px)/value": 8,
24:     "civitai_interface/NSFW content/value": true,
25:     "civitai_interface/Tile count:/value": 28,
26:     "customscript/wildcard_recursive.py/txt2img/Enable UmiAI/value": false
27: }
```

## File: __configs__/ComfyUI/Comfy-Manager/config.ini
```
1: [default]
2: preview_method = latent2rgb
3: share_option = none
```

## File: __configs__/ComfyUI/workflows/anxety-workflow.json
```json
  1: {
  2:   "last_node_id": 19,
  3:   "last_link_id": 25,
  4:   "nodes": [
  5:     {
  6:       "id": 7,
  7:       "type": "CLIPTextEncode",
  8:       "pos": [
  9:         570,
 10:         300
 11:       ],
 12:       "size": [
 13:         420,
 14:         170
 15:       ],
 16:       "flags": {
 17:         "collapsed": false
 18:       },
 19:       "order": 6,
 20:       "mode": 0,
 21:       "inputs": [
 22:         {
 23:           "name": "clip",
 24:           "type": "CLIP",
 25:           "link": 15
 26:         }
 27:       ],
 28:       "outputs": [
 29:         {
 30:           "name": "CONDITIONING",
 31:           "type": "CONDITIONING",
 32:           "links": [
 33:             6
 34:           ],
 35:           "slot_index": 0
 36:         }
 37:       ],
 38:       "title": "Negative Prompt",
 39:       "properties": {
 40:         "Node name for S&R": "CLIPTextEncode"
 41:       },
 42:       "widgets_values": [
 43:         "lowres, (worst quality, low quality:1.2), bad anatomy, bad hands, 4koma, comic, greyscale, censored, jpeg artifacts, overly saturated, overly vivid"
 44:       ]
 45:     },
 46:     {
 47:       "id": 13,
 48:       "type": "CLIPSetLastLayer",
 49:       "pos": [
 50:         240,
 51:         230
 52:       ],
 53:       "size": [
 54:         315,
 55:         58
 56:       ],
 57:       "flags": {},
 58:       "order": 3,
 59:       "mode": 0,
 60:       "inputs": [
 61:         {
 62:           "name": "clip",
 63:           "type": "CLIP",
 64:           "link": 13,
 65:           "label": "CLIP"
 66:         }
 67:       ],
 68:       "outputs": [
 69:         {
 70:           "name": "CLIP",
 71:           "type": "CLIP",
 72:           "links": [
 73:             14,
 74:             15
 75:           ],
 76:           "slot_index": 0,
 77:           "label": "CLIP"
 78:         }
 79:       ],
 80:       "properties": {
 81:         "Node name for S&R": "CLIPSetLastLayer"
 82:       },
 83:       "widgets_values": [
 84:         -2
 85:       ]
 86:     },
 87:     {
 88:       "id": 12,
 89:       "type": "EmptyLatentImage",
 90:       "pos": [
 91:         -90,
 92:         240
 93:       ],
 94:       "size": [
 95:         315,
 96:         106
 97:       ],
 98:       "flags": {},
 99:       "order": 0,
100:       "mode": 0,
101:       "inputs": [],
102:       "outputs": [
103:         {
104:           "name": "LATENT",
105:           "type": "LATENT",
106:           "links": [
107:             11
108:           ],
109:           "slot_index": 0,
110:           "label": "Latent"
111:         }
112:       ],
113:       "properties": {
114:         "Node name for S&R": "EmptyLatentImage"
115:       },
116:       "widgets_values": [
117:         1024,
118:         1536,
119:         1
120:       ]
121:     },
122:     {
123:       "id": 19,
124:       "type": "Reroute",
125:       "pos": [
126:         240,
127:         30
128:       ],
129:       "size": [
130:         75,
131:         26
132:       ],
133:       "flags": {},
134:       "order": 4,
135:       "mode": 0,
136:       "inputs": [
137:         {
138:           "name": "",
139:           "type": "*",
140:           "link": 24
141:         }
142:       ],
143:       "outputs": [
144:         {
145:           "name": "VAE",
146:           "type": "VAE",
147:           "links": [
148:             25
149:           ],
150:           "slot_index": 0
151:         }
152:       ],
153:       "properties": {
154:         "showOutputText": true,
155:         "horizontal": false
156:       }
157:     },
158:     {
159:       "id": 4,
160:       "type": "CheckpointLoaderSimple",
161:       "pos": [
162:         -90,
163:         100
164:       ],
165:       "size": [
166:         315,
167:         98
168:       ],
169:       "flags": {},
170:       "order": 1,
171:       "mode": 0,
172:       "inputs": [],
173:       "outputs": [
174:         {
175:           "name": "MODEL",
176:           "type": "MODEL",
177:           "links": [
178:             16
179:           ],
180:           "slot_index": 0
181:         },
182:         {
183:           "name": "CLIP",
184:           "type": "CLIP",
185:           "links": [
186:             13
187:           ],
188:           "slot_index": 1
189:         },
190:         {
191:           "name": "VAE",
192:           "type": "VAE",
193:           "links": [
194:             24
195:           ],
196:           "slot_index": 2
197:         }
198:       ],
199:       "properties": {
200:         "Node name for S&R": "CheckpointLoaderSimple"
201:       },
202:       "widgets_values": [
203:         "WAI-illustrious_V14.safetensors"
204:       ]
205:     },
206:     {
207:       "id": 15,
208:       "type": "ModelSamplingDiscrete",
209:       "pos": [
210:         240,
211:         100
212:       ],
213:       "size": [
214:         315,
215:         82
216:       ],
217:       "flags": {},
218:       "order": 2,
219:       "mode": 4,
220:       "inputs": [
221:         {
222:           "name": "model",
223:           "type": "MODEL",
224:           "link": 16
225:         }
226:       ],
227:       "outputs": [
228:         {
229:           "name": "MODEL",
230:           "type": "MODEL",
231:           "links": [
232:             17
233:           ],
234:           "slot_index": 0
235:         }
236:       ],
237:       "properties": {
238:         "Node name for S&R": "ModelSamplingDiscrete"
239:       },
240:       "widgets_values": [
241:         "eps",
242:         false
243:       ]
244:     },
245:     {
246:       "id": 6,
247:       "type": "CLIPTextEncode",
248:       "pos": [
249:         570,
250:         100
251:       ],
252:       "size": [
253:         420,
254:         160
255:       ],
256:       "flags": {},
257:       "order": 5,
258:       "mode": 0,
259:       "inputs": [
260:         {
261:           "name": "clip",
262:           "type": "CLIP",
263:           "link": 14
264:         }
265:       ],
266:       "outputs": [
267:         {
268:           "name": "CONDITIONING",
269:           "type": "CONDITIONING",
270:           "links": [
271:             4
272:           ],
273:           "slot_index": 0
274:         }
275:       ],
276:       "title": "Prompt",
277:       "properties": {
278:         "Node name for S&R": "CLIPTextEncode"
279:       },
280:       "widgets_values": [
281:         ""
282:       ]
283:     },
284:     {
285:       "id": 3,
286:       "type": "KSampler",
287:       "pos": [
288:         1000,
289:         100
290:       ],
291:       "size": [
292:         315,
293:         474
294:       ],
295:       "flags": {},
296:       "order": 7,
297:       "mode": 0,
298:       "inputs": [
299:         {
300:           "name": "model",
301:           "type": "MODEL",
302:           "link": 17
303:         },
304:         {
305:           "name": "positive",
306:           "type": "CONDITIONING",
307:           "link": 4
308:         },
309:         {
310:           "name": "negative",
311:           "type": "CONDITIONING",
312:           "link": 6
313:         },
314:         {
315:           "name": "latent_image",
316:           "type": "LATENT",
317:           "link": 11
318:         }
319:       ],
320:       "outputs": [
321:         {
322:           "name": "LATENT",
323:           "type": "LATENT",
324:           "links": [
325:             7
326:           ],
327:           "slot_index": 0
328:         }
329:       ],
330:       "properties": {
331:         "Node name for S&R": "KSampler"
332:       },
333:       "widgets_values": [
334:         441812983543614,
335:         "randomize",
336:         28,
337:         5,
338:         "euler",
339:         "karras",
340:         1
341:       ]
342:     },
343:     {
344:       "id": 8,
345:       "type": "VAEDecode",
346:       "pos": [
347:         1000,
348:         10
349:       ],
350:       "size": [
351:         313.89434814453125,
352:         46
353:       ],
354:       "flags": {},
355:       "order": 8,
356:       "mode": 0,
357:       "inputs": [
358:         {
359:           "name": "samples",
360:           "type": "LATENT",
361:           "link": 7
362:         },
363:         {
364:           "name": "vae",
365:           "type": "VAE",
366:           "link": 25
367:         }
368:       ],
369:       "outputs": [
370:         {
371:           "name": "IMAGE",
372:           "type": "IMAGE",
373:           "links": [
374:             23
375:           ],
376:           "slot_index": 0
377:         }
378:       ],
379:       "properties": {
380:         "Node name for S&R": "VAEDecode"
381:       },
382:       "widgets_values": []
383:     },
384:     {
385:       "id": 17,
386:       "type": "PreviewImage",
387:       "pos": [
388:         1330,
389:         100
390:       ],
391:       "size": [
392:         370,
393:         470
394:       ],
395:       "flags": {},
396:       "order": 9,
397:       "mode": 0,
398:       "inputs": [
399:         {
400:           "name": "images",
401:           "type": "IMAGE",
402:           "link": 23
403:         }
404:       ],
405:       "outputs": [],
406:       "properties": {
407:         "Node name for S&R": "PreviewImage"
408:       },
409:       "widgets_values": []
410:     }
411:   ],
412:   "links": [
413:     [
414:       4,
415:       6,
416:       0,
417:       3,
418:       1,
419:       "CONDITIONING"
420:     ],
421:     [
422:       6,
423:       7,
424:       0,
425:       3,
426:       2,
427:       "CONDITIONING"
428:     ],
429:     [
430:       7,
431:       3,
432:       0,
433:       8,
434:       0,
435:       "LATENT"
436:     ],
437:     [
438:       11,
439:       12,
440:       0,
441:       3,
442:       3,
443:       "LATENT"
444:     ],
445:     [
446:       13,
447:       4,
448:       1,
449:       13,
450:       0,
451:       "CLIP"
452:     ],
453:     [
454:       14,
455:       13,
456:       0,
457:       6,
458:       0,
459:       "CLIP"
460:     ],
461:     [
462:       15,
463:       13,
464:       0,
465:       7,
466:       0,
467:       "CLIP"
468:     ],
469:     [
470:       16,
471:       4,
472:       0,
473:       15,
474:       0,
475:       "MODEL"
476:     ],
477:     [
478:       17,
479:       15,
480:       0,
481:       3,
482:       0,
483:       "MODEL"
484:     ],
485:     [
486:       23,
487:       8,
488:       0,
489:       17,
490:       0,
491:       "IMAGE"
492:     ],
493:     [
494:       24,
495:       4,
496:       2,
497:       19,
498:       0,
499:       "*"
500:     ],
501:     [
502:       25,
503:       19,
504:       0,
505:       8,
506:       1,
507:       "VAE"
508:     ]
509:   ],
510:   "groups": [],
511:   "config": {},
512:   "extra": {
513:     "ds": {
514:       "scale": 0.7513148009015777,
515:       "offset": [
516:         134.07084233168055,
517:         113.19968043448176
518:       ]
519:     },
520:     "node_versions": {
521:       "comfy-core": "0.3.12"
522:     }
523:   },
524:   "version": 0.4
525: }
```

## File: __configs__/ComfyUI/comfy.settings.json
```json
 1: {
 2:     "Comfy.DevMode": true,
 3:     "Comfy.TutorialCompleted": true,
 4:     "Comfy.Locale": "en",
 5:     "Comfy.Sidebar.Size": "small",
 6:     "Comfy.ColorPalette": "comfy-anxety",
 7:     "Comfy.Graph.LinkMarkers": 2,
 8:     "Comfy.NodeSuggestions.number": 15,
 9:     "Comfy.CustomColorPalettes": {
10:         "comfy-anxety": {
11:             "id": "comfy-anxety",
12:             "name": "Anxety-Theme",
13:             "colors": {
14:                 "node_slot": {
15:                     "CLIP": "#ffd919",
16:                     "CLIP_VISION": "#97c4c6",
17:                     "CLIP_VISION_OUTPUT": "#7b5fb2",
18:                     "CONDITIONING": "#ffbe4f",
19:                     "CONTROL_NET": "#6ee7b7",
20:                     "GUIDER": "#5cffff",
21:                     "IMAGE": "#6a7691",
22:                     "LATENT": "#ffa5f9",
23:                     "MASK": "#4ae07b",
24:                     "MODEL": "#b088ff",
25:                     "SAMPLER": "#ffb088",
26:                     "SIGMAS": "#4ae07b",
27:                     "STYLE_MODEL": "#7cdfff",
28:                     "TAESD": "#edf588",
29:                     "VAE": "#ff6666",
30:                     "NOISE": "#5a6785"
31:                 },
32:                 "litegraph_base": {
33:                     "BACKGROUND_IMAGE": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkAQMAAABKLAcXAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAZQTFRFIyMjAAAAELmbUwAAADlJREFUeJxjtD/wROa/I4R4yFjf8IODoQFCfGT8z4AAw5+H6vfRcIHxRsMFO280XLDzRsMFOw/F7wDxEwfkrrXhFwAAAABJRU5ErkJggg==",
34:                     "CLEAR_BACKGROUND_COLOR": "#000000",
35:                     "NODE_TITLE_COLOR": "#bbc2c6",
36:                     "NODE_SELECTED_TITLE_COLOR": "#ffd16c",
37:                     "NODE_TEXT_SIZE": 14,
38:                     "NODE_TEXT_COLOR": "#bbc2c6",
39:                     "NODE_TEXT_HIGHLIGHT_COLOR": "#d1d5d7",
40:                     "NODE_SUBTEXT_SIZE": 12,
41:                     "NODE_DEFAULT_COLOR": "#191919",
42:                     "NODE_DEFAULT_BGCOLOR": "#222222",
43:                     "NODE_DEFAULT_BOXCOLOR": "#89b4fa",
44:                     "NODE_DEFAULT_SHAPE": 2,
45:                     "NODE_BOX_OUTLINE_COLOR": "#e29fbe",
46:                     "NODE_BYPASS_BGCOLOR": "#db88ae",
47:                     "NODE_ERROR_COLOUR": "#ff6747",
48:                     "DEFAULT_SHADOW_COLOR": "rgba(0,0,0,0.35)",
49:                     "DEFAULT_GROUP_FONT": 20,
50:                     "WIDGET_BGCOLOR": "#131313",
51:                     "WIDGET_OUTLINE_COLOR": "#3d4142",
52:                     "WIDGET_TEXT_COLOR": "#d1d5d7",
53:                     "WIDGET_SECONDARY_TEXT_COLOR": "#bbc2c6",
54:                     "LINK_COLOR": "#75d8f7",
55:                     "EVENT_LINK_COLOR": "#ff85v2",
56:                     "CONNECTING_LINK_COLOR": "#45db76",
57:                     "BADGE_FG_COLOR": "#d3dce0",
58:                     "BADGE_BG_COLOR": "#22282a"
59:                 },
60:                 "comfy_base": {
61:                     "bg-color": "#181818",
62:                     "comfy-menu-bg": "#0b0b0b",
63:                     "comfy-menu-secondary-bg": "#0b0b0b",
64:                     "comfy-input-bg": "#131313",
65:                     "input-text": "#d1d5d7",
66:                     "descrip-text": "#d3dce0",
67:                     "drag-text": "#939a9c",
68:                     "error-text": "#ff6747",
69:                     "border-color": "#475254",
70:                     "tr-even-bg-color": "#131313",
71:                     "tr-odd-bg-color": "#181818",
72:                     "content-bg": "#db88ae",
73:                     "content-fg": "#f5f6f7",
74:                     "content-hover-bg": "#fab387",
75:                     "content-hover-fg": "#f0f0f0"
76:                 }
77:             }
78:         }
79:     },
80:     "pysssss.ImageFeed.Location": "hidden",
81:     "pysssss.ModelInfo.NsfwLevel": "PG",
82:     "ModelManager.APIKey.Civitai": "65b66176dcf284b266579de57fbdc024",
83:     "ModelManager.APIKey.HuggingFace": ""
84: }
```

## File: __configs__/ComfyUI/install-deps.py
```python
  1: """ install-deps.py | by ANXETY """
  2: 
  3: from importlib.metadata import distribution, PackageNotFoundError
  4: from pathlib import Path
  5: import subprocess
  6: import importlib
  7: import sys
  8: import re
  9: import os
 10: 
 11: def get_enabled_subdirectories(base_directory):
 12:     """Find active directories with dependencies"""
 13:     base_path = Path(base_directory)
 14:     subdirs = []
 15: 
 16:     for subdir in base_path.iterdir():
 17:         if subdir.is_dir() and not subdir.name.endswith('.disabled') and not subdir.name.startswith('.') and subdir.name != '__pycache__':
 18:             print(f"\033[1;34mChecking dependencies >> \033[0m{subdir.name}")
 19:             req_file = subdir / 'requirements.txt'
 20:             inst_script = subdir / 'install.py'
 21: 
 22:             if req_file.exists() or inst_script.exists():
 23:                 subdirs.append((subdir, req_file, inst_script))
 24: 
 25:     print()
 26:     return subdirs
 27: 
 28: def get_git_package_name(git_url):
 29:     """Extract package name from Git URL"""
 30:     clean_url = git_url.split('git+')[-1].rstrip('/')
 31: 
 32:     # Attempt to extract name from GitHub URL
 33:     if 'github.com' in clean_url:
 34:         match = re.search(r'github\.com/[^/]+/([^/]+)', clean_url)
 35:         if match:
 36:             return match.group(1).replace('.git', '')
 37: 
 38:     # General case for .git repositories
 39:     match = re.search(r'/([^/]+?)(\.git)?$', clean_url)
 40:     return match.group(1) if match else None
 41: 
 42: def is_git_installed(git_url):
 43:     """Check if Git package is installed by attempting import"""
 44:     pkg_name = get_git_package_name(git_url)
 45:     if not pkg_name:
 46:         return False
 47: 
 48:     variants = {
 49:         pkg_name,
 50:         pkg_name.lower(),
 51:         pkg_name.replace('-', '_'),
 52:         pkg_name.lower().replace('-', '_')
 53:     }
 54: 
 55:     for variant in variants:
 56:         try:
 57:             importlib.import_module(variant)
 58:             return True
 59:         except ImportError:
 60:             continue
 61:     return False
 62: 
 63: def check_package(package_spec):
 64:     """Check package installation with version verification"""
 65:     try:
 66:         if 'git+' in package_spec:
 67:             return is_git_installed(package_spec)
 68: 
 69:         match = re.match(r'^([^=><]+)([<>=!]+)(.+)$', package_spec)
 70:         if not match:
 71:             dist = distribution(package_spec.strip())
 72:             return True
 73: 
 74:         name, op, version = map(str.strip, match.groups())
 75:         installed = distribution(name).version
 76:         return compare_versions(installed, version, op)
 77: 
 78:     except (PackageNotFoundError, AttributeError):
 79:         return False
 80: 
 81: def compare_versions(v1, v2, operator):
 82:     """Universal version comparison"""
 83:     v1_parts = list(map(int, re.findall(r'\d+', v1)))
 84:     v2_parts = list(map(int, re.findall(r'\d+', v2)))
 85: 
 86:     for a, b in zip(v1_parts, v2_parts):
 87:         if a != b:
 88:             break
 89:     else:
 90:         a, b = len(v1_parts), len(v2_parts)
 91: 
 92:     if operator == '==': return a == b
 93:     if operator == '>=': return a >= b
 94:     if operator == '<=': return a <= b
 95:     if operator == '>': return a > b
 96:     if operator == '<': return a < b
 97:     return False
 98: 
 99: def install_package(package_spec):
100:     """Install a package"""
101:     print(f"\033[1;32mInstalling >> \033[0m{package_spec}")
102:     subprocess.run(
103:         [sys.executable, '-m', 'pip', 'install', '-q', package_spec],
104:         check=True,
105:         stdout=subprocess.DEVNULL,
106:         stderr=subprocess.DEVNULL
107:     )
108: 
109: def process_requirements(file_path, installed):
110:     """Process requirements file"""
111:     if not file_path.exists():
112:         return
113: 
114:     with open(file_path) as f:
115:         for line in f:
116:             line = line.strip()
117:             if not line or line.startswith('#') or line in installed:
118:                 continue
119: 
120:             if not check_package(line):
121:                 install_package(line)
122:                 installed.add(line)
123: 
124: def run_install_script(script_path, executed):
125:     """Execute installation script"""
126:     if script_path.exists() and str(script_path) not in executed:
127:         print(f"\033[1;33mRunning install script >> \033[0m{script_path}")
128:         subprocess.run(
129:             [sys.executable, str(script_path)],
130:             check=True,
131:             stdout=subprocess.DEVNULL,
132:             stderr=subprocess.DEVNULL
133:         )
134:         executed.add(str(script_path))
135: 
136: def save_state(installed, scripts, log_file):
137:     """Save installation state to log file"""
138:     with open(log_file, 'w') as f:
139:         f.write('\n'.join(installed))
140:         f.write('\n\n# Executed scripts:\n')
141:         f.write('\n'.join(scripts))
142: 
143: def load_previous_state(log_file):
144:     """Load previous installation state from log"""
145:     installed = set()
146:     scripts = set()
147: 
148:     if Path(log_file).exists():
149:         with open(log_file) as f:
150:             section = 0
151:             for line in f:
152:                 line = line.strip()
153:                 if not line: continue
154: 
155:                 if line.startswith('# Executed scripts:'):
156:                     section = 1
157:                     continue
158: 
159:                 if section == 0:
160:                     installed.add(line)
161:                 else:
162:                     scripts.add(line)
163: 
164:     return installed, scripts
165: 
166: def main():
167:     base_dir = 'custom_nodes'
168:     log_file = 'installed_packages.txt'
169: 
170:     installed, executed = load_previous_state(log_file)
171:     directories = get_enabled_subdirectories(base_dir)
172: 
173:     try:
174:         for _, req, script in directories:
175:             process_requirements(req, installed)
176:             run_install_script(script, executed)
177: 
178:         save_state(installed, executed, log_file)
179: 
180:     except KeyboardInterrupt:
181:         print("\n\033[1;31mInterrupted by user\033[0m")
182:     except Exception as e:
183:         print(f"\n\033[1;31mError: {e}\033[0m")
184: 
185: if __name__ == '__main__':
186:     main()
```

## File: __configs__/Forge/config.json
```json
  1: {
  2:     "sd_t2i_sampler": "Euler a",
  3:     "sd_t2i_scheduler": "Karras",
  4:     "sd_i2i_sampler": "Euler a",
  5:     "sd_i2i_scheduler": "Karras",
  6:     "sd_vae": "None",
  7:     "CLIP_stop_at_last_layers": 2,
  8:     "ad_max_models": 6,
  9:     "control_net_unit_count": 6,
 10:     "quicksettings_list": [
 11:         "sd_model_checkpoint",
 12:         "sd_vae",
 13:         "CLIP_stop_at_last_layers"
 14:     ],
 15:     "ui_tab_order": [
 16:         "Txt2img",
 17:         "Img2img",
 18:         "Image Info",
 19:         "SuperMerger",
 20:         "HUB",
 21:         "Infinite image browsing",
 22:         "CivitAI Browser+",
 23:         "Tagger",
 24:         "Settings",
 25:         "Extensions"
 26:     ],
 27:     "ui_reorder_list": [
 28:         "override_settings",
 29:         "inpaint",
 30:         "sampler",
 31:         "dimensions",
 32:         "cfg",
 33:         "seed",
 34:         "checkboxes",
 35:         "hires_fix",
 36:         "extra_options",
 37:         "batch",
 38:         "scripts"
 39:     ],
 40:     "hide_samplers": [
 41:         "UniPC",
 42:         "PLMS",
 43:         "LMS"
 44:     ],
 45:     "hidden_tabs": [
 46:         "Extras",
 47:         "PNG Info",
 48:         "Train",
 49:         "Checkpoint Merger",
 50:         "Spaces"
 51:     ],
 52:     "extra_networks_default_multiplier": 0.7,
 53:     "samples_filename_pattern": "M=[model_name]_S=[seed]_D=[date]",
 54:     "grid_extended_filename": true,
 55:     "grid_text_active_color": "#ffffff",
 56:     "grid_background_color": "#0b0b0b",
 57:     "show_progress_grid": true,
 58:     "show_progress_every_n_steps": 2,
 59:     "live_previews_image_format": "webp",
 60:     "live_preview_content": "Prompt",
 61:     "live_preview_refresh_period": 100.0,
 62:     "live_preview_fast_interrupt": true,
 63:     "extra_networks_card_width": 200.0,
 64:     "extra_networks_card_height": 300.0,
 65:     "extra_networks_card_text_scale": 0.8,
 66:     "state_txt2img": [
 67:         "prompt",
 68:         "negative_prompt",
 69:         "styles",
 70:         "sampling",
 71:         "scheduler",
 72:         "sampling_steps",
 73:         "width",
 74:         "height",
 75:         "batch_count",
 76:         "batch_size",
 77:         "cfg_scale",
 78:         "seed"
 79:     ],
 80:     "state_img2img": [
 81:         "prompt",
 82:         "negative_prompt",
 83:         "styles",
 84:         "sampling",
 85:         "scheduler",
 86:         "sampling_steps",
 87:         "width",
 88:         "height",
 89:         "batch_count",
 90:         "batch_size",
 91:         "cfg_scale",
 92:         "denoising_strength",
 93:         "seed"
 94:     ],
 95:     "state_extensions": [
 96:         "control-net",
 97:         "adetailer"
 98:     ],
 99:     "state_ui": [
100:         "Reset Button",
101:         "Import Button",
102:         "Export Button"
103:     ],
104:     "tac_maxResults": 12.0,
105:     "tac_showWikiLinks": true,
106:     "custom_api_key": "65b66176dcf284b266579de57fbdc024",
107:     "aria2_flags": "--header=\"User-Agent: Mozilla/5.0\" --allow-overwrite=true --console-log-level=error --stderr=true -c -x16 -s16 -k1M -j5",
108:     "unpack_zip": true
109: }
```

## File: __configs__/Forge/ui-config.json
```json
 1: {
 2:     "txt2img/Styles/value": [
 3:         "ANXETY V2"
 4:     ],
 5:     "customscript/sampler.py/txt2img/Sampling method/value": "Euler a",
 6:     "customscript/sampler.py/txt2img/Schedule type/value": "Karras",
 7:     "customscript/sampler.py/txt2img/Sampling steps/value": 28,
 8:     "txt2img/CFG Scale/value": 5.0,
 9:     "txt2img/Upscaler/value": "None",
10:     "txt2img/Denoising strength/value": 0.45,
11:     "txt2img/Control Mode/value": "My prompt is more important",
12:     "img2img/Styles/value": [
13:         "ANXETY V2"
14:     ],
15:     "customscript/sampler.py/img2img/Sampling method/value": "Euler a",
16:     "customscript/sampler.py/img2img/Schedule type/value": "Karras",
17:     "customscript/sampler.py/img2img/Sampling steps/value": 40,
18:     "img2img/Inpaint area/value": "Only masked",
19:     "img2img/Denoising strength/value": 0.4,
20:     "img2img/Control Mode/value": "My prompt is more important",
21:     "customscript/xyz_grid.py/txt2img/Include Sub Images/value": true,
22:     "customscript/prompt_matrix.py/txt2img/Grid margins (px)/value": 8,
23:     "customscript/xyz_grid.py/txt2img/Grid margins (px)/value": 8,
24:     "civitai_interface/NSFW content/value": true,
25:     "civitai_interface/Tile count:/value": 28,
26:     "customscript/wildcard_recursive.py/txt2img/Enable UmiAI/value": false
27: }
```

## File: __configs__/ReForge/config.json
```json
  1: {
  2:     "sd_vae": "None",
  3:     "CLIP_stop_at_last_layers": 2,
  4:     "ad_max_models": 6,
  5:     "control_net_unit_count": 6,
  6:     "quicksettings_list": [
  7:         "sd_model_checkpoint",
  8:         "sd_vae",
  9:         "CLIP_stop_at_last_layers"
 10:     ],
 11:     "ui_tab_order": [
 12:         "txt2img",
 13:         "img2img",
 14:         "Image Info",
 15:         "SuperMerger",
 16:         "HUB",
 17:         "Infinite image browsing",
 18:         "CivitAI Browser+",
 19:         "Tagger",
 20:         "Settings",
 21:         "Extensions"
 22:     ],
 23:     "ui_reorder_list": [
 24:         "override_settings",
 25:         "inpaint",
 26:         "sampler",
 27:         "dimensions",
 28:         "cfg",
 29:         "seed",
 30:         "checkboxes",
 31:         "hires_fix",
 32:         "extra_options",
 33:         "batch",
 34:         "scripts"
 35:     ],
 36:     "hide_samplers": [
 37:         "UniPC",
 38:         "PLMS",
 39:         "LMS"
 40:     ],
 41:     "hidden_tabs": [
 42:         "Extras",
 43:         "PNG Info",
 44:         "Train",
 45:         "Checkpoint Merger"
 46:     ],
 47:     "extra_networks_default_multiplier": 0.7,
 48:     "samples_filename_pattern": "M=[model_name]_S=[seed]_D=[date]",
 49:     "grid_extended_filename": true,
 50:     "grid_text_active_color": "#ffffff",
 51:     "grid_background_color": "#0b0b0b",
 52:     "show_progress_grid": true,
 53:     "show_progress_every_n_steps": 2,
 54:     "live_previews_image_format": "webp",
 55:     "live_preview_content": "Prompt",
 56:     "live_preview_refresh_period": 100.0,
 57:     "live_preview_fast_interrupt": true,
 58:     "extra_networks_card_width": 200.0,
 59:     "extra_networks_card_height": 300.0,
 60:     "extra_networks_card_text_scale": 0.8,
 61:     "state_txt2img": [
 62:         "prompt",
 63:         "negative_prompt",
 64:         "styles",
 65:         "sampling",
 66:         "scheduler",
 67:         "sampling_steps",
 68:         "width",
 69:         "height",
 70:         "batch_count",
 71:         "batch_size",
 72:         "cfg_scale",
 73:         "seed"
 74:     ],
 75:     "state_img2img": [
 76:         "prompt",
 77:         "negative_prompt",
 78:         "styles",
 79:         "sampling",
 80:         "scheduler",
 81:         "sampling_steps",
 82:         "width",
 83:         "height",
 84:         "batch_count",
 85:         "batch_size",
 86:         "cfg_scale",
 87:         "denoising_strength",
 88:         "seed"
 89:     ],
 90:     "state_extensions": [
 91:         "control-net",
 92:         "adetailer"
 93:     ],
 94:     "state_ui": [
 95:         "Reset Button",
 96:         "Import Button",
 97:         "Export Button"
 98:     ],
 99:     "tac_maxResults": 12.0,
100:     "tac_showWikiLinks": true,
101:     "custom_api_key": "65b66176dcf284b266579de57fbdc024",
102:     "aria2_flags": "--header=\"User-Agent: Mozilla/5.0\" --allow-overwrite=true --console-log-level=error --stderr=true -c -x16 -s16 -k1M -j5",
103:     "unpack_zip": true
104: }
```

## File: __configs__/ReForge/ui-config.json
```json
 1: {
 2:     "txt2img/Styles/value": [
 3:         "ANXETY V2"
 4:     ],
 5:     "customscript/sampler.py/txt2img/Sampling method/value": "Euler a",
 6:     "customscript/sampler.py/txt2img/Schedule type/value": "Karras",
 7:     "customscript/sampler.py/txt2img/Sampling steps/value": 28,
 8:     "txt2img/CFG Scale/value": 5.0,
 9:     "txt2img/Upscaler/value": "None",
10:     "txt2img/Denoising strength/value": 0.45,
11:     "txt2img/Control Mode/value": "My prompt is more important",
12:     "img2img/Styles/value": [
13:         "ANXETY V2"
14:     ],
15:     "customscript/sampler.py/img2img/Sampling method/value": "Euler a",
16:     "customscript/sampler.py/img2img/Schedule type/value": "Karras",
17:     "customscript/sampler.py/img2img/Sampling steps/value": 40,
18:     "img2img/Inpaint area/value": "Only masked",
19:     "img2img/Denoising strength/value": 0.4,
20:     "img2img/Control Mode/value": "My prompt is more important",
21:     "customscript/xyz_grid.py/txt2img/Include Sub Images/value": true,
22:     "customscript/prompt_matrix.py/txt2img/Grid margins (px)/value": 8,
23:     "customscript/xyz_grid.py/txt2img/Grid margins (px)/value": 8,
24:     "civitai_interface/NSFW content/value": true,
25:     "civitai_interface/Tile count:/value": 28,
26:     "customscript/wildcard_recursive.py/txt2img/Enable UmiAI/value": false
27: }
```

## File: __configs__/SD-UX/config.json
```json
  1: {
  2:     "uiux_show_input_range_ticks": false,
  3:     "sd_vae": "None",
  4:     "CLIP_stop_at_last_layers": 2,
  5:     "ad_max_models": 6,
  6:     "control_net_unit_count": 6,
  7:     "quicksettings_list": [
  8:         "sd_model_checkpoint",
  9:         "sd_vae",
 10:         "CLIP_stop_at_last_layers"
 11:     ],
 12:     "ui_tab_order": [
 13:         "txt2img",
 14:         "img2img",
 15:         "Image Info",
 16:         "SuperMerger",
 17:         "HUB",
 18:         "Infinite image browsing",
 19:         "CivitAI Browser+",
 20:         "Tagger",
 21:         "Settings",
 22:         "Extensions"
 23:     ],
 24:     "ui_reorder_list": [
 25:         "override_settings",
 26:         "inpaint",
 27:         "sampler",
 28:         "dimensions",
 29:         "cfg",
 30:         "seed",
 31:         "checkboxes",
 32:         "hires_fix",
 33:         "extra_options",
 34:         "batch",
 35:         "scripts"
 36:     ],
 37:     "hide_samplers": [
 38:         "UniPC",
 39:         "PLMS",
 40:         "LMS"
 41:     ],
 42:     "hidden_tabs": [
 43:         "Extras",
 44:         "PNG Info",
 45:         "Train",
 46:         "Checkpoint Merger"
 47:     ],
 48:     "extra_networks_default_multiplier": 0.7,
 49:     "samples_filename_pattern": "M=[model_name]_S=[seed]_D=[date]",
 50:     "grid_extended_filename": true,
 51:     "grid_text_active_color": "#ffffff",
 52:     "grid_background_color": "#0b0b0b",
 53:     "show_progress_grid": true,
 54:     "show_progress_every_n_steps": 2,
 55:     "live_previews_image_format": "webp",
 56:     "live_preview_content": "Prompt",
 57:     "live_preview_refresh_period": 100.0,
 58:     "live_preview_fast_interrupt": true,
 59:     "extra_networks_card_width": 200.0,
 60:     "extra_networks_card_height": 300.0,
 61:     "extra_networks_card_text_scale": 0.8,
 62:     "state_txt2img": [
 63:         "prompt",
 64:         "negative_prompt",
 65:         "styles",
 66:         "sampling",
 67:         "scheduler",
 68:         "sampling_steps",
 69:         "width",
 70:         "height",
 71:         "batch_count",
 72:         "batch_size",
 73:         "cfg_scale",
 74:         "seed"
 75:     ],
 76:     "state_img2img": [
 77:         "prompt",
 78:         "negative_prompt",
 79:         "styles",
 80:         "sampling",
 81:         "scheduler",
 82:         "sampling_steps",
 83:         "width",
 84:         "height",
 85:         "batch_count",
 86:         "batch_size",
 87:         "cfg_scale",
 88:         "denoising_strength",
 89:         "seed"
 90:     ],
 91:     "state_extensions": [
 92:         "control-net",
 93:         "adetailer"
 94:     ],
 95:     "state_ui": [
 96:         "Reset Button",
 97:         "Import Button",
 98:         "Export Button"
 99:     ],
100:     "tac_maxResults": 12.0,
101:     "tac_showWikiLinks": true,
102:     "custom_api_key": "65b66176dcf284b266579de57fbdc024",
103:     "aria2_flags": "--header=\"User-Agent: Mozilla/5.0\" --allow-overwrite=true --console-log-level=error --stderr=true -c -x16 -s16 -k1M -j5",
104:     "unpack_zip": true
105: }
```

## File: __configs__/SD-UX/ui-config.json
```json
 1: {
 2:     "txt2img/Styles/value": [
 3:         "ANXETY V2"
 4:     ],
 5:     "customscript/sampler.py/txt2img/Sampling method/value": "Euler a",
 6:     "customscript/sampler.py/txt2img/Schedule type/value": "Karras",
 7:     "customscript/sampler.py/txt2img/Sampling steps/value": 28,
 8:     "txt2img/CFG Scale/value": 5.0,
 9:     "txt2img/Upscaler/value": "None",
10:     "txt2img/Denoising strength/value": 0.45,
11:     "txt2img/Control Mode/value": "My prompt is more important",
12:     "img2img/Styles/value": [
13:         "ANXETY V2"
14:     ],
15:     "customscript/sampler.py/img2img/Sampling method/value": "Euler a",
16:     "customscript/sampler.py/img2img/Schedule type/value": "Karras",
17:     "customscript/sampler.py/img2img/Sampling steps/value": 40,
18:     "img2img/Inpaint area/value": "Only masked",
19:     "img2img/Denoising strength/value": 0.4,
20:     "img2img/Control Mode/value": "My prompt is more important",
21:     "customscript/xyz_grid.py/txt2img/Include Sub Images/value": true,
22:     "customscript/prompt_matrix.py/txt2img/Grid margins (px)/value": 8,
23:     "customscript/xyz_grid.py/txt2img/Grid margins (px)/value": 8,
24:     "civitai_interface/NSFW content/value": true,
25:     "civitai_interface/Tile count:/value": 28,
26:     "customscript/wildcard_recursive.py/txt2img/Enable UmiAI/value": false
27: }
```

## File: __configs__/gradio-tunneling.py
```python
  1: from typing import List, Optional, Tuple
  2: from pathlib import Path
  3: import subprocess
  4: import platform
  5: import argparse
  6: import requests
  7: import logging
  8: import secrets
  9: import atexit
 10: import stat
 11: import time
 12: import sys
 13: import os
 14: import re
 15: 
 16: 
 17: logging.basicConfig(level=logging.INFO)
 18: logger = logging.getLogger(__name__)
 19: 
 20: 
 21: class BinaryManager:
 22:     """Manages downloading and configuration of frpc binary"""
 23:     VERSION = "0.2"
 24:     BASE_URL = "https://cdn-media.huggingface.co/frpc-gradio-{version}/{binary_name}{extension}"
 25: 
 26:     def __init__(self):
 27:         self.system = platform.system().lower()
 28:         self.machine = self._normalize_architecture(platform.machine().lower())
 29:         self.extension = ".exe" if os.name == "nt" else ""
 30: 
 31:         self.binary_name = f"frpc_{self.system}_{self.machine}"
 32:         self.binary_path = Path(__file__).parent / f"{self.binary_name}_v{self.VERSION}"
 33: 
 34:     @staticmethod
 35:     def _normalize_architecture(arch: str) -> str:
 36:         return "amd64" if arch == "x86_64" else arch
 37: 
 38:     @property
 39:     def download_url(self) -> str:
 40:         return self.BASE_URL.format(
 41:             version=self.VERSION,
 42:             binary_name=self.binary_name,
 43:             extension=self.extension
 44:         )
 45: 
 46:     def download(self):
 47:         """Downloads and configures binary if needed"""
 48:         if self.binary_path.exists():
 49:             return
 50: 
 51:         logger.info("Downloading frpc binary...")
 52:         response = requests.get(self.download_url)
 53: 
 54:         if response.status_code == 403:
 55:             raise OSError(f"Unsupported platform: {platform.uname()}")
 56: 
 57:         response.raise_for_status()
 58: 
 59:         self.binary_path.write_bytes(response.content)
 60:         self.binary_path.chmod(self.binary_path.stat().st_mode | stat.S_IEXEC)
 61: 
 62: 
 63: class Tunnel:
 64:     """Manages application tunnel lifecycle"""
 65:     TIMEOUT = 30
 66:     ERROR_MSG = "Failed to create share URL. Logs:\n{logs}"
 67:     GRADIO_API = "https://api.gradio.app/v2/tunnel-request"
 68: 
 69:     def __init__(
 70:         self,
 71:         local_host: str,
 72:         local_port: int,
 73:         share_token: str,
 74:         remote_server: Optional[str] = None
 75:     ):
 76:         self.local_host = local_host
 77:         self.local_port = local_port
 78:         self.share_token = share_token
 79:         self.remote_host, self.remote_port = self._resolve_remote_server(remote_server)
 80: 
 81:         self.proc: Optional[subprocess.Popen] = None
 82:         self.binary = BinaryManager()
 83:         self.url: Optional[str] = None
 84: 
 85:     def _resolve_remote_server(self, server: Optional[str]) -> Tuple[str, int]:
 86:         """Determines remote tunnel server address"""
 87:         if server:
 88:             host, port = server.split(":", 1)
 89:             return host, int(port)
 90: 
 91:         response = requests.get(self.GRADIO_API)
 92:         response.raise_for_status()
 93:         data = response.json()[0]
 94:         return data["host"], int(data["port"])
 95: 
 96:     def start(self) -> str:
 97:         """Starts tunnel and returns public URL"""
 98:         self.binary.download()
 99:         self._launch_process()
100:         self.url = self._read_process_output()
101:         logger.info("Tunnel established at %s", self.url)
102:         return self.url
103: 
104:     def _launch_process(self):
105:         """Launches frpc process"""
106:         command = [
107:             str(self.binary.binary_path),
108:             "http",
109:             "-n", self.share_token,
110:             "-l", str(self.local_port),
111:             "-i", self.local_host,
112:             "--uc",
113:             "--sd", "random",
114:             "--ue",
115:             "--server_addr", f"{self.remote_host}:{self.remote_port}",
116:             "--disable_log_color",
117:         ]
118: 
119:         self.proc = subprocess.Popen(
120:             command,
121:             stdout=subprocess.PIPE,
122:             stderr=subprocess.STDOUT,
123:             universal_newlines=True
124:         )
125:         atexit.register(self.stop)
126: 
127:     def _read_process_output(self) -> str:
128:         """Reads process output to extract tunnel URL"""
129:         start_time = time.time()
130:         logs = []
131: 
132:         while True:
133:             if time.time() - start_time > self.TIMEOUT:
134:                 self._handle_error(logs)
135: 
136:             line = self.proc.stdout.readline().strip()  # type: ignore
137:             if not line:
138:                 continue
139: 
140:             logs.append(line)
141:             logger.debug(line)
142: 
143:             if "start proxy success" in line:
144:                 if match := re.search(r"start proxy success: (.+)", line):
145:                     return match.group(1)
146:                 self._handle_error(logs)
147: 
148:             elif "login to server failed" in line:
149:                 self._handle_error(logs)
150: 
151:     def _handle_error(self, logs: List[str]):
152:         """Handles tunnel errors"""
153:         self.stop()
154:         logger.error("Tunnel failure logs:\n%s", "\n".join(logs))
155:         raise RuntimeError(self.ERROR_MSG.format(logs="\n".join(logs)))
156: 
157:     def stop(self):
158:         """Stops tunnel process"""
159:         if self.proc and self.proc.poll() is None:
160:             logger.info("Stopping tunnel...")
161:             self.proc.terminate()
162:             self.proc.wait()
163: 
164: 
165: def main():
166:     """CLI entry point"""
167:     parser = argparse.ArgumentParser(description="Create application tunnel")
168:     parser.add_argument(
169:         "port",
170:         nargs="?",
171:         type=int,
172:         default=7860,
173:         help="Local port to expose (default: 7860)"
174:     )
175:     parser.add_argument(
176:         "--subdomain", "-s",
177:         type=str,
178:         help="Custom subdomain for the tunnel"
179:     )
180:     args = parser.parse_args()
181: 
182:     try:
183:         tunnel = Tunnel(
184:             local_host="127.0.0.1",
185:             local_port=args.port,
186:             share_token=args.subdomain or secrets.token_urlsafe(32)
187:         )
188:         url = tunnel.start()
189:         print(f"Tunnel URL: {url}")
190: 
191:         # Keep alive with interrupt handling
192:         while True:
193:             time.sleep(3600 * 24 * 3)
194:     except KeyboardInterrupt:
195:         logger.info("Interrupt received. Exiting...")
196:     except Exception as e:
197:         logger.error("Tunnel creation failed: %s", e)
198:         sys.exit(1)
199: 
200: 
201: if __name__ == "__main__":
202:     main()
```

## File: __configs__/styles.csv
```
 1: name,prompt,negative_prompt
 2: None,,
 3: 
 4: ———— Base Negative Style ————
 5: ANXETY,, "extra fingers, fewer fingers, (low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), bad composition, inaccurate eyes, extra digit, fewer digits, (extra arms:1.2), easynegative"
 6: ANXETY V2,, "lowres, (worst quality, low quality:1.2), bad anatomy, bad hands, 4koma, comic, greyscale, censored, jpeg artifacts, overly saturated, overly vivid"
 7: XpucT (Anime),, "(worst quality, low quality, mutated hands and fingers, bad anatomy, wrong anatomy, ugly, mutation:1.2)"
 8: XpucT,, "(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation"
 9: XpucT V2,, "oversaturated, disfigured, poorly, bad, wrong, mutated, [disfigured, poorly drawn], [bad : wrong] anatomy, [extra | missing | floating | disconnected] limb, mutated, blurry"
10: Simply,, "worst quality, bad quality, extra arms, extra hands, disconnected limbs, amputation, blurry"
11: Unknown,, "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face"
12: UnknownV2,, "EasyNegativeV2, (text, signature, logo:1.4), (worst quality, low quality:1.3), illustration, sketch, drawing, anime, cartoon, [:(badhandv4:1.5):18]"
13: 
14: ———— Other Negative Style ————
15: Default,"masterpiece, best quality, {promt}","lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), ((extra feet)), cropped, worst quality, low quality, humpbacked, ((jpeg artifacts))"
16: Nyan Negative,,"(EasyNegative), [[[[[Bad Artist Anime, sketch by Bad Artist OG]]]]], [[[mutation, lowres, bad hands, [text, signature, (watermark:1.2), username], blurry, realistic, simple background, limited palette]]], (forehead jewel:1.2), (forehead mark:1.5), (bad and mutated hands:1.3), (worst quality:2.0), (low quality:2.0), (blurry:2.0), multiple limbs, bad anatomy, (interlocked fingers:1.2),(interlocked leg:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), crown braid, (deformed fingers:1.2), (long fingers:1.2)"
17: New Negative meta,,"(low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), bad composition, inaccurate eyes, extra digit, fewer digits, (extra arms:1.2)"
18: NoCrypt Fav Negative,,"lowres, (bad anatomy:1.1025), (bad hands:1.1025), text, missing finger, extra digits, fewer digits, blurry, (mutated hands and fingers:1.1025), (poorly drawn face:1.05), (mutation:1.1025), (deformed face:1.1025), (ugly:1.05), (bad proportions:1.1025), (extra limbs:1.1025), extra face, (double head:1.05), (extra head:1.05), (extra feet:1.1025), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, (jpeg artifacts:1.1025)"
19: Andite Fav Negative,,"(low quality, worst quality:1.4)"
20: 
21: ———— Other ————
```

## File: __configs__/user.css
```css
 1: /* Gradio Container */
 2: .gradio-container {
 3:   padding: 15px !important;
 4: }
 5: div.compact {
 6:   gap: 6px !important;
 7: }
 8: 
 9: /* Main */
10: #txt2img_gallery,
11: #img2img_gallery {
12:   height: 650px; /* Output height */
13: }
14: 
15: #txt2img_results,
16: #img2img_results {
17:   min-width: 50%; /* Output width */
18: }
19: 
20: #txt2img_gallery > .grid-wrap,
21: #txt2img_gallery > .preview,
22: #img2img_gallery > .grid-wrap,
23: #img2img_gallery > .preview {
24:   max-height: none;
25: }
26: 
27: #txt2img_extra_networks:not(div),
28: #img2img_extra_networks:not(div) {
29:   order: 1 !important;
30: }
31: 
32: #setting_show_progress_every_n_steps > div.wrap > div > label > span {
33:   white-space: nowrap;
34:   overflow: hidden;
35:   width: 220px;
36:   text-overflow: ellipsis;
37: }
38: 
39: /* Fixing Sampling steps covered up on phone */
40: @media screen and (min-width: 420px) {
41:   #sampler_selection_txt2img,
42:   #sampler_selection_img2img {
43:     flex-direction: row;
44:   }
45: }
46: 
47: @media screen and (max-width: 420px) {
48:   #sampler_selection_txt2img,
49:   #sampler_selection_img2img {
50:     flex-direction: column;
51:   }
52: }
53: 
54: #txt2img_script_container > * .block.padded,
55: #img2img_script_container > * .block.padded {
56:   padding: 10px !important;
57: }
58: 
59: #txt2img_script_container > div,
60: #img2img_script_container > div {
61:   margin-bottom: 10px;
62: }
```

## File: .Docs/SVG/en/colab-en.svg
```
  1: <svg fill="none" viewBox="0 0 800 160" width="800" height="160" xmlns="http://www.w3.org/2000/svg">
  2:     <foreignObject width="100%" height="100%">
  3:         <div xmlns="http://www.w3.org/1999/xhtml">
  4:             <style>
  5:                 @keyframes letterSpacingH2 {
  6:                     0% {
  7:                         letter-spacing: 15px; 
  8:                     }
  9:                     100% {
 10:                         letter-spacing: 20px;
 11:                     }
 12:                 }
 13: 
 14:                 @keyframes fadeIn {
 15:                     0% {
 16:                         opacity: 0;
 17:                         transform: translateX(-50%) translateY(50%);
 18:                     }
 19:                     66% {
 20:                         opacity: 0;
 21:                         transform: translateX(-50%) translateY(50%);
 22:                     }
 23:                     100% {
 24:                         opacity: 0.5;
 25:                         transform: translateX(-50%) translateY(0%);
 26:                     }
 27:                 }
 28: 
 29:                 @keyframes moveUp {
 30:                     0% {
 31:                         transform: translateY(0);
 32:                     }
 33:                     100% {
 34:                         transform: translateY(-20px);
 35:                     }
 36:                 }
 37: 
 38:                 .container {
 39:                     display: flex;
 40:                     flex-direction: column;
 41:                     align-items: center;
 42:                     justify-content: center;
 43:                     width: auto;
 44:                     height: 160px;
 45:                     background: #E35D6A;
 46:                     box-shadow: inset 0 0 1px 2px #E87D87;
 47:                     border-radius: 10px;
 48:                     user-select: none;
 49:                     font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
 50:                 }
 51: 
 52:                 .H1 {
 53:                     color: #8DFFDD;
 54:                     font-size: 45px;
 55:                     letter-spacing: 10px;
 56:                     font-weight: bold;
 57:                     text-shadow:
 58:                         0 1px 0 #1EB387,
 59:                         0 2px 0 #1EB387,
 60:                         0 3px 0 #1EB387,
 61:                         0 4px 0 #1EB387,
 62:                         0 12px 5px rgba(0, 0, 0, 0.1);
 63:                     animation: moveUp 1s ease forwards 3.85s;
 64:                 }
 65: 
 66:                 .H2 {
 67:                     color: #FFFFFF;
 68:                     font-size: 70px;
 69:                     letter-spacing: 15px;
 70:                     font-weight: bold;
 71:                     text-shadow:
 72:                         0 1px 0 #BDBBBB,
 73:                         0 2px 0 #BDBBBB,
 74:                         0 3px 0 #BDBBBB,
 75:                         0 4px 0 #BDBBBB,
 76:                         0 12px 5px rgba(0, 0, 0, 0.1);
 77:                     animation: letterSpacingH2 ease-in-out 1s infinite alternate, moveUp 1s ease forwards 4s;
 78:                     margin-top: -15px;
 79:                 }
 80: 
 81:                 .source {
 82:                     position: absolute;
 83:                     top: 98px;
 84:                     left: 50%;
 85:                     opacity: 0;
 86:                     transform: translateX(-50%) translateY(50%);
 87:                     animation: 3s ease 2s normal forwards 1 fadeIn;
 88:                 }
 89: 
 90:                 p {
 91:                     color: white;
 92:                     font-size: 25px;
 93:                     text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
 94:                     white-space: nowrap;
 95:                     font-weight: bold;
 96:                 }
 97:             </style>
 98: 
 99:             <div class="container">
100:                 <div class="H1">Open In</div>
101:                 <div class="H2">COLAB</div>
102: 
103:                 <div class="source">
104:                     <p>Click to open NoteBook</p>
105:                 </div>
106:             </div>
107:         </div>
108:     </foreignObject>
109: </svg>
```

## File: .Docs/SVG/en/discord-en.svg
```
 1: <svg fill="none" viewBox="0 0 800 130" width="800" height="130" xmlns="http://www.w3.org/2000/svg">
 2:     <foreignObject width="100%" height="100%">
 3:         <div xmlns="http://www.w3.org/1999/xhtml">
 4:             <style>
 5: 			@keyframes rotateLabel {
 6: 			    0% {
 7: 			        transform: rotate(1deg) translateY(-20px);
 8: 			    }
 9: 			    100% {
10: 			        transform: rotate(-1deg) translateY(-20px);
11:                     }
12: 			}
13: 
14:                 @keyframes fadeIn {
15:                     0% {
16:                         opacity: 0;
17:                         transform: translateX(-50%) translateY(50%);
18:                     }
19:                     66% {
20:                         opacity: 0;
21:                         transform: translateX(-50%) translateY(50%);
22:                     }
23:                     100% {
24:                         opacity: 0.5;
25:                         transform: translateX(-50%) translateY(0%);
26:                     }
27:                 }
28: 
29:                 .container {
30:                     display: flex;
31:                     flex-direction: column;
32:                     align-items: center;
33:                     justify-content: center;
34:                     width: auto;
35:                     height: 130px;
36:                     background: #004C4C;
37:                     box-shadow: inset 0 0 1px 2px #006666;
38:                     border-radius: 10px;
39:                     user-select: none;
40:                     font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
41:                 }
42: 
43:                 .H1 {
44:                     color: #B2D8D8;
45:                     font-size: 70px;
46:                     letter-spacing: 10px;
47:                     font-weight: bold;
48:                     text-shadow:
49:                         0 1px 0 #008080,
50:                         0 2px 0 #008080,
51:                         0 3px 0 #008080,
52:                         0 4px 0 #008080,
53:                         0 12px 5px rgba(0, 0, 0, 0.1);
54:                     animation: rotateLabel ease-in-out 3s infinite alternate;
55:                 }
56: 
57:                 .source {
58:                     position: absolute;
59:                     top: 55px;
60:                     left: 50%;
61:                     opacity: 0;
62:                     transform: translateX(-50%) translateY(50%);
63:                     animation: 3s ease 2s normal forwards 1 fadeIn;
64:                 }
65: 
66:                 p {
67:                     color: white;
68:                     font-size: 30px;
69:                     text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
70:                     white-space: nowrap;
71:                     font-weight: bold;
72:                 }
73:             </style>
74: 
75:             <div class="container">
76:                 <div class="H1">DISCORD</div>
77: 
78:                 <div class="source">
79:                     <p>Click to join the server</p>
80:                 </div>
81:             </div>
82:         </div>
83:     </foreignObject>
84: </svg>
```

## File: .Docs/SVG/en/kaggle-en.svg
```
  1: <svg fill="none" viewBox="0 0 800 160" width="800" height="160" xmlns="http://www.w3.org/2000/svg">
  2:     <foreignObject width="100%" height="100%">
  3:         <div xmlns="http://www.w3.org/1999/xhtml">
  4:             <style>
  5:                 @keyframes letterSpacingH2 {
  6:                     0% {
  7:                         letter-spacing: 15px; 
  8:                     }
  9:                     100% {
 10:                         letter-spacing: 20px;
 11:                     }
 12:                 }
 13: 
 14:                 @keyframes fadeIn {
 15:                     0% {
 16:                         opacity: 0;
 17:                         transform: translateX(-50%) translateY(50%);
 18:                     }
 19:                     66% {
 20:                         opacity: 0;
 21:                         transform: translateX(-50%) translateY(50%);
 22:                     }
 23:                     100% {
 24:                         opacity: 0.5;
 25:                         transform: translateX(-50%) translateY(0%);
 26:                     }
 27:                 }
 28: 
 29:                 @keyframes moveUp {
 30:                     0% {
 31:                         transform: translateY(0);
 32:                     }
 33:                     100% {
 34:                         transform: translateY(-20px);
 35:                     }
 36:                 }
 37: 
 38:                 .container {
 39:                     display: flex;
 40:                     flex-direction: column;
 41:                     align-items: center;
 42:                     justify-content: center;
 43:                     width: auto;
 44:                     height: 160px;
 45:                     background: #B39BC8;
 46:                     box-shadow: inset 0 0 1px 2px #A18BB4;
 47:                     border-radius: 10px;
 48:                     user-select: none;
 49:                     font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
 50:                 }
 51: 
 52:                 .H1 {
 53:                     color: #FFFFFF;
 54:                     font-size: 45px;
 55:                     letter-spacing: 10px;
 56:                     font-weight: bold;
 57:                     text-shadow:
 58:                         0 1px 0 #BDBBBB,
 59:                         0 2px 0 #BDBBBB,
 60:                         0 3px 0 #BDBBBB,
 61:                         0 4px 0 #BDBBBB,
 62:                         0 12px 5px rgba(0, 0, 0, 0.1);
 63:                     animation: moveUp 1s ease forwards 3.85s;
 64:                 }
 65: 
 66:                 .H2 {
 67:                     color: #F0EBF4;
 68:                     font-size: 70px;
 69:                     letter-spacing: 15px;
 70:                     font-weight: bold;
 71:                     text-shadow:
 72:                         0 1px 0 #BCB4C2,
 73:                         0 2px 0 #BCB4C2,
 74:                         0 3px 0 #BCB4C2,
 75:                         0 4px 0 #BCB4C2,
 76:                         0 12px 5px rgba(0, 0, 0, 0.1);
 77:                     animation: letterSpacingH2 ease-in-out 1s infinite alternate, moveUp 1s ease forwards 4s;
 78:                     margin-top: -15px;
 79:                 }
 80: 
 81:                 .source {
 82:                     position: absolute;
 83:                     top: 98px;
 84:                     left: 50%;
 85:                     opacity: 0;
 86:                     transform: translateX(-50%) translateY(50%);
 87:                     animation: 3s ease 2s normal forwards 1 fadeIn;
 88:                 }
 89: 
 90:                 p {
 91:                     color: white;
 92:                     font-size: 25px;
 93:                     text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
 94:                     white-space: nowrap;
 95:                     font-weight: bold;
 96:                 }
 97:             </style>
 98: 
 99:             <div class="container">
100:                 <div class="H1">Open In</div>
101:                 <div class="H2">KAGGLE</div>
102: 
103:                 <div class="source">
104:                     <p>Click to copy NoteBook</p>
105:                 </div>
106:             </div>
107:         </div>
108:     </foreignObject>
109: </svg>
```

## File: .Docs/SVG/ru/colab-ru.svg
```
  1: <svg fill="none" viewBox="0 0 800 160" width="800" height="160" xmlns="http://www.w3.org/2000/svg">
  2:     <foreignObject width="100%" height="100%">
  3:         <div xmlns="http://www.w3.org/1999/xhtml">
  4:             <style>
  5:                 @keyframes letterSpacingH2 {
  6:                     0% {
  7:                         letter-spacing: 15px; 
  8:                     }
  9:                     100% {
 10:                         letter-spacing: 20px;
 11:                     }
 12:                 }
 13: 
 14:                 @keyframes fadeIn {
 15:                     0% {
 16:                         opacity: 0;
 17:                         transform: translateX(-50%) translateY(50%);
 18:                     }
 19:                     66% {
 20:                         opacity: 0;
 21:                         transform: translateX(-50%) translateY(50%);
 22:                     }
 23:                     100% {
 24:                         opacity: 0.5;
 25:                         transform: translateX(-50%) translateY(0%);
 26:                     }
 27:                 }
 28: 
 29:                 @keyframes moveUp {
 30:                     0% {
 31:                         transform: translateY(0);
 32:                     }
 33:                     100% {
 34:                         transform: translateY(-20px);
 35:                     }
 36:                 }
 37: 
 38:                 .container {
 39:                     display: flex;
 40:                     flex-direction: column;
 41:                     align-items: center;
 42:                     justify-content: center;
 43:                     width: auto;
 44:                     height: 160px;
 45:                     background: #E35D6A;
 46:                     box-shadow: inset 0 0 1px 2px #E87D87;
 47:                     border-radius: 10px;
 48:                     user-select: none;
 49:                     font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
 50:                 }
 51: 
 52:                 .H1 {
 53:                     color: #8DFFDD;
 54:                     font-size: 45px;
 55:                     letter-spacing: 10px;
 56:                     font-weight: bold;
 57:                     text-shadow:
 58:                         0 1px 0 #1EB387,
 59:                         0 2px 0 #1EB387,
 60:                         0 3px 0 #1EB387,
 61:                         0 4px 0 #1EB387,
 62:                         0 12px 5px rgba(0, 0, 0, 0.1);
 63:                     animation: moveUp 1s ease forwards 3.85s;
 64:                 }
 65: 
 66:                 .H2 {
 67:                     color: #FFFFFF;
 68:                     font-size: 70px;
 69:                     letter-spacing: 15px;
 70:                     font-weight: bold;
 71:                     text-shadow:
 72:                         0 1px 0 #BDBBBB,
 73:                         0 2px 0 #BDBBBB,
 74:                         0 3px 0 #BDBBBB,
 75:                         0 4px 0 #BDBBBB,
 76:                         0 12px 5px rgba(0, 0, 0, 0.1);
 77:                     animation: letterSpacingH2 ease-in-out 1s infinite alternate, moveUp 1s ease forwards 4s;
 78:                     margin-top: -15px;
 79:                 }
 80: 
 81:                 .source {
 82:                     position: absolute;
 83:                     top: 98px;
 84:                     left: 50%;
 85:                     opacity: 0;
 86:                     transform: translateX(-50%) translateY(50%);
 87:                     animation: 3s ease 2s normal forwards 1 fadeIn;
 88:                 }
 89: 
 90:                 p {
 91:                     color: white;
 92:                     font-size: 25px;
 93:                     text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
 94:                     white-space: nowrap;
 95:                     font-weight: bold;
 96:                 }
 97:             </style>
 98: 
 99:             <div class="container">
100:                 <div class="H1">Открыть в</div>
101:                 <div class="H2">COLAB</div>
102: 
103:                 <div class="source">
104:                     <p>Нажмите, чтобы открыть Блокнот</p>
105:                 </div>
106:             </div>
107:         </div>
108:     </foreignObject>
109: </svg>
```

## File: .Docs/SVG/ru/discord-ru.svg
```
 1: <svg fill="none" viewBox="0 0 800 130" width="800" height="130" xmlns="http://www.w3.org/2000/svg">
 2:     <foreignObject width="100%" height="100%">
 3:         <div xmlns="http://www.w3.org/1999/xhtml">
 4:             <style>
 5: 			@keyframes rotateLabel {
 6: 			    0% {
 7: 			        transform: rotate(1deg) translateY(-20px);
 8: 			    }
 9: 			    100% {
10: 			        transform: rotate(-1deg) translateY(-20px);
11:                     }
12: 			}
13: 
14:                 @keyframes fadeIn {
15:                     0% {
16:                         opacity: 0;
17:                         transform: translateX(-50%) translateY(50%);
18:                     }
19:                     66% {
20:                         opacity: 0;
21:                         transform: translateX(-50%) translateY(50%);
22:                     }
23:                     100% {
24:                         opacity: 0.5;
25:                         transform: translateX(-50%) translateY(0%);
26:                     }
27:                 }
28: 
29:                 .container {
30:                     display: flex;
31:                     flex-direction: column;
32:                     align-items: center;
33:                     justify-content: center;
34:                     width: auto;
35:                     height: 130px;
36:                     background: #004C4C;
37:                     box-shadow: inset 0 0 1px 2px #006666;
38:                     border-radius: 10px;
39:                     user-select: none;
40:                     font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
41:                 }
42: 
43:                 .H1 {
44:                     color: #B2D8D8;
45:                     font-size: 70px;
46:                     letter-spacing: 10px;
47:                     font-weight: bold;
48:                     text-shadow:
49:                         0 1px 0 #008080,
50:                         0 2px 0 #008080,
51:                         0 3px 0 #008080,
52:                         0 4px 0 #008080,
53:                         0 12px 5px rgba(0, 0, 0, 0.1);
54:                     animation: rotateLabel ease-in-out 3s infinite alternate;
55:                 }
56: 
57:                 .source {
58:                     position: absolute;
59:                     top: 55px;
60:                     left: 50%;
61:                     opacity: 0;
62:                     transform: translateX(-50%) translateY(50%);
63:                     animation: 3s ease 2s normal forwards 1 fadeIn;
64:                 }
65: 
66:                 p {
67:                     color: white;
68:                     font-size: 30px;
69:                     text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
70:                     white-space: nowrap;
71:                     font-weight: bold;
72:                 }
73:             </style>
74: 
75:             <div class="container">
76:                 <div class="H1">DISCORD</div>
77: 
78:                 <div class="source">
79:                     <p>Нажмите, чтобы присоединиться к серверу</p>
80:                 </div>
81:             </div>
82:         </div>
83:     </foreignObject>
84: </svg>
```

## File: .Docs/SVG/ru/kaggle-ru.svg
```
  1: <svg fill="none" viewBox="0 0 800 160" width="800" height="160" xmlns="http://www.w3.org/2000/svg">
  2:     <foreignObject width="100%" height="100%">
  3:         <div xmlns="http://www.w3.org/1999/xhtml">
  4:             <style>
  5:                 @keyframes letterSpacingH2 {
  6:                     0% {
  7:                         letter-spacing: 15px; 
  8:                     }
  9:                     100% {
 10:                         letter-spacing: 20px;
 11:                     }
 12:                 }
 13: 
 14:                 @keyframes fadeIn {
 15:                     0% {
 16:                         opacity: 0;
 17:                         transform: translateX(-50%) translateY(50%);
 18:                     }
 19:                     66% {
 20:                         opacity: 0;
 21:                         transform: translateX(-50%) translateY(50%);
 22:                     }
 23:                     100% {
 24:                         opacity: 0.5;
 25:                         transform: translateX(-50%) translateY(0%);
 26:                     }
 27:                 }
 28: 
 29:                 @keyframes moveUp {
 30:                     0% {
 31:                         transform: translateY(0);
 32:                     }
 33:                     100% {
 34:                         transform: translateY(-20px);
 35:                     }
 36:                 }
 37: 
 38:                 .container {
 39:                     display: flex;
 40:                     flex-direction: column;
 41:                     align-items: center;
 42:                     justify-content: center;
 43:                     width: auto;
 44:                     height: 160px;
 45:                     background: #B39BC8;
 46:                     box-shadow: inset 0 0 1px 2px #A18BB4;
 47:                     border-radius: 10px;
 48:                     user-select: none;
 49:                     font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
 50:                 }
 51: 
 52:                 .H1 {
 53:                     color: #FFFFFF;
 54:                     font-size: 45px;
 55:                     letter-spacing: 10px;
 56:                     font-weight: bold;
 57:                     text-shadow:
 58:                         0 1px 0 #BDBBBB,
 59:                         0 2px 0 #BDBBBB,
 60:                         0 3px 0 #BDBBBB,
 61:                         0 4px 0 #BDBBBB,
 62:                         0 12px 5px rgba(0, 0, 0, 0.1);
 63:                     animation: moveUp 1s ease forwards 3.85s;
 64:                 }
 65: 
 66:                 .H2 {
 67:                     color: #F0EBF4;
 68:                     font-size: 70px;
 69:                     letter-spacing: 15px;
 70:                     font-weight: bold;
 71:                     text-shadow:
 72:                         0 1px 0 #BCB4C2,
 73:                         0 2px 0 #BCB4C2,
 74:                         0 3px 0 #BCB4C2,
 75:                         0 4px 0 #BCB4C2,
 76:                         0 12px 5px rgba(0, 0, 0, 0.1);
 77:                     animation: letterSpacingH2 ease-in-out 1s infinite alternate, moveUp 1s ease forwards 4s;
 78:                     margin-top: -15px;
 79:                 }
 80: 
 81:                 .source {
 82:                     position: absolute;
 83:                     top: 98px;
 84:                     left: 50%;
 85:                     opacity: 0;
 86:                     transform: translateX(-50%) translateY(50%);
 87:                     animation: 3s ease 2s normal forwards 1 fadeIn;
 88:                 }
 89: 
 90:                 p {
 91:                     color: white;
 92:                     font-size: 25px;
 93:                     text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
 94:                     white-space: nowrap;
 95:                     font-weight: bold;
 96:                 }
 97:             </style>
 98: 
 99:             <div class="container">
100:                 <div class="H1">Открыть в</div>
101:                 <div class="H2">KAGGLE</div>
102: 
103:                 <div class="source">
104:                     <p>Нажмите, чтобы скопировать Блокнот</p>
105:                 </div>
106:             </div>
107:         </div>
108:     </foreignObject>
109: </svg>
```

## File: .Docs/SVG/Boosty_Logo_Color.svg
```
 1: <?xml version="1.0" encoding="utf-8"?>
 2: <!-- Generator: Adobe Illustrator 24.2.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
 3: <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
 4: 	 viewBox="0 0 715.8 317.4" style="enable-background:new 0 0 715.8 317.4;" xml:space="preserve">
 5: <style type="text/css">
 6: 	.st0{fill:#242B2C;}
 7: 	.st1{fill:url(#SVGID_1_);}
 8: </style>
 9: <g id="text">
10: 	<path class="st0" d="M632.8,138.6l-23.1,35.9l-2.3-35.9h-19.3h-6h-7.9c3.1-10.5,5.5-19,5.5-19l1.3-4.2h-25.5l-1.2,4.2l-5.5,19
11: 		h-21.7c-3.6,0-5.4,0-5.4,0c-22.3,0-34.8,6.4-40,18.4c-3-11-12.9-18.4-28.2-18.4c-13.2,0-24.9,4.9-33.6,12.7
12: 		c-4.5-7.8-13.4-12.7-25.8-12.7c-14.2,0-26.5,5.7-35.5,14.4c-4.1-8.7-13.4-14.4-26.7-14.4c-4.6,0-8.9,0.6-13,1.7l2-6.9
13: 		c0-0.1,0.1-0.2,0.1-0.3l5.1-17.7h-25.4l-16.2,55.8c-0.4,1.1-0.8,2.2-1.1,3.4c-0.7,2.6-1.2,5.1-1.4,7.5
14: 		c-2.1,15.6,4.7,27.3,23.6,28.1c1.7,0.2,3.5,0.3,5.5,0.3c13.4,0,25.9-5.7,35.1-14.4c3.9,8.7,13,14.4,27.1,14.4
15: 		c12.5,0,24.3-4.9,33.2-12.7c4.3,7.8,13.1,12.7,26.2,12.7c28.4,0,49.6,0,63.6,0c19.7,0,30.8-3.9,36.6-12.3c0,8.1,4.6,12.3,16.2,12.3
16: 		c9.4,0,22-2.1,39.3-6.3L563.3,240h25.4l69.5-101.4H632.8z M334.3,174.5c-2.4,8.2-10,14.8-17,14.8c-7,0-10.8-6.6-8.4-14.8
17: 		c2.4-8.2,10-14.8,17-14.8C332.9,159.7,336.7,166.3,334.3,174.5z M396.4,174.5c-2.4,8.2-10,14.8-17,14.8s-10.8-6.6-8.4-14.8
18: 		s10-14.8,17-14.8S398.8,166.3,396.4,174.5z M430.5,174.5c2.4-8.2,10-14.8,17-14.8s10.8,6.6,8.4,14.8c-2.3,8.1-9.8,14.6-16.7,14.8
19: 		c-0.2,0-0.4,0-0.6,0C431.8,189.1,428.2,182.6,430.5,174.5z M512.2,186.7c-1.3,3-11.3,2.5-13.8,2.6c0,0-6.6,0-24.6,0
20: 		c3.3-4.5,5.9-9.5,7.4-14.8c0.2-0.5,0.3-1.1,0.4-1.6c2.7,3.8,8.3,7.2,19.2,9.4C511.2,184.3,513.1,183.7,512.2,186.7z M537.3,178.6
21: 		c-2.2-8.4-11.5-11.8-24.6-13.4c-5.5-0.7-8.6-0.9-7.9-3.3c0.5-1.8,3.3-2.2,9.2-2.2c3.7,0,8.1,0,13.2,0h15.6L537.3,178.6z
22: 		 M562.6,178.7c0-0.2,2.5-8.6,5.5-19h16.1l2.6,26.9C560.3,192.3,559.7,190.8,562.6,178.7z"/>
23: </g>
24: <g id="sign">
25: 	<g id="b_1_">
26: 		<linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="188.3014" y1="75.5591" x2="123.8106" y2="295.4895">
27: 			<stop  offset="0" style="stop-color:#EF7829"/>
28: 			<stop  offset="5.189538e-02" style="stop-color:#F07529"/>
29: 			<stop  offset="0.3551" style="stop-color:#F0672B"/>
30: 			<stop  offset="0.6673" style="stop-color:#F15E2C"/>
31: 			<stop  offset="1" style="stop-color:#F15A2C"/>
32: 		</linearGradient>
33: 		<path class="st1" d="M87.5,163.9L120.2,51h50.1l-10.1,35c-0.1,0.2-0.2,0.4-0.3,0.6L133.3,179h24.8c-10.4,25.9-18.5,46.2-24.3,60.9
34: 			c-45.8-0.5-58.6-33.3-47.4-72.1 M133.9,240l60.4-86.9h-25.6l22.3-55.7c38.2,4,56.2,34.1,45.6,70.5C225.3,207,179.4,240,134.8,240
35: 			C134.5,240,134.2,240,133.9,240z"/>
36: 	</g>
37: </g>
38: </svg>
```

## File: .Docs/SVG/DA_Logo_Color.svg
```
 1: <?xml version="1.0" encoding="utf-8"?>
 2: <!-- Generator: Adobe Illustrator 23.0.3, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
 3: <svg version="1.1" id="Logo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
 4: 	 viewBox="0 0 236 80" style="enable-background:new 0 0 236 80;" xml:space="preserve">
 5: <style type="text/css">
 6: 	.st0{fill:#F57D07;}
 7: 	.st1{fill:url(#D_1_);}
 8: </style>
 9: <g id="Text" transform="translate(0.000000, 7.000000)">
10: 	<path id="Shape" class="st0" d="M20.2,11.4c-0.4,5.5-4.2,11-11.8,11H0L1.9,0.8h8.5C17.8,0.8,20.6,6,20.2,11.4z M4.4,18.4h4.4
11: 		c4.9,0,7.2-3.6,7.4-7.1C16.4,8,14.7,4.6,10,4.6H5.6L4.4,18.4z"/>
12: 	<path class="st0" d="M44.4,11.7c-0.5,5.6-4.4,11.2-12.1,11.2s-10.6-5.5-10.1-11.1S26.9,0.3,34.3,0.3S45,6,44.4,11.7z M26.3,11.8
13: 		c-0.2,3.6,1.4,7.3,6.4,7.3s7.3-3.8,7.7-7.4C40.8,8.2,39.1,4,34,4S26.5,8.1,26.3,11.8L26.3,11.8z"/>
14: 	<polygon id="Path" class="st0" points="62.6,0.7 66.7,0.7 64.8,22.4 62.2,22.4 62.2,22.4 52.2,7.8 50.9,22.4 46.8,22.4 48.7,0.8 
15: 		52,0.8 61.4,14.2 	"/>
16: 	<path class="st0" d="M84.2,18.3H72.9l-2.2,4.1h-4.4L77.8,0.8h4.5l7.8,21.6h-4.4L84.2,18.3z M79.7,5.3l-4.8,9.2h8L79.7,5.3z"/>
17: 	<polygon class="st0" points="95.6,4.5 88.7,4.5 89,0.8 106.8,0.8 106.5,4.5 99.6,4.5 98.1,22.4 94,22.4 	"/>
18: 	<polygon class="st0" points="107.4,22.4 109.3,0.8 113.3,0.8 111.4,22.4 	"/>
19: 	<path class="st0" d="M138.1,11.7c-0.6,5.6-4.5,11.2-12.1,11.2s-10.6-5.5-10.1-11.1S120.5,0.3,128,0.3S138.6,6,138.1,11.7z
20: 		 M119.9,11.8c-0.2,3.6,1.4,7.3,6.5,7.3c5.1,0,7.3-3.8,7.7-7.4c0.4-3.6-1.3-7.8-6.4-7.8S120.1,8.1,119.9,11.8z"/>
21: 	<polygon class="st0" points="156.2,0.7 160.3,0.7 158.4,22.4 155.9,22.4 155.9,22.4 145.8,7.8 144.5,22.4 140.5,22.4 142.3,0.8 
22: 		145.6,0.8 155.1,14.2 	"/>
23: 	<path class="st0" d="M53.6,48.9H42.3L40.1,53h-4.4l11.6-21.7h4.4L59.5,53H55L53.6,48.9z M49,35.9l-4.8,9.2h8L49,35.9z"/>
24: 	<polygon class="st0" points="67.6,31.3 66,49.2 77.1,49.2 76.8,53 61.6,53 63.5,31.3 	"/>
25: 	<path class="st0" d="M95.8,53H79.6c0.6-7.2,1.3-14.5,1.9-21.7h16.2l-0.3,4H85.2l-0.4,5h11.7l-0.3,3.8H84.4L84,49h12.1L95.8,53z"/>
26: 	<path class="st0" d="M118.1,53h-4.8l-5.7-7.2h-3.9L103,53h-4l1.9-21.7c3.4,0,6.8,0,10.3,0c5.1,0,7.5,3.4,7.2,7.2
27: 		c-0.1,3.4-2.7,6.3-6.1,6.8l5.9,7.4L118.1,53z M104.6,35.1l-0.6,6.9h6.2c1,0.1,2-0.3,2.7-0.9c0.8-0.7,1.2-1.6,1.3-2.6
28: 		c0.1-0.9-0.2-1.9-0.8-2.6c-0.7-0.7-1.6-1-2.6-0.9H104.6z"/>
29: 	<polygon class="st0" points="127.9,35 121,35 121.3,31.3 139.1,31.3 138.8,35 131.9,35 130.4,53 126.3,53 	"/>
30: 	<path class="st0" d="M154.5,36.5c-0.6-1.2-2.6-2.4-4.9-2.4c-3,0-4.6,1.3-4.7,2.9c-0.2,1.9,2,2.4,4.6,2.7c4.5,0.6,8.6,1.7,8.1,6.9
31: 		c-0.4,4.8-4.9,6.9-9.7,6.9c-4.4,0-7.7-1.4-9-5.3l3.6-1.8c0.8,2.4,3.2,3.4,5.8,3.4c2.6,0,5.1-0.9,5.2-3.2c0.2-2-1.9-2.9-4.7-3.2
32: 		c-4.4-0.5-8.3-1.7-7.9-6.6c0.4-4.5,4.9-6.3,8.9-6.3c3.4,0,6.8,1,8.1,4.3L154.5,36.5z"/>
33: </g>
34: <g id="Alert" transform="translate(166.000000, 0.000000)">
35: 
36: 		<linearGradient id="D_1_" gradientUnits="userSpaceOnUse" x1="-341.5981" y1="456.1763" x2="-342.3327" y2="455.1763" gradientTransform="matrix(68.4058 0 0 -79.8102 23421.9238 36402.6836)">
37: 		<stop  offset="0" style="stop-color:#F59C07"/>
38: 		<stop  offset="1" style="stop-color:#F57507"/>
39: 	</linearGradient>
40: 	<path id="D" class="st1" d="M68.6,17.7L54.4,1.2C53.7,0.4,52.8,0,51.8,0H9.4C7.6,0,6.2,1.3,6,3L0.9,61c-0.1,0.9,0.2,1.9,0.9,2.6
41: 		s1.5,1.1,2.5,1.1h8.3l-1.3,15.1l16.4-15.1h18.6c0.9,0,1.7-0.3,2.3-1l17.5-17c0.6-0.6,0.9-1.3,1-2.1l2.1-24.5
42: 		C69.4,19.3,69.1,18.4,68.6,17.7z M55.6,40c-0.1,0.8-0.4,1.6-1,2.1l-10.1,9.7c-0.6,0.6-1.5,0.9-2.3,0.9H17.4c-1.5,0-2.8-1-3.2-2.4
43: 		C14,49.9,14,49.5,14,49.1l3-34c0.1-1.7,1.6-3.1,3.3-3.1h25.2c1,0,1.9,0.4,2.5,1.1l8,9.2c0.6,0.7,0.9,1.6,0.8,2.5L55.6,40z
44: 		 M35.8,46.5h-4.9c-0.3,0-0.6-0.1-0.7-0.3s-0.3-0.5-0.3-0.8l0.4-4.9c0-0.5,0.5-0.9,1-0.9h4.9c0.3,0,0.6,0.1,0.7,0.3s0.3,0.5,0.3,0.8
45: 		l-0.4,4.9C36.8,46.1,36.3,46.5,35.8,46.5L35.8,46.5z M36.7,37.2h-5c-0.6,0-1-0.4-1-1L32,20.7c0.1-0.5,0.5-0.9,1-0.9h5
46: 		c0.6,0,1,0.4,1,1l-1.4,15.5C37.6,36.8,37.2,37.2,36.7,37.2z"/>
47: </g>
48: </svg>
```

## File: CSS/auto-cleaner.css
```css
  1: @import url('https://fonts.googleapis.com/css2?family=Shantell+Sans:ital,wght@0,300..800;1,300..800&family=Tiny5&display=swap');
  2: 
  3: :root {
  4:     /* Text - Fonts */
  5:     --aw-font-family-primary: "Shantell Sans", serif;
  6:     --aw-font-family-secondary: "Tiny5", sans-serif;
  7:     --aw-color-text-primary: #f0f8ff;
  8:     --aw-text-size: 14px;
  9: 
 10:     /* Container */
 11:     --aw-container-bg: #232323;
 12:     --aw-container-border: 2px solid rgba(0, 0, 0, 0.4);
 13: 
 14:     /* Inputs */
 15:     --aw-input-bg: #1f1f1f;
 16:     --aw-input-border: 1px solid #262626;
 17:     --aw-input-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);
 18: 
 19:     /* Buttons */
 20:     --aw-button-gradient: radial-gradient(circle at top left, purple 10%, violet 90%);
 21:     --aw-button-execute-hover: radial-gradient(circle at top left, purple 10%, #93ac47 90%);
 22:     --aw-button-hide-hover: radial-gradient(circle at top left, purple 10%, #fc3468 90%);
 23: }
 24: 
 25: 
 26: /* General Styles */
 27: 
 28: hr {
 29:     border-color: grey;
 30:     background-color: grey;
 31:     opacity: 0.25;
 32: }
 33: 
 34: .instruction {
 35:     font-size: 18px;
 36:     color: grey;
 37:     user-select: none;
 38:     cursor: default;
 39: }
 40: 
 41: 
 42: /* Special fixes for IpyWidgets */
 43: /* Fix Vertical Centering */
 44: .widget-hbox,
 45: .jupyter-widgets label {
 46:     display: flex;
 47:     align-items: center;
 48: }
 49: 
 50: 
 51: /* Text FONTs */
 52: 
 53: .instruction,
 54: .custom_select_multiple select,
 55: .output_message,
 56: .storage_info,
 57: .cleaner_button {
 58:     font-family: var(--aw-font-family-primary);
 59:     font-optical-sizing: auto;
 60: }
 61: 
 62: 
 63: /* Container style */
 64: 
 65: .cleaner_container {
 66:     position: relative;
 67:     padding: 10px 15px;
 68:     margin: 5px 0 0 5px;
 69:     background-color: var(--aw-container-bg);
 70:     border: var(--aw-container-border);
 71:     border-radius: 16px;
 72:     box-shadow: 0 0 15px rgba(0, 0, 0, 0.35), inset 0 0 10px rgba(0, 0, 0, 0.3);
 73:     overflow: hidden;
 74: }
 75: .cleaner_container::before {
 76:     position: absolute;
 77:     top: 5px;
 78:     right: 10px;
 79:     content: "AutoCleaner";
 80:     font-family: var(--aw-font-family-secondary);
 81:     font-optical-sizing: auto;
 82:     font-weight: 750;
 83:     font-size: 24px;
 84:     color: rgba(0, 0, 0, 0.3);
 85: }
 86: .cleaner_container::after {
 87:     position: absolute;
 88:     top: 30px;
 89:     right: 10px;
 90:     content: "ANXETY";
 91:     font-family: var(--aw-font-family-secondary);
 92:     font-optical-sizing: auto;
 93:     font-weight: 750;
 94:     font-size: 18px;
 95:     color: rgba(0, 0, 0, 0.3);
 96: }
 97: 
 98: 
 99: /* Input-Output field styles */
100: 
101: .custom_select_multiple select {
102:     padding: 10px;
103:     border: var(--aw-input-border) !important;
104:     border-radius: 10px;
105:     color: var(--aw-color-text-primary);
106:     background-color: var(--aw-input-bg);
107:     box-shadow: var(--aw-input-shadow);
108: }
109: 
110: .output_panel {
111:     padding: 10px;
112:     border: var(--aw-input-border);
113:     border-radius: 10px;
114:     background-color: var(--aw-input-bg);
115:     box-shadow: var(--aw-input-shadow);
116: }
117: .output_message {
118:     color: var(--aw-color-text-primary);
119:     font-size: var(--aw-text-size);
120:     user-select: none;
121:     cursor: default;
122: }
123: 
124: .storage_info {
125:     padding: 5px 20px;
126:     border: var(--aw-input-border);
127:     border-radius: 10px;
128:     background-color: var(--aw-input-bg);
129:     box-shadow: var(--aw-input-shadow);
130:     font-size: var(--aw-text-size);
131:     user-select: none;
132:     cursor: default;
133: }
134: 
135: /* Layout for selection and output areas */
136: .selection_output_layout {
137:     display: flex;
138:     justify-content: space-between;
139:     gap: 5px;
140:     align-items: stretch;
141: }
142: 
143: .custom_select_multiple,
144: .output_panel {
145:     flex: 1;
146:     box-sizing: border-box;
147:     margin: 0;
148: }
149: 
150: 
151: /* Button and storage info layout */
152: .lower_information_panel {
153:     justify-content: space-between;
154: }
155: 
156: 
157: /* Button style */
158: 
159: .cleaner_button {
160:     width: auto;
161:     color: var(--aw-color-text-primary);
162:     font-size: var(--aw-text-size);
163:     height: 35px;
164:     border-radius: 15px;
165:     background-image: var(--aw-button-gradient);
166:     background-size: 200% 200%;
167:     background-position: left bottom;
168:     transition: background 0.5s ease, transform 0.3s ease;
169: }
170: .cleaner_button:hover {
171:     cursor: pointer;
172:     background-size: 200% 200%;
173:     background-position: right bottom;
174:     transform: translateY(1px);
175: }
176: 
177: .button_execute:hover {
178:     background-image: var(--aw-button-execute-hover);
179: }
180: .button_hide:hover {
181:     background-image: var(--aw-button-hide-hover);
182: }
183: 
184: /* Removes ugly stroke from widget buttons. */
185: .cleaner_button:active {
186:     filter: brightness(0.75) !important;
187: }
188: .jupyter-widgets.lm-Widget:focus {
189:     outline: none;
190: }
191: 
192: 
193: /* Animation of elements */
194: 
195: .cleaner_container {
196:     animation: slideInTopBlur 0.7s forwards;
197: }
198: .animated_message {
199:     animation: fadeIn 0.5s forwards;
200: }
201: 
202: @keyframes fadeIn {
203:     from {
204:         opacity: 0;
205:         transform: translateY(-10px);
206:     }
207:     to {
208:         opacity: 1;
209:         transform: translateY(0);
210:     }
211: }
212: 
213: @keyframes slideInTopBlur {
214:     0% {
215:         transform: translate3d(0, 50%, 0) scale(0.85) rotate3d(1, 0, 0, -85deg);
216:         filter: blur(5px) grayscale(1) brightness(0.5);
217:         opacity: 0;
218:     }
219:     100% {
220:         transform: translate3d(0, 0, 0) scale(1) rotate3d(1, 0, 0, 0deg);
221:         filter: blur(0) grayscale(0) brightness(1);
222:         opacity: 1;
223:     }
224: }
225: 
226: /* Leaving animation */
227: .cleaner_container.hide {
228:     animation: slideOutTopBlur 0.3s forwards;
229: }
230: 
231: @keyframes slideOutTopBlur {
232:     0% {
233:         transform: translate3d(0, 0, 0) scale(1);
234:         filter: blur(0) grayscale(0) brightness(1);
235:         opacity: 1;
236:     }
237:     100% {
238:         transform: translate3d(0, -100%, 0);
239:         filter: blur(5px) grayscale(1) brightness(0);
240:         opacity: 0;
241:     }
242: }
```

## File: CSS/download-result.css
```css
  1: @import url('https://fonts.googleapis.com/css2?family=Shantell+Sans:ital,wght@0,300..800;1,300..800&family=Tiny5&display=swap');
  2: 
  3: :root {
  4:     /* Accent Color */
  5:     --aw-accent-color: #ac8fa5;
  6: 
  7:     /* Text / Fonts */
  8:     --aw-font-family-primary: "Shantell Sans", serif;
  9:     --aw-font-family-secondary: "Tiny5", sans-serif;
 10:     --aw-color-text-primary: #f0f8ff;
 11:     --aw-text-size: 14px;
 12: 
 13:     /* Container */
 14:     --aw-container-bg: #232323;
 15:     --aw-container-border: 2px solid rgba(0, 0, 0, 0.4);
 16:     --aw-output-container-bg: #1f1f1f;
 17:     --aw-output-section-bg: #181818;
 18:     --aw-output-section-border: 2px solid rgba(0, 0, 0, 0.35);
 19: }
 20: 
 21: 
 22: /* Text FONTs */
 23: 
 24: .widget-html,
 25: .header-main-title,
 26: .section-title {
 27:     font-family: var(--aw-font-family-primary);
 28:     font-optical-sizing: auto;
 29: }
 30: 
 31: 
 32: /* Element text style */
 33: 
 34: .widget-html {
 35:     font-size: var(--aw-text-size);
 36:     color: var(--aw-color-text-primary) !important;
 37:     user-select: none;
 38: }
 39: 
 40: 
 41: /* General Styles */
 42: 
 43: .header-main-title,
 44: .section-title {
 45:     font-size: 20px;
 46:     font-weight: bold;
 47:     text-align: center;
 48: }
 49: .header-main-title {
 50:     color: var(--aw-accent-color);
 51:     text-align: center;
 52:     margin-bottom: 15px;
 53: }
 54: .section-title {
 55:     color: #0083c0;
 56: }
 57: 
 58: .divider-line {
 59:     border-color: grey;
 60:     background-color: grey;
 61:     opacity: 0.25;
 62:     width: 1000px;
 63: }
 64: 
 65: 
 66: /* Container style */
 67: 
 68: .result-container {
 69:     position: relative;
 70:     flex-direction: column;
 71:     align-items: center;
 72:     padding: 15px;
 73:     margin: 40px 10px 10px 10px;
 74:     background-color: var(--aw-container-bg);
 75:     border: var(--aw-container-border);
 76:     border-radius: 16px;
 77:     box-shadow: 0 0 15px rgba(0, 0, 0, 0.35), inset 0 0 10px rgba(0, 0, 0, 0.3);
 78:     overflow: hidden;
 79: }
 80: .result-container::after {
 81:     position: absolute;
 82:     top: 5px;
 83:     right: 10px;
 84:     content: "ANXETY";
 85:     font-family: var(--aw-font-family-secondary);
 86:     font-optical-sizing: auto;
 87:     font-weight: 750;
 88:     font-size: 24px;
 89:     color: rgba(0, 0, 0, 0.3);
 90: }
 91: 
 92: .result-output-container {
 93:     display: flex;
 94:     flex-wrap: wrap;
 95:     align-items: stretch;
 96:     width: 95%;
 97:     height: 100%;
 98:     box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3);
 99:     background-color: var(--aw-output-container-bg);
100:     border-radius: 8px;
101:     padding: 25px;
102:     gap: 16px;
103:     overflow: visible;
104: }
105: .output-section {
106:     flex: 1 1 auto;
107:     min-width: min-content;
108:     max-height: 100%;
109:     background-color: var(--aw-output-section-bg);
110:     padding: 10px 15px;
111:     border-radius: 16px;
112:     border: var(--aw-output-section-border);
113:     box-shadow: 0 0 8px rgba(0, 0, 0, 0.3), inset 0 0 10px rgba(0, 0, 0, 0.3);
114:     transition: all 0.15s;
115: }
116: /* good use of space */
117: ._horizontal {
118:     display: grid;
119:     grid-template-columns: repeat(3, 1fr);
120: }
121: 
122: 
123: /* Animation of elements */
124: 
125: .result-container,
126: .output-section {
127:     animation: showedResult 1s cubic-bezier(0.785, 0.135, 0.15, 0.86);
128: }
129: .output-item {
130:     animation: showedText 1s cubic-bezier(0.785, 0.135, 0.15, 0.86);
131: }
132: 
133: @keyframes showedResult {
134:     0% {
135:         transform: translate3d(0, 15%, 0);
136:         opacity: 0;
137:     }
138:     100% {
139:         transform: translate3d(0, 0, 0);
140:         opacity: 1;
141:     }
142: }
143: 
144: @keyframes showedText {
145:     0% {
146:         transform: translate3d(-30%, 0, 0);
147:         opacity: 0;
148:     }
149:     100% {
150:         transform: translate3d(0, 0, 0);
151:         opacity: 1;
152:     }
153: }
```

## File: CSS/main-widgets.css
```css
  1: @import url('https://fonts.googleapis.com/css2?family=Shantell+Sans:ital,wght@0,300..800;1,300..800&family=Tiny5&display=swap');
  2: 
  3: :root {
  4:     /* Accent Color */
  5:     --aw-accent-color: #ff97ef;
  6: 
  7:     /* Text - Fonts */
  8:     --aw-font-family-primary: "Shantell Sans", serif;
  9:     --aw-font-family-secondary: "Tiny5", sans-serif;
 10:     --aw-color-text-primary: #f0f8ff;
 11:     --aw-text-size: 14px;
 12:     --aw-text-size-small: 13px;
 13: 
 14:     /* Container */
 15:     --aw-container-bg: #232323;
 16:     --aw-container-border: 2px solid rgba(0, 0, 0, 0.4);
 17: 
 18:     /* Inputs */
 19:     --aw-input-bg: #1c1c1c;
 20:     --aw-input-bg-hover: #262626;
 21:     --aw-input-border: 1px solid #262626;
 22:     --aw-input-border-focus: #006ee5;
 23: 
 24:     /* Checkboxes */
 25:     --aw-checkbox-unchecked-bg: #20b2aa;
 26:     --aw-checkbox-checked-bg: #2196f3;
 27:     --aw-checkbox-inpaint-bg: #bbca53;
 28:     --aw-checkbox-sdxl-bg: #ea861a;
 29:     --aw-checkbox-empowerment-bg: #df6b91;
 30:     --aw-checkbox-handle-bg: white;
 31: 
 32:     /* Popup */
 33:     --aw-popup-bg: rgba(255, 255, 255, 0.05);
 34:     --aw-popup-color: #ffffff;
 35:     --aw-popup-border: 2px solid rgba(255, 255, 255, 0.45);
 36:     --aw-popup-sample-bg: rgba(255, 255, 255, 0.2);
 37:     --aw-popup-sample-color: #c6e2ff;
 38:     --aw-popup-sample-border: 2px solid rgba(255, 255, 255, 0.2);
 39: 
 40:     /* Term Colors (Popup) */
 41:     --aw-term-sample-label: #dbafff;
 42:     --aw-term-braces: #ffff00;
 43:     --aw-term-extension: #eb934b;
 44:     --aw-term-filename: #ffdba7;
 45:     --aw-term-required: #ff9999;
 46: 
 47:     /* Scrollbar */
 48:     --aw-scrollbar-width: 0.65rem;
 49:     --aw-scrollbar-thumb-bg: #475254;
 50:     --aw-scrollbar-track-bg: #111111;
 51:     --aw-scrollbar-thumb-hover: var(--aw-accent-color);
 52: 
 53:     /* Buttons */
 54:     --aw-button-gradient: radial-gradient(circle at top left, purple 10%, violet 90%);
 55:     --aw-button-input-gradient: radial-gradient(circle at top left, var(--aw-input-bg));
 56:     --aw-button-save-hover: radial-gradient(circle at top left, purple 10%, #93ac47 90%);
 57:     --aw-button-api-hover: radial-gradient(circle at top left, purple 10%, #1d94bb 90%);
 58: }
 59: 
 60: 
 61: /* General Styles */
 62: 
 63: .header {
 64:     display: inline-block;
 65:     font-size: 20px;
 66:     font-weight: 650;
 67:     color: var(--aw-accent-color);
 68:     margin-bottom: 10px;
 69:     user-select: none;
 70:     cursor: default;
 71:     text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
 72: }
 73: 
 74: hr {
 75:     margin: 4px 0;
 76:     background-color: grey;
 77:     border-color: grey;
 78:     opacity: 0.25;
 79: }
 80: a {
 81:     color: inherit;
 82:     text-decoration: none;
 83: }
 84: 
 85: 
 86: /* == Special fixes for IpyWidgets == */
 87: /* Remove Shit-Spacing for HTML-Widgets (button) */
 88: .widget-html:has(.button),
 89: .widget-html-content:has(.button) {
 90:     padding: 0;
 91:     margin: 0;
 92: }
 93: 
 94: /* Fix Vertical Centering */
 95: .widget-hbox,
 96: .jupyter-widgets label {
 97:     display: flex;
 98:     align-items: center;
 99: }
100: 
101: /* Fix Checkbox Width */
102: .widget-checkbox {
103:     width: auto;
104:     display: inline-flex;
105:     min-width: unset;
106: }
107: 
108: 
109: /* Special Styles (ScrollBars) */
110: 
111: ::selection {
112:     background: #3d4142;
113: }
114: ::-moz-selection { /* Code for Firefox */
115:     background: #3d4142;
116: }
117: 
118: /* === ScrollBar (For TextArea) === */
119: .widget-textarea textarea::-webkit-scrollbar {
120:     width: var(--aw-scrollbar-width);
121:     height: var(--aw-scrollbar-width);
122: }
123: .widget-textarea textarea::-webkit-scrollbar-thumb {
124:     background: var(--aw-scrollbar-thumb-bg) !important;
125:     border: 3px solid var(--aw-scrollbar-track-bg);
126:     border-radius: 16px;
127: }
128: .widget-textarea textarea::-webkit-scrollbar-thumb:hover {
129:     background: var(--aw-scrollbar-thumb-hover) !important;
130: }
131: .widget-textarea textarea::-webkit-scrollbar-track,
132: .widget-textarea textarea::-webkit-scrollbar-corner {
133:     background: var(--aw-scrollbar-track-bg) !important;
134:     border-radius: 0 8px 8px 0;
135: }
136: /* FireFox Styles */
137: @-moz-document url-prefix() {
138:     .widget-textarea textarea {
139:         scrollbar-width: auto;
140:         scrollbar-color: var(--aw-scrollbar-thumb-bg) var(--aw-scrollbar-track-bg);
141:     }
142: }
143: 
144: 
145: /* Text FONTs */
146: 
147: .info,
148: .popup,
149: .button,
150: .header,
151: .widget-button,
152: .widget-text label,
153: .widget-checkbox label,
154: .widget-dropdown label,
155: .widget-dropdown select,
156: .widget-textarea textarea,
157: .widget-text input[type="text"] {
158:     font-family: var(--aw-font-family-primary);
159:     font-optical-sizing: auto;
160: }
161: 
162: 
163: /* Element text style */
164: 
165: .widget-text,
166: .widget-button,
167: .widget-text label,
168: .widget-checkbox label,
169: .widget-dropdown label,
170: .widget-dropdown select,
171: .widget-textarea textarea,
172: .widget-text input[type="text"] {
173:     font-style: normal;
174:     font-size: var(--aw-text-size);
175:     color: var(--aw-color-text-primary) !important;
176:     user-select: none;
177: }
178: .widget-text input[type="text"]::placeholder {
179:     color: grey;
180:     font-size: var(--aw-text-size);
181: }
182: 
183: /* TextArea */
184: .widget-textarea textarea,
185: .widget-textarea textarea::placeholder {
186:     font-size: var(--aw-text-size-small);
187: }
188: 
189: 
190: /* Container style */
191: 
192: .mainContainer * { /* Fix For Containers Shadow */
193:     overflow: visible !important;
194: }
195: .mainContainer {
196:     padding: 5px;
197:     gap: 5px;
198: }
199: 
200: .container {
201:     position: relative;
202:     width: 1080px;
203:     padding: 10px 15px;
204:     background-color: var(--aw-container-bg);
205:     border: var(--aw-container-border);
206:     border-radius: 16px;
207:     box-shadow: 0 0 15px rgba(0, 0, 0, 0.35), inset 0 0 10px rgba(0, 0, 0, 0.3);
208:     overflow: hidden !important;
209: }
210: .container::after {
211:     content: "ANXETY";
212:     position: absolute;
213:     top: 5px;
214:     right: 10px;
215:     color: rgba(0, 0, 0, 0.3);
216:     font-family: var(--aw-font-family-secondary);
217:     font-optical-sizing: auto;
218:     font-weight: 750;
219:     font-size: 24px;
220: }
221: 
222: .container_cdl {
223:     height: 55px;
224:     transition: all 0.5s cubic-bezier(0.785, 0.135, 0.15, 0.85);
225: }
226: .container_cdl.expanded {
227:     height: 305px;
228: }
229: 
230: /* GDrive Button */
231: .gdrive-btn {
232:     align-self: flex-start;
233:     min-width: 48px;
234:     min-height: 48px;
235:     margin: 0 !important;
236:     margin-left: 15px !important; /* SPACE */
237:     padding: 0 !important;
238:     background-size: 70%;
239:     background-position: center;
240:     background-repeat: no-repeat;
241:     background-image: url('https://upload.wikimedia.org/wikipedia/commons/1/12/Google_Drive_icon_%282020%29.svg');
242:     background-color: var(--aw-container-bg);
243:     border: var(--aw-container-border);
244:     border-radius: 8px;
245:     box-shadow: 0 0 15px rgba(0, 0, 0, 0.35), inset 0 0 10px rgba(0, 0, 0, 0.3) !important;
246:     cursor: pointer;
247:     outline: none;
248:     transition: all 0.15s ease;
249: }
250: .gdrive-btn.active {
251:     background-color: #006d33;
252:     border-color: #00d062;
253:     transform: scale(0.9) !important;
254: }
255: 
256: 
257: /* Input field styles */
258: 
259: .widget-dropdown select,
260: .widget-text input[type="text"],
261: .widget-textarea textarea {
262:     height: 30px;
263:     margin: 0 !important;
264:     background-color: var(--aw-input-bg);
265:     border: var(--aw-input-border);
266:     border-radius: 10px;
267:     box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);
268:     transition: all 0.25s ease-in-out;
269: }
270: .widget-textarea textarea {
271:     height: 200px;
272:     resize: none;
273: }
274: 
275: .widget-dropdown select:focus,
276: .widget-text input[type="text"]:focus,
277: .widget-textarea textarea:focus {
278:     border-color: var(--aw-input-border-focus);
279: }
280: 
281: .widget-dropdown select:hover,
282: .widget-text input[type="text"]:hover {
283:     transform: scale(1.003);
284:     background-color: var(--aw-input-bg-hover);
285:     box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
286: }
287: .widget-dropdown option {
288:     background-color: var(--aw-input-bg);
289: }
290: 
291: /* Animation when switching empowerment mode */
292: .widget-text.empowerment-text-field,
293: .widget-textarea.empowerment-output  {
294:     transition: all 0.3s ease;
295:     overflow: hidden;
296: }
297: /* Standard state */
298: .widget-text.empowerment-text-field {
299:     opacity: 1;
300:     max-height: 30px;
301:     visibility: visible;
302: }
303: .widget-textarea.empowerment-output {
304:     opacity: 1;
305:     max-height: 200px;
306:     visibility: visible;
307: }
308: /* Hidden state */
309: .widget-text.empowerment-text-field.hidden,
310: .widget-textarea.empowerment-output.hidden {
311:     opacity: 0;
312:     max-height: 0;
313:     margin-top: 0;
314:     margin-bottom: 0;
315:     visibility: hidden;
316: }
317: 
318: 
319: /* Slider Checkbox style */
320: 
321: .widget-checkbox input[type="checkbox"] {
322:     appearance: none;
323:     position: relative;
324:     width: 40px;
325:     height: 20px;
326:     background-color: var(--aw-checkbox-unchecked-bg);
327:     border: none;
328:     border-radius: 10px;
329:     cursor: pointer;
330:     box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3);
331:     transition: background-color 0.3s cubic-bezier(0.785, 0.135, 0.15, 0.85);
332: }
333: .widget-checkbox input[type="checkbox"]:checked {
334:     background-color: var(--aw-checkbox-checked-bg);
335: }
336: .inpaint input[type="checkbox"]:checked {
337:     background-color: var(--aw-checkbox-inpaint-bg);
338: }
339: .sdxl input[type="checkbox"]:checked {
340:     background-color: var(--aw-checkbox-sdxl-bg);
341: }
342: .empowerment input[type="checkbox"]:checked {
343:     background-color: var(--aw-checkbox-empowerment-bg);
344: }
345: 
346: .widget-checkbox input[type="checkbox"]:before {
347:     content: '';
348:     position: absolute;
349:     top: 50%;
350:     left: 4px;
351:     width: 12px;
352:     height: 12px;
353:     background-color: var(--aw-checkbox-handle-bg);
354:     border-radius: inherit;
355:     box-shadow: 0 0 8px rgba(0, 0, 0, 0.3);
356:     transform: translateY(-50%);
357:     transition: all 0.25s cubic-bezier(0.785, 0.135, 0.15, 0.85);
358: }
359: .widget-checkbox input[type="checkbox"]:checked:before {
360:     left: 20px;
361:     width: 16px;
362:     height: 16px;
363: }
364: 
365: 
366: /* Popup style of `INFO` window */
367: 
368: .info {
369:     position: absolute;
370:     display: inline-block;
371:     top: -5px;
372:     right: 90px;
373:     color: grey;
374:     font-size: var(--aw-text-size);
375:     opacity: 0;
376:     transition: all 0.25s;
377:     user-select: none;
378: }
379: 
380: .popup {
381:     position: absolute;
382:     top: 120px;
383:     padding: 12px;
384:     color: var(--aw-popup-color);
385:     font-size: 16px;
386:     text-align: center;
387:     background-color: var(--aw-popup-bg);
388:     backdrop-filter: blur(8px);
389:     border: var(--aw-popup-border);
390:     border-radius: 10px;
391:     box-shadow: 0 0 50px rgba(0, 0, 0, 0.5);
392:     opacity: 0;
393:     transform: rotate(-5deg);
394:     pointer-events: none;
395:     z-index: 999;
396:     transition: all 0.25s cubic-bezier(0.175, 0.885, 0.30, 1.275);
397: }
398: 
399: .sample {
400:     margin-top: 25px;
401:     padding: 10px 100px;
402:     color: var(--aw-popup-sample-color);
403:     background-color: var(--aw-popup-sample-bg);
404:     border: var(--aw-popup-sample-border);
405:     border-radius: 10px;
406:     white-space: nowrap;
407: }
408: 
409: /* For Empowerment */
410: .empowerment {
411:     position: absolute;
412:     top: 10px;
413:     left: 300px;
414:     opacity: 0;
415:     pointer-events: none;
416:     transition: all 0.25s;
417: }
418: 
419: .info.showed,
420: .empowerment.showed {
421:     opacity: 1;
422:     pointer-events: auto;
423: }
424: 
425: .info.showed:hover + .popup {
426:     top: 35px;
427:     opacity: 1;
428:     transform: rotate(0deg);
429: }
430: 
431: /* Term Colors */
432: .sample_label { color: var(--aw-term-sample-label); }
433: .braces { color: var(--aw-term-braces); }
434: .extension { color: var(--aw-term-extension); }
435: .file_name { color: var(--aw-term-filename); }
436: .required { color: var(--aw-term-required); }
437: 
438: 
439: /* Button styles */
440: 
441: .button {
442:     margin: 0;
443:     color: var(--aw-color-text-primary);
444:     font-size: 15px;
445:     box-sizing: border-box !important;
446:     white-space: nowrap;
447:     cursor: pointer;
448:     user-select: none;
449:     overflow: hidden !important;
450:     transition: background 0.5s ease;
451: }
452: .button_save {
453:     font-weight: 650;
454:     width: 120px;
455:     height: 35px;
456:     background-image: var(--aw-button-gradient);
457:     background-size: 200% 100%;
458:     background-position: left bottom;
459:     border-radius: 15px;
460: }
461: .button_api {
462:     position: relative;
463:     font-size: 12px;
464:     display: inline-flex;
465:     align-items: center;
466:     justify-content: center;
467:     height: 30px !important;
468:     min-width: 45px;
469:     margin-left: 4px; /* SPACE */
470:     padding: 0;
471:     background-image: var(--aw-button-input-gradient);
472:     background-size: 200% 100%;
473:     background-position: left bottom;
474:     border: var(--aw-input-border);
475:     border-radius: 10px;
476:     box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);
477:     transition: all 0.4s ease;
478: }
479: .button_api .icon {
480:     position: absolute;
481:     left: 50%;
482:     transform: translateX(-50%);
483:     transition: all 0.4s ease;
484:     pointer-events: none;
485: }
486: .button_api .text {
487:     display: inline-block;
488:     max-width: 0;
489:     opacity: 0;
490:     pointer-events: none;
491:     transition: all 0.4s ease;
492: }
493: 
494: .button:hover {
495:     background-position: right bottom;
496: }
497: .button_save:hover {
498:     background-image: var(--aw-button-save-hover);
499: }
500: .button_api:hover {
501:     max-width: 300px;
502:     padding: 0 12px 0 32px;
503:     background-image: var(--aw-button-api-hover);
504: }
505: .button_api:hover .icon {
506:     left: 15px;
507:     transform: translateX(0);
508: }
509: .button_api:hover .text {
510:     max-width: 200px;
511:     padding-left: 6px;
512:     opacity: 1;
513: }
514: 
515: /* Removes ugly stroke from widget buttons. */
516: .button:active {
517:     filter: brightness(0.75) !important;
518: }
519: .jupyter-widgets.lm-Widget:focus {
520:     outline: none;
521: }
522: 
523: 
524: /* Animation of elements */
525: 
526: .container,
527: .gdrive-btn,
528: .button_save {
529:     animation: showedWidgets 0.8s forwards ease;
530: }
531: 
532: .container.hide,
533: .gdrive-btn.hide,
534: .button_save.hide {
535:     animation: hideWidgets 0.5s forwards ease;
536: }
537: 
538: @keyframes showedWidgets {
539:     0% {
540:         transform: translate3d(-65%, 15%, 0) scale(0) rotate(15deg);
541:         filter: blur(25px) brightness(0.3);
542:         opacity: 0;
543:     }
544:     100% {
545:         transform: translate3d(0, 0, 0) scale(1) rotate(0deg);
546:         filter: blur(0) brightness(1);
547:         opacity: 1;
548:     }
549: }
550: 
551: @keyframes hideWidgets {
552:     0% {
553:         transform: translate3d(0, 0, 0) scale(1) rotate3d(1, 0, 0, 0deg);
554:         filter: blur(0) brightness(1);
555:         opacity: 1;
556:     }
557:     100% {
558:         transform: translate3d(0, 5%, 0) scale(0.9) rotate3d(1, 0, 0, 90deg);
559:         filter: blur(15px) brightness(0.5);
560:         opacity: 0;
561:     }
562: }
```

## File: JS/main-widgets.js
```javascript
1: function toggleContainer() {
2:     const downloadContainer = document.querySelector('.container_cdl');
3:     const info = document.querySelector('.info');
4:     const emp = document.querySelector('.empowerment');
5: 
6:     downloadContainer.classList.toggle('expanded');
7:     info.classList.toggle('showed');
8:     emp.classList.toggle('showed');
9: }
```

## File: modules/__season.py
```python
  1: from IPython.display import display, HTML
  2: import datetime
  3: import argparse
  4: 
  5: TRANSLATIONS = {
  6:     'en': {
  7:         'done_message': "Done! Now you can run the cells below. ☄️",
  8:         'runtime_env': "Runtime environment:",
  9:         'file_location': "File location:",
 10:         'current_fork': "Current fork:",
 11:         'current_branch': "Current branch:"
 12:     },
 13:     'ru': {
 14:         'done_message': "Готово! Теперь вы можете выполнить ячейки ниже. ☄️",
 15:         'runtime_env': "Среда выполнения:",
 16:         'file_location': "Расположение файлов:",
 17:         'current_fork': "Текущий форк:",
 18:         'current_branch': "Текущая ветка:"
 19:     }
 20: }
 21: 
 22: def get_season():
 23:     month = datetime.datetime.now().month
 24:     if month in [12, 1, 2]:
 25:         return 'winter'
 26:     elif month in [3, 4, 5]:
 27:         return 'spring'
 28:     elif month in [6, 7, 8]:
 29:         return 'summer'
 30:     else:
 31:         return 'autumn'
 32: 
 33: def display_info(env, scr_folder, branch, lang='en', fork=None):
 34:     season = get_season()
 35:     translations = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
 36: 
 37:     season_config = {
 38:         'winter': {
 39:             'bg': 'linear-gradient(180deg, #66666633, transparent)',
 40:             'primary': '#666666',
 41:             'accent': '#ffffff',
 42:             'icon': '❄️',
 43:             'particle_color': '#ffffff'
 44:         },
 45:         'spring': {
 46:             'bg': 'linear-gradient(180deg, #9366b433, transparent)',
 47:             'primary': '#9366b4',
 48:             'accent': '#dbcce6',
 49:             'icon': '🌸',
 50:             'particle_color': '#ffb3ba'
 51:         },
 52:         'summer': {
 53:             'bg': 'linear-gradient(180deg, #ffe76633, transparent)',
 54:             'primary': '#ffe766',
 55:             'accent': '#fff7cc',
 56:             'icon': '🌴',
 57:             'particle_color': '#ffd700'
 58:         },
 59:         'autumn': {
 60:             'bg': 'linear-gradient(180deg, #ff8f6633, transparent)',
 61:             'primary': '#ff8f66',
 62:             'accent': '#ffd9cc',
 63:             'icon': '🍁',
 64:             'particle_color': '#ff8f66'
 65:         }
 66:     }
 67:     config = season_config.get(season, season_config['winter'])
 68: 
 69:     CONTENT = f"""
 70:     <div class="season-container">
 71:       <div class="text-container">
 72:         <span>{config['icon']}</span>
 73:         <span>A</span><span>N</span><span>X</span><span>E</span><span>T</span><span>Y</span>
 74:         <span>&nbsp;</span>
 75:         <span>S</span><span>D</span><span>-</span><span>W</span><span>E</span><span>B</span><span>U</span><span>I</span>
 76:         <span>&nbsp;</span>
 77:         <span>V</span><span>2</span>
 78:         <span>{config['icon']}</span>
 79:       </div>
 80: 
 81:       <div class="message-container">
 82:         <span>{translations['done_message']}</span>
 83:         <span>{translations['runtime_env']} <span class="env">{env}</span></span>
 84:         <span>{translations['file_location']} <span class="files-location">{scr_folder}</span></span>
 85:         {f"<span>{translations['current_fork']} <span class='fork'>{fork}</span></span>" if fork else ""}
 86:         <span>{translations['current_branch']} <span class="branch">{branch}</span></span>
 87:       </div>
 88:     </div>
 89:     """
 90: 
 91:     STYLE = f"""
 92:     <style>
 93:     @import url('https://fonts.googleapis.com/css2?family=Righteous&display=swap');
 94: 
 95:     .season-container {{
 96:       position: relative;
 97:       margin: 0 10px !important;
 98:       padding: 20px !important;
 99:       border-radius: 15px;
100:       margin: 10px 0;
101:       overflow: hidden;
102:       min-height: 200px;
103:       background: {config['bg']};
104:       border-top: 2px solid {config['primary']};
105:       animation: fadeIn 0.5s ease-in !important;
106:     }}
107: 
108:     @keyframes fadeIn {{
109:       from {{ opacity: 0; }}
110:       to {{ opacity: 1; }}
111:     }}
112: 
113:     .text-container {{
114:       display: flex;
115:       flex-wrap: wrap;
116:       justify-content: center;
117:       align-items: center;
118:       gap: 0.5em;
119:       font-family: 'Righteous', cursive;
120:       margin-bottom: 1em;
121:     }}
122: 
123:     .text-container span {{
124:       font-size: 2.5rem;
125:       color: {config['primary']};
126:       opacity: 0;
127:       transform: translateY(-20px);
128:       filter: blur(4px);
129:       transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
130:     }}
131: 
132:     .text-container.loaded span {{
133:       opacity: 1;
134:       transform: translateY(0);
135:       filter: blur(0);
136:       color: {config['accent']};
137:     }}
138: 
139:     .message-container {{
140:       font-family: 'Righteous', cursive;
141:       text-align: center;
142:       display: flex;
143:       flex-direction: column;
144:       gap: 0.5em;
145:     }}
146: 
147:     .message-container span {{
148:       font-size: 1.2rem;
149:       color: {config['primary']};
150:       opacity: 0;
151:       transform: translateY(20px);
152:       transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
153:     }}
154: 
155:     .message-container.loaded span {{
156:       opacity: 1;
157:       transform: translateY(0);
158:       color: {config['accent']};
159:     }}
160: 
161:     .env {{ color: #FFA500 !important; }}
162:     .files-location {{ color: #FF99C2 !important; }}
163:     .branch {{ color: #16A543 !important; }}
164:     .fork {{ color: #C786D3 !important; }}
165:     </style>
166:     """
167: 
168:     SCRIPT = """
169:     <script>
170:     (function() {
171:       // Text animation
172:       const textContainer = document.querySelector('.text-container');
173:       const messageContainer = document.querySelector('.message-container');
174:       const textSpans = textContainer.querySelectorAll('span');
175:       const messageSpans = messageContainer.querySelectorAll('span');
176: 
177:       textSpans.forEach((span, index) => {
178:         span.style.transitionDelay = `${index * 25}ms`;
179:       });
180: 
181:       messageSpans.forEach((span, index) => {
182:         span.style.transitionDelay = `${index * 50}ms`;
183:       });
184: 
185:       setTimeout(() => {
186:         textContainer.classList.add('loaded');
187:         messageContainer.classList.add('loaded');
188:       }, 250);
189:     })();
190:     </script>
191:     """
192: 
193:     display(HTML(CONTENT + STYLE + SCRIPT))
194: 
195:     # === Season Scripts ===
196: 
197:     ## OLD VER | adaptation needed...
198:     # WINTER_SCRIPT = """
199:     # <script>
200:     # // Function to create snowflakes
201:     # function createSnowflake() {
202:     #   const snowContainer = document.getElementById('snow-container');
203:     #   const snowflake = document.createElement('div');
204:     #   snowflake.className = 'snowflake';
205: 
206:     #   // Set random size
207:     #   const size = Math.random() * 5 + 3; // Size from 3 to 8 pixels
208:     #   snowflake.style.width = size + 'px';
209:     #   snowflake.style.height = size + 'px';
210: 
211:     #   // Position the snowflake within the snow container
212:     #   const containerRect = snowContainer.getBoundingClientRect();
213:     #   snowflake.style.left = Math.random() * (containerRect.width - size) + 'px';
214:     #   snowflake.style.top = -size + 'px'; // Start just above the container
215: 
216:     #   // Set random opacity between 0.1 and 0.5
217:     #   const opacity = Math.random() * 0.4 + 0.1;
218:     #   snowflake.style.opacity = opacity;
219: 
220:     #   // Set random fall duration and angle (up to 25 degrees)
221:     #   const fallDuration = Math.random() * 3 + 2; // Random fall duration (from 2 to 5 seconds)
222:     #   const angle = (Math.random() * 50 - 25) * (Math.PI / 180); // Angle from -25 to 25 degrees
223:     #   const horizontalMovement = Math.sin(angle) * (containerRect.height / 2); // Horizontal shift
224:     #   const verticalMovement = Math.cos(angle) * (containerRect.height + 10); // Vertical shift
225: 
226:     #   snowContainer.appendChild(snowflake); // Append snowflake to snow container
227: 
228:     #   // Animation for falling with horizontal movement
229:     #   snowflake.animate([
230:     #     { transform: `translate(0, 0)`, opacity: 1 },
231:     #     { transform: `translate(${horizontalMovement}px, ${verticalMovement}px)`, opacity: 0 }
232:     #   ], {
233:     #     duration: fallDuration * 1000,
234:     #     easing: 'linear',
235:     #     fill: 'forwards'
236:     #   });
237: 
238:     #   // Also remove the snowflake after falling
239:     #   setTimeout(() => {
240:     #     snowflake.remove();
241:     #   }, fallDuration * 1000);
242:     # }
243:     # setInterval(createSnowflake, 50);
244:     # </script>
245:     # """
246: 
247:     WINTER_SCRIPT = f"""
248:     <script>
249:     (function() {{
250:       const container = document.querySelector('.season-container');
251:       const style = document.createElement('style');
252:       style.innerHTML = `
253:         .snowflake {{
254:           position: absolute;
255:           background: {config['particle_color']};
256:           border-radius: 50%;
257:           filter: blur(1px);
258:           opacity: 0;
259:           animation: snow-fall linear forwards;
260:           pointer-events: none;
261:         }}
262:         @keyframes snow-fall {{
263:           0% {{ opacity: 0; transform: translate(-50%, -50%) scale(0); }}
264:           20% {{ opacity: 0.8; transform: translate(-50%, -50%) scale(1); }}
265:           100% {{ opacity: 0; transform: translate(-50%, 150%) scale(0.5); }}
266:         }}
267:       `;
268:       document.head.appendChild(style);
269: 
270:       let activeParticles = 0;
271:       const maxParticles = 100;
272: 
273:       function createSnowflake() {{
274:         if (activeParticles >= maxParticles) return;
275: 
276:         const snowflake = document.createElement('div');
277:         snowflake.className = 'snowflake';
278:         const size = Math.random() * 5 + 3;
279:         const x = Math.random() * 100;
280:         const duration = Math.random() * 3 + 2;
281: 
282:         snowflake.style.cssText = `
283:           width: ${{size}}px;
284:           height: ${{size}}px;
285:           left: ${{x}}%;
286:           top: ${{Math.random() * 100}}%;
287:           animation: snow-fall ${{duration}}s linear forwards;
288:         `;
289: 
290:         activeParticles++;
291:         snowflake.addEventListener('animationend', () => {{
292:           snowflake.remove();
293:           activeParticles--;
294:         }});
295: 
296:         container.appendChild(snowflake);
297:       }}
298: 
299:       const interval = setInterval(createSnowflake, 50);
300: 
301:       // Cleanup when container is removed
302:       const observer = new MutationObserver(() => {{
303:         if (!document.contains(container)) {{
304:           clearInterval(interval);
305:           observer.disconnect();
306:         }}
307:       }});
308:       observer.observe(document.body, {{ childList: true, subtree: true }});
309:     }})();
310:     </script>
311:     """
312: 
313:     SPRING_SCRIPT = f"""
314:     <script>
315:     (function() {{
316:       const container = document.querySelector('.season-container');
317:       const style = document.createElement('style');
318:       style.innerHTML = `
319:         .petal {{
320:           position: absolute;
321:           width: 8px;
322:           height: 8px;
323:           background: {config['particle_color']};
324:           border-radius: 50% 50% 0 50%;
325:           transform: rotate(45deg);
326:           opacity: 0;
327:           pointer-events: none;
328:           filter: blur(0.5px);
329:         }}
330:         @keyframes spring-fall {{
331:           0% {{ opacity: 0; transform: translate(-50%, -50%) scale(0); }}
332:           20% {{ opacity: 0.8; transform: translate(-50%, -50%) scale(1) rotate(180deg); }}
333:           100% {{ opacity: 0; transform: translate(-50%, 150%) scale(0.5) rotate(360deg); }}
334:         }}
335:       `;
336:       document.head.appendChild(style);
337: 
338:       let activeParticles = 0;
339:       const maxParticles = 40;
340: 
341:       function createPetal() {{
342:         if (activeParticles >= maxParticles) return;
343: 
344:         const petal = document.createElement('div');
345:         petal.className = 'petal';
346:         const startX = Math.random() * 100;
347:         const duration = Math.random() * 3 + 3;
348: 
349:         petal.style.cssText = `
350:           left: ${{startX}}%;
351:           top: ${{Math.random() * 100}}%;
352:           animation: spring-fall ${{duration}}s linear forwards;
353:         `;
354: 
355:         activeParticles++;
356:         petal.addEventListener('animationend', () => {{
357:           petal.remove();
358:           activeParticles--;
359:         }});
360: 
361:         container.appendChild(petal);
362:       }}
363: 
364:       const interval = setInterval(createPetal, 250);
365: 
366:       // Cleanup when container is removed
367:       const observer = new MutationObserver(() => {{
368:         if (!document.contains(container)) {{
369:           clearInterval(interval);
370:           observer.disconnect();
371:         }}
372:       }});
373:       observer.observe(document.body, {{ childList: true, subtree: true }});
374:     }})();
375:     </script>
376:     """
377: 
378:     SUMMER_SCRIPT = f"""
379:     <script>
380:     (function() {{
381:       const container = document.querySelector('.season-container');
382:       const style = document.createElement('style');
383:       style.innerHTML = `
384:         .stick-particle {{
385:           position: absolute;
386:           width: 2px;
387:           height: 15px;
388:           background: {config['particle_color']};
389:           transform-origin: center bottom;
390:           opacity: 0;
391:           pointer-events: none;
392:         }}
393:         @keyframes stick-fall {{
394:           0% {{ opacity: 0; transform: translate(-50%, -50%) rotate(0) scale(0.5); }}
395:           20% {{ opacity: 0.8; transform: translate(-50%, -50%) rotate(0deg) scale(1); }}
396:           100% {{ opacity: 0; transform: translate(-50%, 150%) rotate(180deg) scale(0.5); }}
397:         }}
398:       `;
399:       document.head.appendChild(style);
400: 
401:       let activeParticles = 0;
402:       const maxParticles = 25;
403: 
404:       function createStick() {{
405:         if (activeParticles >= maxParticles) return;
406: 
407:         const stick = document.createElement('div');
408:         stick.className = 'stick-particle';
409:         const startX = Math.random() * 100;
410:         const duration = Math.random() * 4 + 3;
411:         const rotation = (Math.random() - 0.5) * 180;
412: 
413:         stick.style.cssText = `
414:           left: ${{startX}}%;
415:           top: ${{Math.random() * 100}}%;
416:           animation: stick-fall ${{duration}}s linear forwards;
417:           transform: rotate(${{rotation}}deg);
418:         `;
419: 
420:         activeParticles++;
421:         stick.addEventListener('animationend', () => {{
422:           stick.remove();
423:           activeParticles--;
424:         }});
425: 
426:         container.appendChild(stick);
427:       }}
428: 
429:       const interval = setInterval(createStick, 100);
430: 
431:       // Cleanup when container is removed
432:       const observer = new MutationObserver(() => {{
433:         if (!document.contains(container)) {{
434:           clearInterval(interval);
435:           observer.disconnect();
436:         }}
437:       }});
438:       observer.observe(document.body, {{ childList: true, subtree: true }});
439:     }})();
440:     </script>
441:     """
442: 
443:     AUTUMN_SCRIPT = f"""
444:     <script>
445:     (function() {{
446:       const container = document.querySelector('.season-container');
447:       const style = document.createElement('style');
448:       style.innerHTML = `
449:         .leaf {{
450:           position: absolute;
451:           width: 12px;
452:           height: 12px;
453:           background: {config['particle_color']};
454:           clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
455:           opacity: 0;
456:           pointer-events: none;
457:         }}
458:         @keyframes autumn-fall {{
459:           0% {{ opacity: 0; transform: translate(-50%, -50%) rotate(0deg); }}
460:           20% {{ opacity: 0.8; transform: translate(-50%, -50%) rotate(180deg); }}
461:           100% {{ opacity: 0; transform: translate(-50%, 150%) rotate(360deg); }}
462:         }}
463:       `;
464:       document.head.appendChild(style);
465: 
466:       let activeParticles = 0;
467:       const maxParticles = 40;
468: 
469:       function createLeaf() {{
470:         if (activeParticles >= maxParticles) return;
471: 
472:         const leaf = document.createElement('div');
473:         leaf.className = 'leaf';
474:         const startX = Math.random() * 100;
475:         const duration = Math.random() * 3 + 3;
476: 
477:         leaf.style.cssText = `
478:           left: ${{startX}}%;
479:           top: ${{Math.random() * 100}}%;
480:           animation: autumn-fall ${{duration}}s linear forwards;
481:         `;
482: 
483:         activeParticles++;
484:         leaf.addEventListener('animationend', () => {{
485:           leaf.remove();
486:           activeParticles--;
487:         }});
488: 
489:         container.appendChild(leaf);
490:       }}
491: 
492:       const interval = setInterval(createLeaf, 250);
493: 
494:       // Cleanup when container is removed
495:       const observer = new MutationObserver(() => {{
496:         if (!document.contains(container)) {{
497:           clearInterval(interval);
498:           observer.disconnect();
499:         }}
500:       }});
501:       observer.observe(document.body, {{ childList: true, subtree: true }});
502:     }})();
503:     </script>
504:     """
505: 
506:     # Season Scripts
507:     if season == 'winter':
508:         display(HTML(WINTER_SCRIPT))
509:     elif season == 'spring':
510:         display(HTML(SPRING_SCRIPT))
511:     elif season == 'summer':
512:         display(HTML(SUMMER_SCRIPT))
513:     elif season == 'autumn':
514:         display(HTML(AUTUMN_SCRIPT))
515: 
516: if __name__ == "__main__":
517:     parser = argparse.ArgumentParser()
518:     parser.add_argument('env', type=str, help='Runtime environment')
519:     parser.add_argument('scr_folder', type=str, help='Script folder location')
520:     parser.add_argument('branch', type=str, help='Current branch')
521:     parser.add_argument('lang', type=str, help='Language for messages (ru/en)')
522:     parser.add_argument('fork', type=str, help='Current git-fork')
523: 
524:     args = parser.parse_args()
525: 
526:     display_info(
527:         env=args.env,
528:         scr_folder=args.scr_folder,
529:         branch=args.branch,
530:         lang=args.lang,
531:         fork=args.fork
532:     )
```

## File: modules/CivitaiAPI.py
```python
  1: """ CivitAi API Module | by ANXETY """
  2: 
  3: from urllib.parse import urlparse, parse_qs, urlencode
  4: from typing import Optional, Tuple, Dict, Any
  5: from dataclasses import dataclass
  6: from pathlib import Path
  7: import requests
  8: import os
  9: 
 10: class CivitAiLogger:
 11:     """Provides colored logging functionality for API events"""
 12: 
 13:     @staticmethod
 14:     def error(message: str):
 15:         print(f"\033[31m[API Error]:\033[0m {message}")
 16: 
 17:     @staticmethod
 18:     def warning(message: str):
 19:         print(f"\033[33m[API Warning]:\033[0m {message}")
 20: 
 21:     @staticmethod
 22:     def info(message: str):
 23:         print(f"\033[34m[API Info]:\033[0m {message}")
 24: 
 25: @dataclass
 26: class ModelData:
 27:     """Container for validated model metadata"""
 28:     download_url: str
 29:     clean_url: str
 30:     model_name: str
 31:     model_type: str
 32:     version_id: str
 33:     model_id: str
 34:     image_url: Optional[str] = None
 35:     image_name: Optional[str] = None
 36:     is_early_access: bool = False
 37: 
 38: class CivitAiAPI:
 39:     """
 40:     Main API client for CivitAI interactions
 41: 
 42:     Handles core functionality including:
 43:     - API request management
 44:     - URL validation and processing
 45:     - Model metadata extraction
 46:     - Early access verification
 47:     - Preview image handling
 48: 
 49:     Usage Example:
 50:         api = CivitAiAPI()
 51:         result = api.validate_download(
 52:             url='https://civitai.com/models/...',
 53:             file_name='model.safetensors'
 54:         )
 55:     """
 56:     SUPPORTED_TYPES = {'Checkpoint', 'TextualInversion', 'LORA'}
 57:     BASE_URL = 'https://civitai.com/api/v1'
 58:     is_KAGGLE = os.getenv('KAGGLE_URL_BASE')    # to check NSFW
 59: 
 60:     def __init__(self, token: str = None):
 61:         """Initialize API client with optional authentication token"""
 62:         self.token = token or '65b66176dcf284b266579de57fbdc024'    # FAKE
 63:         self.logger = CivitAiLogger()
 64: 
 65:     def _build_url(self, endpoint: str) -> str:
 66:         """Construct full API endpoint URL"""
 67:         return f"{self.BASE_URL}/{endpoint}"
 68: 
 69:     def _fetch_json(self, url: str) -> Optional[Dict]:
 70:         """Execute GET request and return parsed JSON response"""
 71:         try:
 72:             headers = {'Authorization': f"Bearer {self.token}"} if self.token else {}
 73:             response = requests.get(url, headers=headers)
 74:             response.raise_for_status()
 75:             return response.json()
 76:         except requests.RequestException as e:
 77:             self.logger.error(f"Request to {url} failed: {str(e)}")
 78:             return None
 79: 
 80:     def _process_download_url(self, download_url: str) -> Tuple[str, str]:
 81:         """Sanitize download URL and add authentication token"""
 82:         parsed_url = urlparse(download_url)
 83:         query_params = parse_qs(parsed_url.query)
 84:         query_params.pop('token', None)
 85: 
 86:         clean_url = parsed_url._replace(query=urlencode(query_params, doseq=True)).geturl()
 87:         full_url = f"{clean_url}?token={self.token}" if self.token else clean_url
 88:         return clean_url, full_url
 89: 
 90:     def _extract_version_id(self, url: str) -> Optional[str]:
 91:         """Extract model version ID from different URL formats"""
 92:         try:
 93:             # Basic URL format validation
 94:             if not url.startswith(('http://', 'https://')):
 95:                 self.logger.error(f"Invalid URL format: {url}")
 96:                 return None
 97: 
 98:             # Handle model page URLs
 99:             if 'civitai.com/models/' in url:
100:                 if 'modelVersionId=' in url:
101:                     version_part = url.split('modelVersionId=')[1]
102:                     return version_part.split('&')[0].split('#')[0]
103: 
104:                 model_id_part = url.split('/models/')[1]
105:                 model_id = model_id_part.split('/')[0].split('?')[0]
106:                 if not model_id.isdigit():
107:                     self.logger.error(f"Invalid model ID format: {model_id}")
108:                     return None
109: 
110:                 model_data = self._fetch_json(self._build_url(f"models/{model_id}"))
111:                 return model_data['modelVersions'][0]['id'] if model_data else None
112: 
113:             # Handle direct download URLs
114:             if '/api/download/models/' in url:
115:                 version_part = url.split('/api/download/models/')[1]
116:                 return version_part.split('?')[0].split('/')[0]
117: 
118:             self.logger.error(f"Unsupported URL format: {url}")
119:             return None
120: 
121:         except (IndexError, AttributeError, KeyError) as e:
122:             self.logger.error(f"Failed to parse URL: {url} ({str(e)})")
123:             return None
124: 
125:     def _get_preview_metadata(self, images: list, model_name: str) -> Tuple[Optional[str], Optional[str]]:
126:         """Extract appropriate preview image from model metadata"""
127:         if not images:
128:             return None, None
129: 
130:         for img in images:
131:             try:
132:                 if img['nsfwLevel'] >= 4 and self.is_KAGGLE:   # Filter NSFW images for Kaggle
133:                     continue
134:                 image_url = img['url']
135:                 file_extension = image_url.split('.')[-1].split('?')[0]
136:                 base_name = Path(model_name).stem
137:                 return image_url, f"{base_name}.preview.{file_extension}"
138:             except (KeyError, IndexError):
139:                 continue
140:         return None, None
141: 
142:     def _prepare_model_metadata(self, data: Dict, file_name: Optional[str]) -> ModelData:
143:         """Transform raw API response into structured ModelData"""
144:         model_type, final_name = self._determine_model_name(
145:             data=data,
146:             custom_name=file_name
147:         )
148:         clean_url, full_url = self._process_download_url(data['downloadUrl'])
149: 
150:         preview_url, preview_name = None, None
151:         if model_type in self.SUPPORTED_TYPES:
152:             preview_url, preview_name = self._get_preview_metadata(
153:                 images=data.get('images', []),
154:                 model_name=final_name
155:             )
156: 
157:         early_access = data.get('availability') == 'EarlyAccess' or data.get('earlyAccessEndsAt', None)
158: 
159:         return ModelData(
160:             download_url=full_url,
161:             clean_url=clean_url,
162:             model_name=final_name,
163:             model_type=model_type,
164:             version_id=data['id'],
165:             model_id=data['modelId'],
166:             is_early_access=early_access,
167:             image_url=preview_url,
168:             image_name=preview_name
169:         )
170: 
171:     def _determine_model_name(self, data: Dict, custom_name: Optional[str]) -> Tuple[str, str]:
172:         """Generate final model filename with proper extension"""
173:         original_name = data['files'][0]['name']
174:         original_extension = original_name.split('.')[-1]
175: 
176:         if custom_name:
177:             if '.' not in custom_name:
178:                 custom_name = f"{custom_name}.{original_extension}"
179:             return data['model']['type'], custom_name
180:         return data['model']['type'], original_name
181: 
182:     def _get_version_data(self, url: str) -> Tuple[Optional[str], Optional[Dict]]:
183:         """Helper method to extract version ID and fetch API data"""
184:         version_id = self._extract_version_id(url)
185:         if not version_id:
186:             self.logger.error('Invalid model URL')
187:             return None, None
188:         api_data = self._fetch_json(self._build_url(f"model-versions/{version_id}"))
189:         return api_data
190: 
191:     # -- Special function for 'sdAIgen' --
192:     def validate_download(self, url: str, file_name: Optional[str] = None) -> Optional[ModelData]:
193:         """
194:         Validate and process model download URL
195: 
196:         Args:
197:             url: CivitAI model URL in any supported format
198:             file_name: Optional custom filename for the model
199: 
200:         Returns:
201:             ModelData object with processed metadata or None
202:         """
203:         api_data = self._get_version_data(url)
204:         if not api_data:
205:             return None
206: 
207:         model_info = self._prepare_model_metadata(api_data, file_name)
208:         if model_info.is_early_access:
209:             self.logger.warning(
210:                 f"Model: {model_info.model_id} | Version: {model_info.version_id} -> requires Early Access\n"
211:                 f"    > URL: https://civitai.com/models/{model_info.model_id}?modelVersionId={model_info.version_id}"
212:             )
213:             return None
214: 
215:         return model_info
216: 
217:     def get_data(self, url: str) -> Optional[Dict]:
218:         """Get Full Model Version metadata"""
219:         return self._get_version_data(url)
```

## File: modules/json_utils.py
```python
  1: """ JSON Utilities Module | by ANXETY """
  2: 
  3: from functools import wraps
  4: from pathlib import Path
  5: import logging
  6: import json
  7: import os
  8: 
  9: # ==================== Logger Configuration ====================
 10: 
 11: logging.basicConfig(level=logging.WARNING)
 12: logger = logging.getLogger(__name__)
 13: 
 14: class CustomFormatter(logging.Formatter):
 15:     """Custom log formatter with color support for warnings/errors"""
 16:     colors = {
 17:         logging.WARNING: '\033[33m',
 18:         logging.ERROR: '\033[31m',
 19:         'ENDC': '\033[0m'
 20:     }
 21: 
 22:     def format(self, record):
 23:         color = self.colors.get(record.levelno, '')
 24:         message = super().format(record)
 25:         return f"{color}{message}{self.colors['ENDC']}"
 26: 
 27: handler = logging.StreamHandler()
 28: handler.setFormatter(CustomFormatter())
 29: logger.addHandler(handler)
 30: logger.propagate = False
 31: 
 32: # ==================== Argument Validation Decorator ====================
 33: 
 34: def validate_args(min_args: int, max_args: int):
 35:     """Decorator to validate number of arguments in variadic functions
 36: 
 37:     Args:
 38:         min_args: Minimum required arguments (inclusive)
 39:         max_args: Maximum allowed arguments (inclusive)
 40:     """
 41:     def decorator(func):
 42:         @wraps(func)
 43:         def wrapper(*args):
 44:             if not (min_args <= len(args) <= max_args):
 45:                 logger.error(
 46:                     f"Invalid argument count for {func.__name__}. "
 47:                     f"Expected {min_args}-{max_args}, got {len(args)}"
 48:                 )
 49:                 return None
 50:             return func(*args)
 51:         return wrapper
 52:     return decorator
 53: 
 54: # ==================== Core Functionality ====================
 55: 
 56: def parse_key(key: str) -> list[str]:
 57:     """
 58:     Parse dot-separated key with escape support for double dots
 59: 
 60:     Args:
 61:         key: Input key string (e.g., 'parent..child.prop')
 62: 
 63:     Returns:
 64:         List of parsed key segments (e.g., ['parent.child', 'prop'])
 65:     """
 66:     if not isinstance(key, str):
 67:         logger.error('Key must be a string')
 68:         return []
 69: 
 70:     temp_char = '\uE000'
 71:     parts = key.replace('..', temp_char).split('.')
 72:     return [p.replace(temp_char, '.') for p in parts]
 73: 
 74: def _get_nested_value(data: dict, keys: list) -> any:
 75:     """
 76:     Get value using explicit path through nested dictionaries
 77: 
 78:     Args:
 79:         data: Root dictionary
 80:         keys: List of keys forming exact path
 81: 
 82:     Returns:
 83:         Value at specified path or None if path breaks
 84:     """
 85:     current = data
 86:     for key in keys:
 87:         if not isinstance(current, dict):
 88:             return None
 89:         current = current.get(key)
 90:         if current is None:
 91:             return None
 92:     return current
 93: 
 94: def _set_nested_value(data: dict, keys: list, value: any):
 95:     """
 96:     Update existing nested structure without overwriting sibling keys
 97: 
 98:     Args:
 99:         data: Root dictionary to modify
100:         keys: Path to target location
101:         value: New value to set at target
102:     """
103:     current = data
104:     for key in keys[:-1]:
105:         if key not in current or not isinstance(current[key], dict):
106:             current[key] = {}
107:         current = current[key]
108:     current[keys[-1]] = value
109: 
110: def _read_json(filepath: str | Path) -> dict:
111:     """
112:     Safely read JSON file, returning empty dict on error/missing file
113: 
114:     Args:
115:         filepath: Path to JSON file (str or Path object)
116:     """
117:     try:
118:         if not os.path.exists(filepath):
119:             return {}
120: 
121:         with open(filepath, 'r') as f:
122:             content = f.read()
123:             return json.loads(content) if content.strip() else {}
124:     except Exception as e:
125:         logger.error(f"Read error ({filepath}): {str(e)}")
126:         return {}
127: 
128: def _write_json(filepath: str | Path, data: dict):
129:     """
130:     Write JSON file with directory creation and error handling
131: 
132:     Args:
133:         filepath: Destination path (str or Path object)
134:     """
135:     try:
136:         os.makedirs(os.path.dirname(filepath), exist_ok=True)
137:         with open(filepath, 'w') as f:
138:             json.dump(data, f, indent=4, ensure_ascii=False)
139:     except Exception as e:
140:         logger.error(f"Write error ({filepath}): {str(e)}")
141: 
142: # ==================== Main Functions ====================
143: 
144: @validate_args(1, 3)
145: def read(*args) -> any:
146:     """
147:     Read value from JSON file using explicit path
148: 
149:     Args:
150:         filepath (str): Path to JSON file
151:         key (str, optional): Dot-separated key path
152:         default (any, optional): Default if key not found
153: 
154:     Returns:
155:         Value at key path, entire data, or default
156:     """
157:     filepath, key, default = args[0], None, None
158:     if len(args) > 1: key = args[1]
159:     if len(args) > 2: default = args[2]
160: 
161:     data = _read_json(filepath)
162:     if key is None:
163:         return data
164: 
165:     keys = parse_key(key)
166:     if not keys:
167:         return default
168: 
169:     result = _get_nested_value(data, keys)
170:     return result if result is not None else default
171: 
172: @validate_args(3, 3)
173: def save(*args):
174:     """
175:     Save value creating full path
176: 
177:     Args:
178:         filepath (str): JSON file path
179:         key (str): Dot-separated target path
180:         value (any): Value to store
181:     """
182:     filepath, key, value = args[0], args[1], args[2]
183: 
184:     data = _read_json(filepath)
185:     keys = parse_key(key)
186:     if not keys:
187:         return
188: 
189:     _set_nested_value(data, keys, value)
190:     _write_json(filepath, data)
191: 
192: @validate_args(3, 3)
193: def update(*args):
194:     """
195:     Update existing path preserving surrounding data
196: 
197:     Args:
198:         filepath (str): JSON file path
199:         key (str): Dot-separated target path
200:         value (any): New value to set
201:     """
202:     filepath, key, value = args[0], args[1], args[2]
203: 
204:     data = _read_json(filepath)
205:     keys = parse_key(key)
206:     if not keys:
207:         return
208: 
209:     current = data
210:     for part in keys[:-1]:
211:         current = current.setdefault(part, {})
212: 
213:     last_key = keys[-1]
214:     if last_key in current:
215:         if isinstance(current[last_key], dict) and isinstance(value, dict):
216:             current[last_key].update(value)
217:         else:
218:             current[last_key] = value
219:     else:
220:         logger.warning(f"Key '{'.'.join(keys)}' not found. Update failed.")
221: 
222:     _write_json(filepath, data)
223: 
224: @validate_args(2, 2)
225: def delete_key(*args):
226:     """
227:     Remove specified key from JSON data
228: 
229:     Args:
230:         filepath (str): JSON file path
231:         key (str): Dot-separated path to delete
232:     """
233:     filepath, key = args[0], args[1]
234: 
235:     data = _read_json(filepath)
236:     keys = parse_key(key)
237:     if not keys:
238:         return
239: 
240:     current = data
241:     for part in keys[:-1]:
242:         current = current.get(part)
243:         if not isinstance(current, dict):
244:             return
245: 
246:     last_key = keys[-1]
247:     if last_key in current:
248:         del current[last_key]
249:         _write_json(filepath, data)
250: 
251: @validate_args(2, 3)
252: def key_exists(*args) -> bool:
253:     """
254:     Check if key path exists with optional value check
255: 
256:     Args:
257:         filepath (str): JSON file path
258:         key (str): Dot-separated path to check
259:         value (any, optional): Verify exact value match
260: 
261:     Returns:
262:         True if path exists (and value matches if provided)
263:     """
264:     filepath, key = args[0], args[1]
265:     value = args[2] if len(args) > 2 else None
266: 
267:     data = _read_json(filepath)
268:     keys = parse_key(key)
269:     if not keys:
270:         return False
271: 
272:     result = _get_nested_value(data, keys)
273: 
274:     if value is not None:
275:         return result == value
276:     return result is not None
```

## File: modules/Manager.py
```python
  1: """ Manager Module | by ANXETY """
  2: 
  3: from CivitaiAPI import CivitAiAPI    # CivitAI API
  4: import json_utils as js              # JSON
  5: 
  6: from urllib.parse import urlparse, parse_qs
  7: from pathlib import Path
  8: import subprocess
  9: import requests
 10: import zipfile
 11: import shlex
 12: import sys
 13: import os
 14: import re
 15: 
 16: 
 17: CD = os.chdir
 18: 
 19: # Constants
 20: HOME = Path.home()
 21: SCR_PATH = HOME / 'ANXETY'
 22: SETTINGS_PATH = SCR_PATH / 'settings.json'
 23: 
 24: CAI_TOKEN = js.read(SETTINGS_PATH, 'WIDGETS.civitai_token') or '65b66176dcf284b266579de57fbdc024'
 25: HF_TOKEN = js.read(SETTINGS_PATH, 'WIDGETS.huggingface_token') or ''
 26: 
 27: 
 28: ## ====================== Download =======================
 29: 
 30: # Logging function
 31: def log_message(message, log=False):
 32:     if log:
 33:         print(f"{message}")
 34: 
 35: # Error handling decorator
 36: def handle_errors(func):
 37:     def wrapper(*args, **kwargs):
 38:         try:
 39:             return func(*args, **kwargs)
 40:         except Exception as e:
 41:             log_message(f"> \033[31m[Error]:\033[0m {e}", kwargs.get('log', False))
 42:             return None
 43:     return wrapper
 44: 
 45: # Download function
 46: @handle_errors
 47: def m_download(line, log=False, unzip=False):
 48:     """Download files from a comma-separated list of URLs or file paths."""
 49:     links = [link.strip() for link in line.split(',') if link.strip()]
 50: 
 51:     if not links:
 52:         log_message('> Missing URL, downloading nothing', log)
 53:         return
 54: 
 55:     for link in links:
 56:         url = link[0]
 57:         if url.endswith('.txt') and Path(url).expanduser().is_file():
 58:             with open(Path(url).expanduser(), 'r') as file:
 59:                 for line in file:
 60:                     process_download(line, log, unzip)
 61:         else:
 62:             process_download(link, log, unzip)
 63: 
 64: @handle_errors
 65: def process_download(line, log, unzip):
 66:     """Process an individual download line."""
 67:     parts = line.split()
 68:     url = parts[0].replace('\\', '')
 69:     url = clean_url(url)
 70: 
 71:     if not url:
 72:         return
 73: 
 74:     path, filename = handle_path_and_filename(parts, url)
 75:     current_dir = Path.cwd()
 76: 
 77:     try:
 78:         if path:
 79:             path.mkdir(parents=True, exist_ok=True)
 80:             CD(path)
 81: 
 82:         download_file(url, filename, log)
 83:         if unzip and filename and filename.endswith('.zip'):
 84:             unzip_file(filename, log)
 85:     finally:
 86:         CD(current_dir)
 87: 
 88: def handle_path_and_filename(parts, url):
 89:     """Extract path and filename from parts."""
 90:     if len(parts) >= 3:
 91:         path = Path(parts[1]).expanduser()
 92:         filename = parts[2]
 93:     elif len(parts) >= 2:
 94:         path = Path(parts[1]).expanduser() if '/' in parts[1] or '~/' in parts[1] else None
 95:         filename = None if path else parts[1]
 96:     else:
 97:         path, filename = None, None
 98: 
 99:     if 'drive.google.com' not in url:
100:         if filename and not Path(filename).suffix:
101:             url = parts[0]
102:             url_extension = Path(urlparse(url).path).suffix
103:             if url_extension:
104:                 filename += url_extension
105:             else:
106:                 filename = None
107: 
108:     return path, filename
109: 
110: @handle_errors
111: def download_file(url, filename, log):
112:     """Download a file from various sources."""
113:     is_special_domain = any(domain in url for domain in ['civitai.com', 'huggingface.co', 'github.com'])
114: 
115:     if is_special_domain:
116:         download_with_aria2(url, filename, log)
117:     elif 'drive.google.com' in url:
118:         download_google_drive(url, filename, log)
119:     else:
120:         """Download using curl."""
121:         command = f"curl -#JL '{url}'"
122:         if filename:
123:             command += f" -o '{filename}'"
124:         execute_shell_command(command, log)
125: 
126: def download_with_aria2(url, filename, log):
127:     """Download using aria2c."""
128:     aria2_args = ('aria2c --header="User-Agent: Mozilla/5.0" --allow-overwrite=true --console-log-level=error --stderr=true -c -x16 -s16 -k1M -j5')
129: 
130:     if HF_TOKEN and 'huggingface.co' in url:
131:         aria2_args += f' --header="Authorization: Bearer {HF_TOKEN}"'
132: 
133:     command = f"{aria2_args} '{url}'"
134: 
135:     if not filename:
136:         filename = get_file_name(url)
137:     if filename:
138:         command += f" -o '{filename}'"
139: 
140:     monitor_aria2_download(command, log)
141: 
142: def download_google_drive(url, filename, log):
143:     """Download from Google Drive using gdown."""
144:     cmd = 'gdown --fuzzy ' + url
145:     if filename:
146:         cmd += ' -O ' + filename
147:     if 'drive.google.com/drive/folders' in url:
148:         cmd += ' --folder'
149: 
150:     execute_shell_command(cmd, log)
151: 
152: def get_file_name(url):
153:     """Get the file name based on the URL."""
154:     if any(domain in url for domain in ['civitai.com', 'drive.google.com']):
155:         return None
156:     else:
157:         return Path(urlparse(url).path).name
158: 
159: @handle_errors
160: def unzip_file(zip_filepath, log):
161:     """Extract the ZIP file."""
162:     with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
163:         zip_ref.extractall(Path(zip_filepath).parent)
164:     log_message(f">> Successfully unpacked: {zip_filepath}", log)
165: 
166: @handle_errors
167: def monitor_aria2_download(command, log):
168:     """Monitor aria2c download progress."""
169:     try:
170:         process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
171:         error_codes, error_messages = [], []
172:         result = ''
173:         br = False
174: 
175:         while True:
176:             lines = process.stderr.readline()
177:             if lines == '' and process.poll() is not None:
178:                 break
179: 
180:             if lines:
181:                 result += lines
182:                 for output_line in lines.splitlines():
183:                     handle_error_output(lines, error_codes, error_messages)
184: 
185:                     if re.match(r'\[#\w{6}\s.*\]', output_line):
186:                         formatted_line = format_output_line(output_line)
187:                         if log:
188:                             print(f"\r{' ' * 180}\r{formatted_line}", end='')
189:                             sys.stdout.flush()
190:                         br = True
191:                         break
192: 
193:         if log:
194:             for error in error_codes + error_messages:
195:                 print(f"{error}")
196: 
197:             if br:
198:                 print()
199: 
200:             stripe = result.find('======+====+===========')
201:             if stripe != -1:
202:                 for line in result[stripe:].splitlines():
203:                     if '|' in line and 'OK' in line:
204:                         formatted_line = re.sub(r'(\|\s*)(OK)(\s*\|)', r'\1\033[32m\2\033[0m\3', line)
205:                         print(f"{formatted_line}")
206: 
207:         process.wait()
208:     except KeyboardInterrupt:
209:         log_message('\n> Download interrupted', log)
210: 
211: def format_output_line(line):
212:     """Format a line of output with ANSI color codes."""
213:     line = re.sub(r'\[', '\033[35m【\033[0m', line)
214:     line = re.sub(r'\]', '\033[35m】\033[0m', line)
215:     line = re.sub(r'(#)(\w+)', r'\1\033[32m\2\033[0m', line)
216:     line = re.sub(r'(\(\d+%\))', r'\033[36m\1\033[0m', line)
217:     line = re.sub(r'(CN:)(\d+)', r'\1\033[34m\2\033[0m', line)
218:     line = re.sub(r'(DL:)(\d+\w+)', r'\1\033[32m\2\033[0m', line)
219:     line = re.sub(r'(ETA:)(\d+\w+)', r'\1\033[33m\2\033[0m', line)
220:     return line
221: 
222: def handle_error_output(line, error_codes, error_messages):
223:     """Check and collect error messages from the output."""
224:     if 'errorCode' in line or 'Exception' in line:
225:         error_codes.append(line)
226:     if '|' in line and 'ERR' in line:
227:         formatted_line = re.sub(r'(\|\s*)(ERR)(\s*\|)', r'\1\033[31m\2\033[0m\3', line)
228:         error_messages.append(formatted_line)
229: 
230: @handle_errors
231: def execute_shell_command(command, log):
232:     """Execute a shell command and handle logging."""
233:     process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
234:     if log:
235:         for line in process.stderr:
236:             print(line, end='')
237:     process.wait()
238: 
239: @handle_errors
240: def clean_url(url):
241:     """Clean and format URLs to ensure correct access."""
242:     if 'civitai.com/models/' in url:
243:         api = CivitAiAPI(CAI_TOKEN)
244:         if not (data := api.validate_download(url)):
245:             return
246: 
247:         url = data.download_url
248: 
249:     elif 'huggingface.co' in url:
250:         if '/blob/' in url:
251:             url = url.replace('/blob/', '/resolve/')
252:         if '?' in url:
253:             url = url.split('?')[0]
254: 
255:     elif 'github.com' in url:
256:         if '/blob/' in url:
257:             url = url.replace('/blob/', '/raw/')
258: 
259:     return url
260: 
261: ## ======================== Clone ========================
262: 
263: def m_clone(input_source, log=False):
264:     """Main function to clone repositories"""
265:     commands = process_input_source(input_source, log)
266: 
267:     if not commands:
268:         log_message('>> No valid repositories to clone', log)
269:         return
270: 
271:     for command in commands:
272:         execute_command(command, log=log)
273: 
274: def process_input_source(input_source, log=False):
275:     input_path = Path(input_source).expanduser()
276:     commands = []
277: 
278:     def build_command(line):
279:         line = line.strip()
280:         if not line:
281:             return None
282: 
283:         # Extract base command and URL
284:         parts = shlex.split(line)
285:         if len(parts) >= 2 and parts[0] == 'git' and parts[1] == 'clone':
286:             base_command = parts
287:             url = next((p for p in parts[2:] if re.match(r'https?://', p)), None)
288:         else:
289:             url = line
290:             base_command = ['git', 'clone', url]
291: 
292:         if not url:
293:             log_message(f">> Skipping invalid command: {line}", log)
294:             return None
295: 
296:         # Add shallow clone parameters
297:         if '--depth' not in base_command:
298:             base_command += ['--depth', '1']
299: 
300:         return ' '.join(base_command)
301: 
302:     # Process different input types
303:     if input_source.endswith('.txt') and input_path.is_file():
304:         with open(input_path, 'r') as f:
305:             for line in f:
306:                 if cmd := build_command(line):
307:                     commands.append(cmd)
308:     else:
309:         sources = [input_source] if isinstance(input_source, str) else input_source
310:         for source in sources:
311:             if cmd := build_command(source):
312:                 commands.append(cmd)
313: 
314:     return commands
315: 
316: 
317: @handle_errors
318: def execute_command(command, log=False):
319:     repo_url = re.search(r'https?://\S+', command).group()
320:     process = subprocess.Popen(
321:         shlex.split(command),
322:         stdout=subprocess.PIPE,
323:         stderr=subprocess.STDOUT,
324:         text=True
325:     )
326: 
327:     repo_name = None
328:     while True:
329:         output = process.stdout.readline()
330:         if not output and process.poll() is not None:
331:             break
332: 
333:         output = output.strip()
334:         if not output:
335:             continue
336: 
337:         # Parse cloning progress
338:         if 'Cloning into' in output:
339:             repo_path = re.search(r"'(.+?)'", output).group(1)
340:             repo_name = '/'.join(repo_path.split('/')[-3:])
341:             log_message(f">> Cloning: {repo_name} -> {repo_url}", log)
342: 
343:         # Handle error messages
344:         if 'fatal' in output.lower():
345:             log_message(f">> \033[31m[Error]:\033[0m {output}", log)
```

## File: modules/TunnelHub.py
```python
  1: """
  2: Modified script for creating tunnels.
  3: Originated from: https://raw.githubusercontent.com/cupang-afk/subprocess-tunnel/refs/heads/master/src/tunnel.py
  4: Author: cupang-afk https://github.com/cupang-afk
  5: 
  6: This script has been modified specifically for the 'sdAIgen' project and may not be compatible with normal use.
  7: Use the original script of the author cupang-afk.
  8: """
  9: 
 10: 
 11: from typing import Callable, List, Optional, Tuple, TypedDict, Union, get_args
 12: from threading import Event, Lock, Thread
 13: from pathlib import Path
 14: import subprocess
 15: import logging
 16: import socket
 17: import shlex
 18: import time
 19: import re
 20: import os
 21: 
 22: 
 23: StrOrPath = Union[str, Path]
 24: StrOrRegexPattern = Union[str, re.Pattern]
 25: ListHandlersOrBool = Union[List[logging.Handler], bool]
 26: 
 27: 
 28: class ColoredFormatter(logging.Formatter):
 29:     COLORS = {
 30:         logging.DEBUG: '\033[36m',        # Cyan
 31:         logging.INFO: '\033[32m',         # Green
 32:         logging.WARNING: '\033[33m',      # Yellow
 33:         logging.ERROR: '\033[31m',        # Red
 34:         logging.CRITICAL: '\033[31;1m',   # Bold Red
 35:     }
 36: 
 37:     def format(self, record):
 38:         color = self.COLORS.get(record.levelno, '\033[0m')
 39:         message = super().format(record)
 40:         return f"\n{color}[{record.name}]:\033[0m {message}"
 41: 
 42: 
 43: class FileFormatter(logging.Formatter):
 44:     @staticmethod
 45:     def strip_ansi_codes(text: str) -> str:
 46:         ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
 47:         return ansi_escape.sub('', text)
 48: 
 49:     def format(self, record):
 50:         formatted_message = super().format(record)
 51:         return self.strip_ansi_codes(formatted_message)
 52: 
 53: 
 54: class TunnelDict(TypedDict):
 55:     command: str
 56:     pattern: re.Pattern
 57:     name: str
 58:     note: Optional[str]
 59:     callback: Optional[Callable[[str, Optional[str], Optional[str]], None]]
 60: 
 61: 
 62: class Tunnel:
 63:     """
 64:     A class for creating and managing tunnels.
 65: 
 66:     This class allows for the establishment of tunnels to redirect traffic through specified ports.
 67:     It supports local port checking, process and thread management, as well as logging for debugging
 68:     and monitoring tunnel operations.
 69: 
 70:     Attributes:
 71:         port (int): The port on which the tunnel will be created.
 72:         check_local_port (bool): Flag indicating whether to check the local port before creating the tunnel.
 73:         debug (bool): Flag enabling debug mode, which outputs additional information to the logs.
 74:         timeout (int): The timeout (in seconds) for operations related to the tunnel.
 75:         propagate (bool): Flag indicating whether to propagate logs to the parent logger.
 76:         log_handlers (List[logging.Handler]): List of log handlers for configuring log output.
 77:         log_dir (StrOrPath): Directory for storing logs. If not specified, the current working directory is used.
 78:         callback (Callable[[List[Tuple[str, Optional[str]]]], None]): A callback function that will be invoked with
 79:             a list of URLs after the tunnel is created.
 80: 
 81:     Instance Attributes:
 82:         _is_running (bool): Indicates whether the tunnel is currently running.
 83:         urls (List[Tuple[str, Optional[str], Optional[str]]]): List of URLs associated with the tunnel,
 84:             including the URL, note, and name of the tunnel.
 85:         urls_lock (Lock): Mutex for safe access to the list of URLs, ensuring thread-safety.
 86:         jobs (List[Thread]): List of threads associated with the tunnel, used for managing tunnel processes.
 87:         processes (List[subprocess.Popen]): List of running subprocesses for managing tunnels.
 88:         tunnel_list (List[TunnelDict]): List of dictionaries containing parameters for each tunnel added.
 89:         stop_event (Event): Event used to signal the stopping of tunnel operations.
 90:         printed (Event): Event indicating whether tunnel information has been printed to the console.
 91:         logger (logging.Logger): Logger for recording information about the tunnel's operation, including
 92:             errors and status updates.
 93: 
 94:     Exceptions:
 95:         ValueError: Raised if the specified port is invalid or occupied.
 96:         RuntimeError: Raised if the tunnel is already running or if an operation is attempted when the tunnel is not running.
 97:     """
 98: 
 99:     def __init__(
100:         self,
101:         port: int,
102:         check_local_port: bool = True,
103:         debug: bool = False,
104:         timeout: int = 15,
105:         propagate: bool = False,
106:         log_handlers: ListHandlersOrBool = None,
107:         log_dir: StrOrPath = None,
108:         callback: Callable[[List[Tuple[str, Optional[str]]]], None] = None,
109:     ):
110:         """Initialize the Tunnel class with provided parameters."""
111:         self._is_running = False
112:         self.urls: List[Tuple[str, Optional[str], Optional[str]]] = []
113:         self.urls_lock = Lock()
114:         self.jobs: List[Thread] = []
115:         self.processes: List[subprocess.Popen] = []
116:         self.tunnel_list: List[TunnelDict] = []
117:         self.stop_event: Event = Event()
118:         self.printed = Event()
119:         self.port = port
120:         self.check_local_port = check_local_port
121:         self.debug = debug
122:         self.timeout = timeout
123:         self.log_handlers = log_handlers or []
124:         self.log_dir = Path(log_dir) if log_dir else Path.home() / 'tunnel_logs'
125:         self.log_dir.mkdir(parents=True, exist_ok=True)
126:         self.callback = callback
127: 
128:         self.logger = self.setup_logger(propagate)
129: 
130:     def setup_logger(self, propagate: bool) -> logging.Logger:
131:         """Set up the logger for the tunnel operations."""
132:         logger = logging.getLogger('TunnelHub')
133:         logger.setLevel(logging.DEBUG if self.debug else logging.INFO)
134:         logger.propagate = propagate
135: 
136:         if not propagate:
137:             for handler in logger.handlers[:]:
138:                 logger.removeHandler(handler)
139: 
140:         if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
141:             stream_handler = logging.StreamHandler()
142:             stream_handler.setLevel(logger.level)
143:             stream_handler.setFormatter(ColoredFormatter('{message}', style='{'))
144:             logger.addHandler(stream_handler)
145: 
146:         log_file = self.log_dir / 'tunnelhub.log'
147:         file_handler = logging.FileHandler(log_file, encoding='utf-8')
148:         file_handler.setLevel(logging.DEBUG)
149:         file_handler.setFormatter(FileFormatter("[%(asctime)s] [%(name)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
150:         logger.addHandler(file_handler)
151: 
152:         for handler in self.log_handlers:
153:             logger.addHandler(handler)
154: 
155:         return logger
156: 
157:     def is_command_available(self, command: str) -> bool:
158:         """Check if the specified command is available in the system PATH."""
159:         return any(
160:             os.access(os.path.join(path, command), os.X_OK)
161:             for path in os.environ['PATH'].split(os.pathsep)
162:         )
163: 
164:     def add_tunnel(self, *, command: str, pattern: StrOrRegexPattern, name: str,
165:                  note: str = None, callback: Callable[[str, Optional[str], Optional[str]], None] = None) -> None:
166:         """Add a new tunnel with the specified command, pattern, name, and optional note and callback."""
167:         cmd_name = command.split()[0]
168:         if not self.is_command_available(cmd_name):
169:             self.logger.warning(f"Skipping {name} - {cmd_name} not installed")
170:             return
171: 
172:         if isinstance(pattern, str):
173:             pattern = re.compile(pattern)
174: 
175:         self.logger.debug(f"Adding tunnel {command=} {pattern=} {name=} {note=} {callback=}")
176:         self.tunnel_list.append({
177:             'command': command,
178:             'pattern': pattern,
179:             'name': name,
180:             'note': note,
181:             'callback': callback,
182:         })
183: 
184:     def start(self) -> None:
185:         """Start the tunnel and its associated threads."""
186:         if self._is_running:
187:             raise RuntimeError('Tunnel is already running')
188: 
189:         self.__enter__()
190: 
191:         try:
192:             while not self.printed.is_set():
193:                 time.sleep(1)
194:         except KeyboardInterrupt:
195:             self.logger.warning('\033[33m⚠️  Keyboard Interrupt detected, stopping tunnel\033[0m')
196:             self.stop()
197: 
198:     def stop(self) -> None:
199:         """Stop the tunnel and clean up resources."""
200:         if not self._is_running:
201:             raise RuntimeError('Tunnel is not running')
202: 
203:         self.logger.info(f"💣 \033[32mTunnels:\033[0m \033[34m{self.get_tunnel_names()}\033[0m -> \033[31mKilled.\033[0m")
204:         self.stop_event.set()
205:         self.terminate_processes()
206:         self.join_threads()
207:         self.reset()
208: 
209:     def get_tunnel_names(self) -> str:
210:         """Get a comma-separated string of tunnel names."""
211:         return ', '.join(tunnel['name'] for tunnel in self.tunnel_list)
212: 
213:     def terminate_processes(self) -> None:
214:         """Terminate all running subprocesses associated with the tunnels."""
215:         for process in self.processes:
216:             try:
217:                 if process.poll() is None:
218:                     process.terminate()
219:                     process.wait(timeout=5)
220:             except Exception as e:
221:                 self.logger.warning(f"Error terminating process: {str(e)}")
222:         self.processes.clear()
223: 
224:     def join_threads(self) -> None:
225:         """Wait for all threads associated with the tunnels to finish."""
226:         for job in self.jobs:
227:             job.join()
228: 
229:     def __enter__(self):
230:         """Enter the runtime context for the tunnel."""
231:         if self._is_running:
232:             raise RuntimeError('Tunnel is already running by another method')
233: 
234:         if not self.tunnel_list:
235:             raise ValueError('No tunnels added')
236: 
237:         print_job = Thread(target=self._print)
238:         print_job.start()
239:         self.jobs.append(print_job)
240: 
241:         for tunnel in self.tunnel_list:
242:             self.start_tunnel_thread(tunnel)
243: 
244:         self._is_running = True
245:         return self
246: 
247:     def start_tunnel_thread(self, tunnel: TunnelDict) -> None:
248:         """Start a new thread for the specified tunnel."""
249:         try:
250:             cmd = tunnel['command'].format(port=self.port)
251:             name = tunnel.get('name')
252:             tunnel_thread = Thread(target=self._run, args=(cmd, name))
253:             tunnel_thread.start()
254:             self.jobs.append(tunnel_thread)
255:         except Exception as e:
256:             self.logger.error(f"Failed to start tunnel {tunnel.get('name')}: {str(e)}")
257: 
258:     def __exit__(self, exc_type, exc_value, exc_tb):
259:         """Exit the runtime context for the tunnel, stopping it."""
260:         self.stop()
261: 
262:     def reset(self) -> None:
263:         """Reset the tunnel state, clearing all stored URLs, jobs, and processes."""
264:         self.urls.clear()
265:         self.jobs.clear()
266:         self.processes.clear()
267:         self.stop_event.clear()
268:         self.printed.clear()
269:         self._is_running = False
270: 
271:     @staticmethod
272:     def is_port_in_use(port: int) -> bool:
273:         """Check if the specified port is currently in use."""
274:         try:
275:             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
276:                 s.settimeout(1)
277:                 return s.connect_ex(('localhost', port)) == 0
278:         except Exception:
279:             return False
280: 
281:     @staticmethod
282:     def wait_for_condition(condition: Callable[[], bool], *, interval: int = 1, timeout: int = 10) -> bool:
283:         """Wait for a condition to be true, checking at specified intervals."""
284:         start_time = time.time()
285:         elapsed_time = 0
286:         checks_count = 0
287:         timeout = max(1, timeout) if timeout is not None else None
288: 
289:         while True:
290:             if condition():
291:                 return True
292: 
293:             checks_count += 1
294:             elapsed_time = time.time() - start_time
295: 
296:             if timeout is not None and elapsed_time >= timeout:
297:                 return False
298: 
299:             next_interval = min(interval, (timeout - elapsed_time) / (checks_count + 1)) if timeout else interval
300:             time.sleep(next_interval)
301: 
302:     def _process_line(self, line: str) -> bool:
303:         """Process a line of output from the tunnel command to check for URLs."""
304:         for tunnel in self.tunnel_list:
305:             if self.extract_url(tunnel, line):
306:                 return True
307:         return False
308: 
309:     def extract_url(self, tunnel: TunnelDict, line: str) -> bool:
310:         """Extract a URL from a line of output based on the tunnel's regex pattern."""
311:         regex = tunnel['pattern']
312:         matches = regex.search(line)
313: 
314:         if matches:
315:             link = matches.group().strip()
316:             link = link if link.startswith('http') else 'http://' + link
317:             note = tunnel.get('note')
318:             name = tunnel.get('name')
319:             callback = tunnel.get('callback')
320: 
321:             with self.urls_lock:
322:                 self.urls.append((link, note, name))
323: 
324:             if callback:
325:                 self.invoke_callback(callback, link, note, name)
326:             return True
327:         return False
328: 
329:     def invoke_callback(self, callback: Callable, link: str, note: Optional[str], name: Optional[str]) -> None:
330:         """Invoke the provided callback with the extracted URL and its associated metadata."""
331:         try:
332:             callback(link, note, name)
333:         except Exception:
334:             self.logger.error('An error occurred while invoking URL callback', exc_info=True)
335: 
336:     def _run(self, cmd: str, name: str) -> None:
337:         """Run the specified command in a subprocess, monitoring its output."""
338:         log_path = self.log_dir / f"tunnel_{name}.log"
339:         log_path.write_text('')  # Clear previous log file
340: 
341:         log = self.logger.getChild(name)  # Create a child logger for this tunnel
342:         self.setup_file_logging(log, log_path)  # Set up file logging for this tunnel
343: 
344:         try:
345:             self.wait_for_port_if_needed()
346:             cmd = shlex.split(cmd)
347:             process = subprocess.Popen(
348:                 cmd,
349:                 stdout=subprocess.PIPE,
350:                 stderr=subprocess.STDOUT,
351:                 stdin=subprocess.PIPE,
352:                 universal_newlines=True,
353:                 bufsize=1,
354:             )
355:             self.processes.append(process)
356:             self.monitor_process_output(process, log)
357: 
358:         except Exception as e:
359:             log.error(f"Error in tunnel: {str(e)}", exc_info=self.debug)
360:         finally:
361:             for handler in log.handlers:
362:                 handler.close()  # Close any handlers associated with this logger
363: 
364:     def setup_file_logging(self, log: logging.Logger, log_path: Path) -> None:
365:         """Set up file logging for the specified logger and log file path."""
366:         if not log.handlers:
367:             handler = logging.FileHandler(log_path, encoding='utf-8')
368:             handler.setLevel(logging.DEBUG)
369:             handler.setFormatter(FileFormatter("[%(name)s]: %(message)s"))
370:             log.addHandler(handler)
371: 
372:     def wait_for_port_if_needed(self) -> None:
373:         """Wait for the specified port to be available if the check_local_port flag is set."""
374:         if self.check_local_port:
375:             self.wait_for_condition(
376:                 lambda: self.is_port_in_use(self.port) or self.stop_event.is_set(),
377:                 interval=1,
378:                 timeout=None,
379:             )
380: 
381:     def monitor_process_output(self, process: subprocess.Popen, log: logging.Logger) -> None:
382:         """Monitor the output of the subprocess and process any lines received."""
383:         url_extracted = False
384:         while not self.stop_event.is_set() and process.poll() is None:
385:             line = process.stdout.readline()
386:             if not line:
387:                 break
388:             if not url_extracted:
389:                 url_extracted = self._process_line(line)
390:             log.debug(line.rstrip())
391: 
392:     def _print(self) -> None:
393:         """Print the collected tunnel URLs."""
394:         if self.check_local_port:
395:             self.wait_for_port_if_needed()
396: 
397:         if not self.wait_for_condition(
398:             lambda: len(self.urls) == len(self.tunnel_list) or self.stop_event.is_set(),
399:             interval=1,
400:             timeout=self.timeout,
401:         ):
402:             self.logger.warning('Timeout while getting tunnel URLs, print available URLs')
403: 
404:         if not self.stop_event.is_set():
405:             self.display_urls()
406: 
407:     def display_urls(self) -> None:
408:         """Display the collected URLs in a formatted manner."""
409:         with self.urls_lock:
410:             width = 100
411:             tunnel_name_width = max(len(name) for _, _, name in self.urls) if self.urls else 6
412: 
413:             # Print the header
414:             print('\n\033[32m+' + '=' * (width - 2) + '+\033[0m\n')
415: 
416:             # Print each URL
417:             for url, note, name in self.urls:
418:                 print(f"\033[32m 🔗 Tunnel \033[0m{name:<{tunnel_name_width}}  \033[32mURL: \033[0m{url} {note or ''}")
419: 
420:             # Print the footer
421:             print('\n\033[32m+' + '=' * (width - 2) + '+\033[0m\n')
422: 
423:             if self.callback:
424:                 self.invoke_callback(self.callback, self.urls)
425: 
426:             self.printed.set()
```

## File: modules/webui_utils.py
```python
  1: # ~ WebUI Utils Module | by ANXETY ~
  2: 
  3: import json_utils as js    # JSON
  4: 
  5: from pathlib import Path
  6: import os
  7: 
  8: 
  9: # Constants
 10: HOME = Path.home()
 11: SCR_PATH = HOME / 'ANXETY'
 12: SETTINGS_PATH = SCR_PATH / 'settings.json'
 13: 
 14: WEBUI_PATHS = {
 15:     'A1111': (
 16:         'Stable-diffusion', 'VAE', 'Lora',
 17:         'embeddings', 'extensions', 'ESRGAN', 'outputs'
 18:     ),
 19:     'ComfyUI': (
 20:         'checkpoints', 'vae', 'loras',
 21:         'embeddings', 'custom_nodes', 'upscale_models', 'output'
 22:     ),
 23:     'Classic': (
 24:         'Stable-diffusion', 'VAE', 'Lora',
 25:         'embeddings', 'extensions', 'ESRGAN', 'output'
 26:     )
 27: }
 28: 
 29: DEFAULT_UI = 'A1111'
 30: 
 31: # New: Define a centralized base directory for all shared models
 32: SHARED_MODEL_BASE = HOME / 'sd_models_shared'
 33: 
 34: 
 35: def update_current_webui(current_value):
 36:     """Update the current WebUI value and save settings."""
 37:     current_stored = js.read(SETTINGS_PATH, 'WEBUI.current')
 38:     latest_value = js.read(SETTINGS_PATH, 'WEBUI.latest', None)
 39: 
 40:     if latest_value is None or current_stored != current_value:
 41:         js.save(SETTINGS_PATH, 'WEBUI.latest', current_stored)
 42:         js.save(SETTINGS_PATH, 'WEBUI.current', current_value)
 43: 
 44:     js.save(SETTINGS_PATH, 'WEBUI.webui_path', str(HOME / current_value))
 45:     _set_webui_paths(current_value)
 46: 
 47: def _set_webui_paths(ui):
 48:     """Configure paths for specified UI, fallback to A1111 for unknown UIs"""
 49:     selected_ui = ui if ui in WEBUI_PATHS else DEFAULT_UI
 50:     webui_root = HOME / ui
 51:     
 52:     # NEW: All model-related paths will now point to subdirectories under SHARED_MODEL_BASE
 53:     models_root = SHARED_MODEL_BASE 
 54:     os.makedirs(models_root, exist_ok=True) # Ensure shared base exists
 55: 
 56:     # Fix: Define is_comfy and is_classic before their first use
 57:     is_comfy = selected_ui == 'ComfyUI'
 58:     is_classic = selected_ui == 'Classic'
 59: 
 60:     # Get path components for selected UI (these are now mostly logical names)
 61:     paths = WEBUI_PATHS[selected_ui]
 62:     checkpoint_subdir, vae_subdir, lora_subdir, embed_subdir, extension_subdir, upscale_subdir, output_subdir = paths
 63: 
 64:     # Adjust subdirectory names for shared storage based on UI type, ensuring consistent naming
 65:     # These effectively standardize paths under SHARED_MODEL_BASE
 66:     actual_checkpoint_subdir = 'checkpoints' if is_comfy else 'Stable-diffusion'
 67:     actual_vae_subdir = 'vae'
 68:     actual_lora_subdir = 'loras' if is_comfy else 'Lora'
 69:     actual_embed_subdir = 'embeddings'
 70:     actual_control_subdir = 'controlnet' if is_comfy else 'ControlNet'
 71:     actual_upscale_subdir = 'upscale_models' if is_comfy else 'ESRGAN'
 72:     actual_adetailer_subdir = 'ultralytics' if is_comfy else 'adetailer'
 73:     actual_clip_subdir = 'clip' if is_comfy else 'text_encoder'
 74:     actual_unet_subdir = 'unet' if is_comfy else 'unet' # Unet dir for both
 75:     actual_vision_subdir = 'clip_vision'
 76:     actual_encoder_subdir = 'text_encoders' if is_comfy else 'text_encoder'
 77:     actual_diffusion_subdir = 'diffusion_models'
 78: 
 79:     path_config = {
 80:         'webui_path': str(webui_root), # Add the main webui_path here
 81:         'model_dir': str(models_root / actual_checkpoint_subdir),
 82:         'vae_dir': str(models_root / actual_vae_subdir),
 83:         'lora_dir': str(models_root / actual_lora_subdir),
 84:         'embed_dir': str(models_root / actual_embed_subdir),
 85:         'control_dir': str(models_root / actual_control_subdir),
 86:         'upscale_dir': str(models_root / actual_upscale_subdir),
 87:         'adetailer_dir': str(models_root / actual_adetailer_subdir),
 88:         'clip_dir': str(models_root / actual_clip_subdir),
 89:         'unet_dir': str(models_root / actual_unet_subdir),
 90:         'vision_dir': str(models_root / actual_vision_subdir),
 91:         'encoder_dir': str(models_root / actual_encoder_subdir),
 92:         'diffusion_dir': str(models_root / actual_diffusion_subdir),
 93:         
 94:         # Extensions and outputs usually remain UI-specific
 95:         'extension_dir': str(webui_root / extension_subdir),
 96:         'output_dir': str(webui_root / output_subdir),
 97:         'config_dir': str(webui_root / ('user/default' if is_comfy else ''))
 98:     }
 99: 
100:     # Ensure all new shared directories exist
101:     for key, path_str in path_config.items():
102:         if '_dir' in key and 'extension_dir' not in key and 'output_dir' not in key and 'config_dir' not in key:
103:             Path(path_str).mkdir(parents=True, exist_ok=True)
104:             
105:     js.save(SETTINGS_PATH, 'WEBUI', path_config)
106: 
107: def handle_setup_timer(webui_path, timer_webui):
108:     """Manage timer persistence for WebUI instances."""
109:     timer_file = Path(webui_path) / 'static' / 'timer.txt'
110:     timer_file.parent.mkdir(parents=True, exist_ok=True)
111: 
112:     try:
113:         with timer_file.open('r') as f:
114:             timer_webui = float(f.read())
115:     except FileNotFoundError:
116:         pass
117: 
118:     with timer_file.open('w') as f:
119:         f.write(str(timer_webui))
120: 
121:     return timer_webui
```

## File: modules/widget_factory.py
```python
  1: """ WidgetFactory Module | by ANXETY """
  2: 
  3: from IPython.display import display, HTML
  4: import ipywidgets as widgets
  5: import time
  6: 
  7: class WidgetFactory:
  8:     # INIT
  9:     def __init__(self):
 10:         self.default_style = {'description_width': 'initial'}
 11:         self.default_layout = widgets.Layout()
 12: 
 13:     def _validate_class_names(self, class_names):
 14:         """Validate and normalize class names."""
 15:         if class_names is None:
 16:             return []
 17: 
 18:         if isinstance(class_names, str):
 19:             return [class_names.strip()]
 20: 
 21:         if isinstance(class_names, list):
 22:             return [cls.strip() for cls in class_names if cls.strip()]
 23: 
 24:         self._log(f"Invalid class_names type: {type(class_names).__name__}", 'WARNING')
 25:         return []
 26: 
 27:     def add_classes(self, widget, class_names):
 28:         """Add CSS classes to a widget."""
 29:         classes = self._validate_class_names(class_names)
 30:         for cls in classes:
 31:             widget.add_class(cls)
 32: 
 33:     # HTML
 34:     def load_css(self, css_path):
 35:         """Load CSS from a file and display it in the notebook."""
 36:         try:
 37:             with open(css_path, 'r') as file:
 38:                 data = file.read()
 39:                 display(HTML(f"<style>{data}</style>"))
 40:         except Exception as e:
 41:             print(f"Error loading CSS: {e}")
 42: 
 43:     def load_js(self, js_path):
 44:         """Load JavaScript from a file and display it in the notebook."""
 45:         try:
 46:             with open(js_path, 'r') as file:
 47:                 data = file.read()
 48:                 display(HTML(f"<script>{data}</script>"))
 49:         except Exception as e:
 50:             print(f"Error loading JavaScript: {e}")
 51: 
 52:     def create_html(self, content, class_names=None):
 53:         """Create an HTML widget with optional CSS classes."""
 54:         html_widget = widgets.HTML(content)
 55:         if class_names:
 56:             self.add_classes(html_widget, class_names)
 57:         return html_widget
 58: 
 59:     def create_header(self, name, class_names=None):
 60:         """Create a header HTML widget."""
 61:         class_names_str = ' '.join(class_names) if class_names else 'header'
 62:         header = f'<div class="{class_names_str}">{name}</div>'
 63:         return self.create_html(header)
 64: 
 65:     # Widgets
 66:     ## Supporting functions
 67:     def _apply_layouts(self, children, layouts):
 68:         """Apply layouts to children widgets."""
 69:         n_layouts = len(layouts)
 70: 
 71:         if n_layouts == 1:
 72:             # Apply the single layout to all children
 73:             for child in children:
 74:                 child.layout = layouts[0]
 75:         else:
 76:             for child, layout in zip(children, layouts):
 77:                 child.layout = layout
 78: 
 79:     def _create_widget(self, widget_type, class_names=None, **kwargs):
 80:         """Create a widget of a specified type with optional classes and styles."""
 81:         style = kwargs.get('style', self.default_style)
 82: 
 83:         # Set default layout if not provided
 84:         if widget_type in [widgets.Text, widgets.Dropdown, widgets.Textarea]:
 85:             if 'layout' not in kwargs and kwargs.get('reset') != True:    # reset -> return default width
 86:                 kwargs['layout'] = widgets.Layout(width='100%')
 87: 
 88:         widget = widget_type(style=style, **kwargs)
 89: 
 90:         if class_names:
 91:             self.add_classes(widget, class_names)
 92: 
 93:         return widget
 94: 
 95:     ## Creation functions
 96:     def create_text(self, description, value='', placeholder='', class_names=None, **kwargs):
 97:         """Create a text input widget."""
 98:         return self._create_widget(
 99:             widgets.Text,
100:             description=description,
101:             value=value,
102:             placeholder=placeholder,
103:             class_names=class_names,
104:             **kwargs
105:         )
106: 
107:     def create_textarea(self, description, value='', placeholder='', class_names=None, **kwargs):
108:         """Create a textarea input widget."""
109:         return self._create_widget(
110:             widgets.Textarea,
111:             description=description,
112:             value=value,
113:             placeholder=placeholder,
114:             class_names=class_names,
115:             **kwargs
116:         )
117: 
118:     def create_dropdown(self, options, description, value=None, placeholder='', class_names=None, **kwargs):
119:         """Create a dropdown widget."""
120:         if value is None and options:
121:             value = options[0]
122: 
123:         return self._create_widget(
124:             widgets.Dropdown,
125:             options=options,
126:             description=description,
127:             value=value,
128:             placeholder=placeholder,
129:             class_names=class_names,
130:             **kwargs
131:         )
132: 
133:     def create_select_multiple(self, options, description, value=None, class_names=None, **kwargs):
134:         """Create a multiple select widget."""
135:         if isinstance(value, str):
136:             value = (value,)
137:         elif value is None:
138:             value = ()
139: 
140:         return self._create_widget(
141:             widgets.SelectMultiple,
142:             options=options,
143:             description=description,
144:             value=value,
145:             class_names=class_names,
146:             **kwargs
147:         )
148: 
149:     def create_checkbox(self, description, value=False, class_names=None, **kwargs):
150:         """Create a checkbox widget."""
151:         return self._create_widget(
152:             widgets.Checkbox,
153:             description=description,
154:             value=value,
155:             class_names=class_names,
156:             **kwargs
157:         )
158: 
159:     def create_button(self, description, class_names=None, **kwargs):
160:         """Create a button widget."""
161:         return self._create_widget(
162:             widgets.Button,
163:             description=description,
164:             class_names=class_names,
165:             **kwargs
166:         )
167: 
168:     def _create_box(self, box_type, children, class_names=None, **kwargs):
169:         """Create a box layout (horizontal or vertical) for widgets."""
170:         if 'layouts' in kwargs:
171:             self._apply_layouts(children, kwargs.pop('layouts'))
172: 
173:         return self._create_widget(
174:             box_type,
175:             children=children,
176:             class_names=class_names,
177:             **kwargs
178:         )
179: 
180:     def create_hbox(self, children, class_names=None, **kwargs):
181:         """Create a horizontal box layout for widgets."""
182:         return self._create_box(widgets.HBox, children, class_names, **kwargs)
183: 
184:     def create_vbox(self, children, class_names=None, **kwargs):
185:         """Create a vertical box layout for widgets."""
186:         return self._create_box(widgets.VBox, children, class_names, **kwargs)
187: 
188:     def create_box(self, children, direction='column', wrap=True, class_names=None, **kwargs):
189:         """
190:         Create a flexible Box container with adjustable direction and wrapping.
191:         -  direction (str): Layout direction - 'row' (default) or 'column'.
192:         -  wrap (bool): Enable flex wrapping for children (only for Box container).
193:         """
194:         if direction not in ('row', 'column'):
195:             raise ValueError(f"Invalid direction: {direction}. Use 'row' or 'column'.")
196: 
197:         layout = kwargs.pop('layout', {})
198:         layout.update({
199:             'flex_flow': direction,
200:             'flex_wrap': 'wrap' if wrap else 'nowrap'
201:         })
202: 
203:         return self._create_box(
204:             widgets.Box,
205:             children,
206:             class_names=class_names,
207:             layout=layout,
208:             **kwargs
209:         )
210: 
211:     # Other
212:     def display(self, widgets):
213:         """Display one or multiple widgets."""
214:         if isinstance(widgets, list):
215:             for widget in widgets:
216:                 display(widget)
217:         else:
218:             display(widgets)
219: 
220:     def close(self, widgets, class_names=None, delay=0.2):
221:         """Close one or multiple widgets after a delay."""
222:         if not isinstance(widgets, list):
223:             widgets = [widgets]
224: 
225:         if class_names:
226:             for widget in widgets:
227:                 self.add_classes(widget, class_names)
228: 
229:         time.sleep(delay)  # closing delay for all widgets
230: 
231:         # Close all widgets
232:         for widget in widgets:
233:             widget.close()
234: 
235:     # CallBack
236:     def connect_widgets(self, widget_pairs, callbacks):
237:         """
238:         Connect multiple widgets to callback functions for specified property changes.
239: 
240:         Parameters:
241:         - widget_pairs: List of tuples where each tuple contains a widget and the property name to observe.
242:         - callbacks: List of callback functions or a single callback function to be called on property change.
243:         """
244:         if not isinstance(callbacks, list):
245:             callbacks = [callbacks]
246: 
247:         for widget, property_name in widget_pairs:
248:             for callback in callbacks:
249:                 widget.observe(lambda change, widget=widget, callback=callback: callback(change, widget), names=property_name)
```

## File: Notebook/LightningAnxiety.ipynb
```
   1: {
   2:  "cells": [
   3:   {
   4:    "cell_type": "markdown",
   5:    "id": "4731600d-b776-48c4-88e0-8c20295abf71",
   6:    "metadata": {},
   7:    "source": [
   8:     "1. Setup Environment 🔽\n",
   9:     "\n",
  10:     "This cell downloads the initial setup.py script from your fork and then executes it, instructing the setup process to pull all subsequent project files from your repository."
  11:    ]
  12:   },
  13:   {
  14:    "cell_type": "code",
  15:    "execution_count": 1,
  16:    "id": "fa348b8d-7e1e-48b4-b5d7-f1b336a708a9",
  17:    "metadata": {},
  18:    "outputs": [
  19:     {
  20:      "data": {
  21:       "text/html": [
  22:        "\n",
  23:        "    <div class=\"season-container\">\n",
  24:        "      <div class=\"text-container\">\n",
  25:        "        <span>🌴</span>\n",
  26:        "        <span>A</span><span>N</span><span>X</span><span>E</span><span>T</span><span>Y</span>\n",
  27:        "        <span>&nbsp;</span>\n",
  28:        "        <span>S</span><span>D</span><span>-</span><span>W</span><span>E</span><span>B</span><span>U</span><span>I</span>\n",
  29:        "        <span>&nbsp;</span>\n",
  30:        "        <span>V</span><span>2</span>\n",
  31:        "        <span>🌴</span>\n",
  32:        "      </div>\n",
  33:        "\n",
  34:        "      <div class=\"message-container\">\n",
  35:        "        <span>Done! Now you can run the cells below. ☄️</span>\n",
  36:        "        <span>Runtime environment: <span class=\"env\">Lightning AI</span></span>\n",
  37:        "        <span>File location: <span class=\"files-location\">/teamspace/studios/this_studio/ANXETY</span></span>\n",
  38:        "        <span>Current fork: <span class='fork'>drf0rk/sdAIgenLightning</span></span>\n",
  39:        "        <span>Current branch: <span class=\"branch\">main</span></span>\n",
  40:        "      </div>\n",
  41:        "    </div>\n",
  42:        "    \n",
  43:        "    <style>\n",
  44:        "    @import url('https://fonts.googleapis.com/css2?family=Righteous&display=swap');\n",
  45:        "\n",
  46:        "    .season-container {\n",
  47:        "      position: relative;\n",
  48:        "      margin: 0 10px !important;\n",
  49:        "      padding: 20px !important;\n",
  50:        "      border-radius: 15px;\n",
  51:        "      margin: 10px 0;\n",
  52:        "      overflow: hidden;\n",
  53:        "      min-height: 200px;\n",
  54:        "      background: linear-gradient(180deg, #ffe76633, transparent);\n",
  55:        "      border-top: 2px solid #ffe766;\n",
  56:        "      animation: fadeIn 0.5s ease-in !important;\n",
  57:        "    }\n",
  58:        "\n",
  59:        "    @keyframes fadeIn {\n",
  60:        "      from { opacity: 0; }\n",
  61:        "      to { opacity: 1; }\n",
  62:        "    }\n",
  63:        "\n",
  64:        "    .text-container {\n",
  65:        "      display: flex;\n",
  66:        "      flex-wrap: wrap;\n",
  67:        "      justify-content: center;\n",
  68:        "      align-items: center;\n",
  69:        "      gap: 0.5em;\n",
  70:        "      font-family: 'Righteous', cursive;\n",
  71:        "      margin-bottom: 1em;\n",
  72:        "    }\n",
  73:        "\n",
  74:        "    .text-container span {\n",
  75:        "      font-size: 2.5rem;\n",
  76:        "      color: #ffe766;\n",
  77:        "      opacity: 0;\n",
  78:        "      transform: translateY(-20px);\n",
  79:        "      filter: blur(4px);\n",
  80:        "      transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);\n",
  81:        "    }\n",
  82:        "\n",
  83:        "    .text-container.loaded span {\n",
  84:        "      opacity: 1;\n",
  85:        "      transform: translateY(0);\n",
  86:        "      filter: blur(0);\n",
  87:        "      color: #fff7cc;\n",
  88:        "    }\n",
  89:        "\n",
  90:        "    .message-container {\n",
  91:        "      font-family: 'Righteous', cursive;\n",
  92:        "      text-align: center;\n",
  93:        "      display: flex;\n",
  94:        "      flex-direction: column;\n",
  95:        "      gap: 0.5em;\n",
  96:        "    }\n",
  97:        "\n",
  98:        "    .message-container span {\n",
  99:        "      font-size: 1.2rem;\n",
 100:        "      color: #ffe766;\n",
 101:        "      opacity: 0;\n",
 102:        "      transform: translateY(20px);\n",
 103:        "      transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);\n",
 104:        "    }\n",
 105:        "\n",
 106:        "    .message-container.loaded span {\n",
 107:        "      opacity: 1;\n",
 108:        "      transform: translateY(0);\n",
 109:        "      color: #fff7cc;\n",
 110:        "    }\n",
 111:        "\n",
 112:        "    .env { color: #FFA500 !important; }\n",
 113:        "    .files-location { color: #FF99C2 !important; }\n",
 114:        "    .branch { color: #16A543 !important; }\n",
 115:        "    .fork { color: #C786D3 !important; }\n",
 116:        "    </style>\n",
 117:        "    \n",
 118:        "    <script>\n",
 119:        "    (function() {\n",
 120:        "      // Text animation\n",
 121:        "      const textContainer = document.querySelector('.text-container');\n",
 122:        "      const messageContainer = document.querySelector('.message-container');\n",
 123:        "      const textSpans = textContainer.querySelectorAll('span');\n",
 124:        "      const messageSpans = messageContainer.querySelectorAll('span');\n",
 125:        "\n",
 126:        "      textSpans.forEach((span, index) => {\n",
 127:        "        span.style.transitionDelay = `${index * 25}ms`;\n",
 128:        "      });\n",
 129:        "\n",
 130:        "      messageSpans.forEach((span, index) => {\n",
 131:        "        span.style.transitionDelay = `${index * 50}ms`;\n",
 132:        "      });\n",
 133:        "\n",
 134:        "      setTimeout(() => {\n",
 135:        "        textContainer.classList.add('loaded');\n",
 136:        "        messageContainer.classList.add('loaded');\n",
 137:        "      }, 250);\n",
 138:        "    })();\n",
 139:        "    </script>\n",
 140:        "    "
 141:       ],
 142:       "text/plain": [
 143:        "<IPython.core.display.HTML object>"
 144:       ]
 145:      },
 146:      "metadata": {},
 147:      "output_type": "display_data"
 148:     },
 149:     {
 150:      "data": {
 151:       "text/html": [
 152:        "\n",
 153:        "    <script>\n",
 154:        "    (function() {\n",
 155:        "      const container = document.querySelector('.season-container');\n",
 156:        "      const style = document.createElement('style');\n",
 157:        "      style.innerHTML = `\n",
 158:        "        .stick-particle {\n",
 159:        "          position: absolute;\n",
 160:        "          width: 2px;\n",
 161:        "          height: 15px;\n",
 162:        "          background: #ffd700;\n",
 163:        "          transform-origin: center bottom;\n",
 164:        "          opacity: 0;\n",
 165:        "          pointer-events: none;\n",
 166:        "        }\n",
 167:        "        @keyframes stick-fall {\n",
 168:        "          0% { opacity: 0; transform: translate(-50%, -50%) rotate(0) scale(0.5); }\n",
 169:        "          20% { opacity: 0.8; transform: translate(-50%, -50%) rotate(0deg) scale(1); }\n",
 170:        "          100% { opacity: 0; transform: translate(-50%, 150%) rotate(180deg) scale(0.5); }\n",
 171:        "        }\n",
 172:        "      `;\n",
 173:        "      document.head.appendChild(style);\n",
 174:        "\n",
 175:        "      let activeParticles = 0;\n",
 176:        "      const maxParticles = 25;\n",
 177:        "\n",
 178:        "      function createStick() {\n",
 179:        "        if (activeParticles >= maxParticles) return;\n",
 180:        "\n",
 181:        "        const stick = document.createElement('div');\n",
 182:        "        stick.className = 'stick-particle';\n",
 183:        "        const startX = Math.random() * 100;\n",
 184:        "        const duration = Math.random() * 4 + 3;\n",
 185:        "        const rotation = (Math.random() - 0.5) * 180;\n",
 186:        "\n",
 187:        "        stick.style.cssText = `\n",
 188:        "          left: ${startX}%;\n",
 189:        "          top: ${Math.random() * 100}%;\n",
 190:        "          animation: stick-fall ${duration}s linear forwards;\n",
 191:        "          transform: rotate(${rotation}deg);\n",
 192:        "        `;\n",
 193:        "\n",
 194:        "        activeParticles++;\n",
 195:        "        stick.addEventListener('animationend', () => {\n",
 196:        "          stick.remove();\n",
 197:        "          activeParticles--;\n",
 198:        "        });\n",
 199:        "\n",
 200:        "        container.appendChild(stick);\n",
 201:        "      }\n",
 202:        "\n",
 203:        "      const interval = setInterval(createStick, 100);\n",
 204:        "\n",
 205:        "      // Cleanup when container is removed\n",
 206:        "      const observer = new MutationObserver(() => {\n",
 207:        "        if (!document.contains(container)) {\n",
 208:        "          clearInterval(interval);\n",
 209:        "          observer.disconnect();\n",
 210:        "        }\n",
 211:        "      });\n",
 212:        "      observer.observe(document.body, { childList: true, subtree: true });\n",
 213:        "    })();\n",
 214:        "    </script>\n",
 215:        "    "
 216:       ],
 217:       "text/plain": [
 218:        "<IPython.core.display.HTML object>"
 219:       ]
 220:      },
 221:      "metadata": {},
 222:      "output_type": "display_data"
 223:     },
 224:     {
 225:      "name": "stdout",
 226:      "output_type": "stream",
 227:      "text": [
 228:       "🔄 Ensuring WebUI paths are configured for A1111...\n"
 229:      ]
 230:     }
 231:    ],
 232:    "source": [
 233:     "import os\n",
 234:     "from pathlib import Path\n",
 235:     "\n",
 236:     "# --- Start of Directory Management ---\n",
 237:     "BASE_DIR = Path(\"/teamspace/studios/this_studio\")\n",
 238:     "if os.getcwd() != str(BASE_DIR):\n",
 239:     "    print(f\"🔄 Changing directory from {os.getcwd()} to {BASE_DIR}\")\n",
 240:     "    os.chdir(BASE_DIR)\n",
 241:     "# --- End of Directory Management ---\n",
 242:     "\n",
 243:     "# @title Setup Environment.\n",
 244:     "\n",
 245:     "# Set language and branch. You can change 'en' to 'ru' for Russian.\n",
 246:     "lang, branch = 'en', 'main'\n",
 247:     "\n",
 248:     "# Define the local directory where scripts will be stored\n",
 249:     "scripts_dir = BASE_DIR / 'ANXETY' / 'scripts'\n",
 250:     "setup_script_path = scripts_dir / 'setup.py'\n",
 251:     "\n",
 252:     "# Ensure the local script directory exists\n",
 253:     "os.makedirs(scripts_dir, exist_ok=True)\n",
 254:     "\n",
 255:     "# Download the setup.py script directly from YOUR forked GitHub repository\n",
 256:     "setup_url = f'https://raw.githubusercontent.com/drf0rk/sdAIgenLightning/{branch}/scripts/setup.py'\n",
 257:     "!curl -sLo {setup_script_path} {setup_url}\n",
 258:     "\n",
 259:     "# Run the downloaded setup script to get core files and initial settings\n",
 260:     "%run {setup_script_path} --lang=$lang --branch=$branch --fork=drf0rk/sdAIgenLightning\n",
 261:     "\n",
 262:     "# --- Post-setup.py: Ensure critical modules are loaded and paths are set --- \n",
 263:     "import sys\n",
 264:     "if str(BASE_DIR / 'ANXETY' / 'modules') not in sys.path:\n",
 265:     "    sys.path.insert(0, str(BASE_DIR / 'ANXETY' / 'modules'))\n",
 266:     "if str(BASE_DIR / 'ANXETY' / 'scripts') not in sys.path:\n",
 267:     "    sys.path.insert(0, str(BASE_DIR / 'ANXETY' / 'scripts'))\n",
 268:     "\n",
 269:     "import json_utils as js\n",
 270:     "from webui_utils import _set_webui_paths, SHARED_MODEL_BASE # Import specific utilities\n",
 271:     "\n",
 272:     "# Force update WEBUI paths using the UI selected in settings.json (or default 'A1111')\n",
 273:     "# This ensures `model_dir`, `vae_dir`, etc., are correctly pointing to SHARED_MODEL_BASE\n",
 274:     "current_ui_selection = js.read(BASE_DIR / 'ANXETY' / 'settings.json', 'WEBUI.current', 'A1111')\n",
 275:     "print(f\"🔄 Ensuring WebUI paths are configured for {current_ui_selection}...\")\n",
 276:     "_set_webui_paths(current_ui_selection)\n",
 277:     "\n",
 278:     "# Re-load settings after forcing _set_webui_paths to ensure the latest paths are used.\n",
 279:     "settings = js.read(BASE_DIR / 'ANXETY' / 'settings.json')\n",
 280:     "\n",
 281:     "# Define global path variables explicitly in the notebook's scope from settings\n",
 282:     "# These will be used by subsequent cells, ensuring consistency.\n",
 283:     "WEBUI_PATH = Path(settings.get('WEBUI', {}).get('webui_path', str(BASE_DIR / current_ui_selection)))\n",
 284:     "model_dir = Path(settings.get('WEBUI', {}).get('model_dir', str(SHARED_MODEL_BASE / 'Stable-diffusion')))\n",
 285:     "vae_dir = Path(settings.get('WEBUI', {}).get('vae_dir', str(SHARED_MODEL_BASE / 'vae')))\n",
 286:     "lora_dir = Path(settings.get('WEBUI', {}).get('lora_dir', str(SHARED_MODEL_BASE / 'Lora')))\n",
 287:     "embed_dir = Path(settings.get('WEBUI', {}).get('embed_dir', str(SHARED_MODEL_BASE / 'embeddings')))\n",
 288:     "control_dir = Path(settings.get('WEBUI', {}).get('control_dir', str(SHARED_MODEL_BASE / 'ControlNet')))\n",
 289:     "adetailer_dir = Path(settings.get('WEBUI', {}).get('adetailer_dir', str(SHARED_MODEL_BASE / 'adetailer')))\n",
 290:     "extension_dir = Path(settings.get('WEBUI', {}).get('extension_dir', str(WEBUI_PATH / 'extensions')))\n",
 291:     "\n",
 292:     "# --- Ensure we are back in BASE_DIR at the end of the cell ---\n",
 293:     "if os.getcwd() != str(BASE_DIR):\n",
 294:     "    os.chdir(BASE_DIR)\n",
 295:     "# --- End of Directory Management ---\n"
 296:    ]
 297:   },
 298:   {
 299:    "cell_type": "markdown",
 300:    "id": "6d2b405e-8fb7-497a-8f15-de2b6e5d91a9",
 301:    "metadata": {},
 302:    "source": [
 303:     "2. Widgets 🔽\n",
 304:     "\n",
 305:     "This cell will load the interactive widgets. Since setup.py (executed in the previous cell) has already downloaded the patched widgets-en.py (or widgets-ru.py) to scripts_dir, this command will now use your modified version with the LoRA dropdown."
 306:    ]
 307:   },
 308:   {
 309:    "cell_type": "code",
 310:    "execution_count": 2,
 311:    "id": "3ffca5a8-6603-4463-b057-f3a6b41a9ae1",
 312:    "metadata": {},
 313:    "outputs": [
 314:     {
 315:      "data": {
 316:       "text/html": [
 317:        "<style>@import url('https://fonts.googleapis.com/css2?family=Shantell+Sans:ital,wght@0,300..800;1,300..800&family=Tiny5&display=swap');\n",
 318:        "\n",
 319:        ":root {\n",
 320:        "    /* Accent Color */\n",
 321:        "    --aw-accent-color: #ff97ef;\n",
 322:        "\n",
 323:        "    /* Text - Fonts */\n",
 324:        "    --aw-font-family-primary: \"Shantell Sans\", serif;\n",
 325:        "    --aw-font-family-secondary: \"Tiny5\", sans-serif;\n",
 326:        "    --aw-color-text-primary: #f0f8ff;\n",
 327:        "    --aw-text-size: 14px;\n",
 328:        "    --aw-text-size-small: 13px;\n",
 329:        "\n",
 330:        "    /* Container */\n",
 331:        "    --aw-container-bg: #232323;\n",
 332:        "    --aw-container-border: 2px solid rgba(0, 0, 0, 0.4);\n",
 333:        "\n",
 334:        "    /* Inputs */\n",
 335:        "    --aw-input-bg: #1c1c1c;\n",
 336:        "    --aw-input-bg-hover: #262626;\n",
 337:        "    --aw-input-border: 1px solid #262626;\n",
 338:        "    --aw-input-border-focus: #006ee5;\n",
 339:        "\n",
 340:        "    /* Checkboxes */\n",
 341:        "    --aw-checkbox-unchecked-bg: #20b2aa;\n",
 342:        "    --aw-checkbox-checked-bg: #2196f3;\n",
 343:        "    --aw-checkbox-inpaint-bg: #bbca53;\n",
 344:        "    --aw-checkbox-sdxl-bg: #ea861a;\n",
 345:        "    --aw-checkbox-empowerment-bg: #df6b91;\n",
 346:        "    --aw-checkbox-handle-bg: white;\n",
 347:        "\n",
 348:        "    /* Popup */\n",
 349:        "    --aw-popup-bg: rgba(255, 255, 255, 0.05);\n",
 350:        "    --aw-popup-color: #ffffff;\n",
 351:        "    --aw-popup-border: 2px solid rgba(255, 255, 255, 0.45);\n",
 352:        "    --aw-popup-sample-bg: rgba(255, 255, 255, 0.2);\n",
 353:        "    --aw-popup-sample-color: #c6e2ff;\n",
 354:        "    --aw-popup-sample-border: 2px solid rgba(255, 255, 255, 0.2);\n",
 355:        "\n",
 356:        "    /* Term Colors (Popup) */\n",
 357:        "    --aw-term-sample-label: #dbafff;\n",
 358:        "    --aw-term-braces: #ffff00;\n",
 359:        "    --aw-term-extension: #eb934b;\n",
 360:        "    --aw-term-filename: #ffdba7;\n",
 361:        "    --aw-term-required: #ff9999;\n",
 362:        "\n",
 363:        "    /* Scrollbar */\n",
 364:        "    --aw-scrollbar-width: 0.65rem;\n",
 365:        "    --aw-scrollbar-thumb-bg: #475254;\n",
 366:        "    --aw-scrollbar-track-bg: #111111;\n",
 367:        "    --aw-scrollbar-thumb-hover: var(--aw-accent-color);\n",
 368:        "\n",
 369:        "    /* Buttons */\n",
 370:        "    --aw-button-gradient: radial-gradient(circle at top left, purple 10%, violet 90%);\n",
 371:        "    --aw-button-input-gradient: radial-gradient(circle at top left, var(--aw-input-bg));\n",
 372:        "    --aw-button-save-hover: radial-gradient(circle at top left, purple 10%, #93ac47 90%);\n",
 373:        "    --aw-button-api-hover: radial-gradient(circle at top left, purple 10%, #1d94bb 90%);\n",
 374:        "}\n",
 375:        "\n",
 376:        "\n",
 377:        "/* General Styles */\n",
 378:        "\n",
 379:        ".header {\n",
 380:        "    display: inline-block;\n",
 381:        "    font-size: 20px;\n",
 382:        "    font-weight: 650;\n",
 383:        "    color: var(--aw-accent-color);\n",
 384:        "    margin-bottom: 10px;\n",
 385:        "    user-select: none;\n",
 386:        "    cursor: default;\n",
 387:        "    text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);\n",
 388:        "}\n",
 389:        "\n",
 390:        "hr {\n",
 391:        "    margin: 4px 0;\n",
 392:        "    background-color: grey;\n",
 393:        "    border-color: grey;\n",
 394:        "    opacity: 0.25;\n",
 395:        "}\n",
 396:        "a {\n",
 397:        "    color: inherit;\n",
 398:        "    text-decoration: none;\n",
 399:        "}\n",
 400:        "\n",
 401:        "\n",
 402:        "/* == Special fixes for IpyWidgets == */\n",
 403:        "/* Remove Shit-Spacing for HTML-Widgets (button) */\n",
 404:        ".widget-html:has(.button),\n",
 405:        ".widget-html-content:has(.button) {\n",
 406:        "    padding: 0;\n",
 407:        "    margin: 0;\n",
 408:        "}\n",
 409:        "\n",
 410:        "/* Fix Vertical Centering */\n",
 411:        ".widget-hbox,\n",
 412:        ".jupyter-widgets label {\n",
 413:        "    display: flex;\n",
 414:        "    align-items: center;\n",
 415:        "}\n",
 416:        "\n",
 417:        "/* Fix Checkbox Width */\n",
 418:        ".widget-checkbox {\n",
 419:        "    width: auto;\n",
 420:        "    display: inline-flex;\n",
 421:        "    min-width: unset;\n",
 422:        "}\n",
 423:        "\n",
 424:        "\n",
 425:        "/* Special Styles (ScrollBars) */\n",
 426:        "\n",
 427:        "::selection {\n",
 428:        "    background: #3d4142;\n",
 429:        "}\n",
 430:        "::-moz-selection { /* Code for Firefox */\n",
 431:        "    background: #3d4142;\n",
 432:        "}\n",
 433:        "\n",
 434:        "/* === ScrollBar (For TextArea) === */\n",
 435:        ".widget-textarea textarea::-webkit-scrollbar {\n",
 436:        "    width: var(--aw-scrollbar-width);\n",
 437:        "    height: var(--aw-scrollbar-width);\n",
 438:        "}\n",
 439:        ".widget-textarea textarea::-webkit-scrollbar-thumb {\n",
 440:        "    background: var(--aw-scrollbar-thumb-bg) !important;\n",
 441:        "    border: 3px solid var(--aw-scrollbar-track-bg);\n",
 442:        "    border-radius: 16px;\n",
 443:        "}\n",
 444:        ".widget-textarea textarea::-webkit-scrollbar-thumb:hover {\n",
 445:        "    background: var(--aw-scrollbar-thumb-hover) !important;\n",
 446:        "}\n",
 447:        ".widget-textarea textarea::-webkit-scrollbar-track,\n",
 448:        ".widget-textarea textarea::-webkit-scrollbar-corner {\n",
 449:        "    background: var(--aw-scrollbar-track-bg) !important;\n",
 450:        "    border-radius: 0 8px 8px 0;\n",
 451:        "}\n",
 452:        "/* FireFox Styles */\n",
 453:        "@-moz-document url-prefix() {\n",
 454:        "    .widget-textarea textarea {\n",
 455:        "        scrollbar-width: auto;\n",
 456:        "        scrollbar-color: var(--aw-scrollbar-thumb-bg) var(--aw-scrollbar-track-bg);\n",
 457:        "    }\n",
 458:        "}\n",
 459:        "\n",
 460:        "\n",
 461:        "/* Text FONTs */\n",
 462:        "\n",
 463:        ".info,\n",
 464:        ".popup,\n",
 465:        ".button,\n",
 466:        ".header,\n",
 467:        ".widget-button,\n",
 468:        ".widget-text label,\n",
 469:        ".widget-checkbox label,\n",
 470:        ".widget-dropdown label,\n",
 471:        ".widget-dropdown select,\n",
 472:        ".widget-textarea textarea,\n",
 473:        ".widget-text input[type=\"text\"] {\n",
 474:        "    font-family: var(--aw-font-family-primary);\n",
 475:        "    font-optical-sizing: auto;\n",
 476:        "}\n",
 477:        "\n",
 478:        "\n",
 479:        "/* Element text style */\n",
 480:        "\n",
 481:        ".widget-text,\n",
 482:        ".widget-button,\n",
 483:        ".widget-text label,\n",
 484:        ".widget-checkbox label,\n",
 485:        ".widget-dropdown label,\n",
 486:        ".widget-dropdown select,\n",
 487:        ".widget-textarea textarea,\n",
 488:        ".widget-text input[type=\"text\"] {\n",
 489:        "    font-style: normal;\n",
 490:        "    font-size: var(--aw-text-size);\n",
 491:        "    color: var(--aw-color-text-primary) !important;\n",
 492:        "    user-select: none;\n",
 493:        "}\n",
 494:        ".widget-text input[type=\"text\"]::placeholder {\n",
 495:        "    color: grey;\n",
 496:        "    font-size: var(--aw-text-size);\n",
 497:        "}\n",
 498:        "\n",
 499:        "/* TextArea */\n",
 500:        ".widget-textarea textarea,\n",
 501:        ".widget-textarea textarea::placeholder {\n",
 502:        "    font-size: var(--aw-text-size-small);\n",
 503:        "}\n",
 504:        "\n",
 505:        "\n",
 506:        "/* Container style */\n",
 507:        "\n",
 508:        ".mainContainer * { /* Fix For Containers Shadow */\n",
 509:        "    overflow: visible !important;\n",
 510:        "}\n",
 511:        ".mainContainer {\n",
 512:        "    padding: 5px;\n",
 513:        "    gap: 5px;\n",
 514:        "}\n",
 515:        "\n",
 516:        ".container {\n",
 517:        "    position: relative;\n",
 518:        "    width: 1080px;\n",
 519:        "    padding: 10px 15px;\n",
 520:        "    background-color: var(--aw-container-bg);\n",
 521:        "    border: var(--aw-container-border);\n",
 522:        "    border-radius: 16px;\n",
 523:        "    box-shadow: 0 0 15px rgba(0, 0, 0, 0.35), inset 0 0 10px rgba(0, 0, 0, 0.3);\n",
 524:        "    overflow: hidden !important;\n",
 525:        "}\n",
 526:        ".container::after {\n",
 527:        "    content: \"ANXETY\";\n",
 528:        "    position: absolute;\n",
 529:        "    top: 5px;\n",
 530:        "    right: 10px;\n",
 531:        "    color: rgba(0, 0, 0, 0.3);\n",
 532:        "    font-family: var(--aw-font-family-secondary);\n",
 533:        "    font-optical-sizing: auto;\n",
 534:        "    font-weight: 750;\n",
 535:        "    font-size: 24px;\n",
 536:        "}\n",
 537:        "\n",
 538:        ".container_cdl {\n",
 539:        "    height: 55px;\n",
 540:        "    transition: all 0.5s cubic-bezier(0.785, 0.135, 0.15, 0.85);\n",
 541:        "}\n",
 542:        ".container_cdl.expanded {\n",
 543:        "    height: 305px;\n",
 544:        "}\n",
 545:        "\n",
 546:        "/* GDrive Button */\n",
 547:        ".gdrive-btn {\n",
 548:        "    align-self: flex-start;\n",
 549:        "    min-width: 48px;\n",
 550:        "    min-height: 48px;\n",
 551:        "    margin: 0 !important;\n",
 552:        "    margin-left: 15px !important; /* SPACE */\n",
 553:        "    padding: 0 !important;\n",
 554:        "    background-size: 70%;\n",
 555:        "    background-position: center;\n",
 556:        "    background-repeat: no-repeat;\n",
 557:        "    background-image: url('https://upload.wikimedia.org/wikipedia/commons/1/12/Google_Drive_icon_%282020%29.svg');\n",
 558:        "    background-color: var(--aw-container-bg);\n",
 559:        "    border: var(--aw-container-border);\n",
 560:        "    border-radius: 8px;\n",
 561:        "    box-shadow: 0 0 15px rgba(0, 0, 0, 0.35), inset 0 0 10px rgba(0, 0, 0, 0.3) !important;\n",
 562:        "    cursor: pointer;\n",
 563:        "    outline: none;\n",
 564:        "    transition: all 0.15s ease;\n",
 565:        "}\n",
 566:        ".gdrive-btn.active {\n",
 567:        "    background-color: #006d33;\n",
 568:        "    border-color: #00d062;\n",
 569:        "    transform: scale(0.9) !important;\n",
 570:        "}\n",
 571:        "\n",
 572:        "\n",
 573:        "/* Input field styles */\n",
 574:        "\n",
 575:        ".widget-dropdown select,\n",
 576:        ".widget-text input[type=\"text\"],\n",
 577:        ".widget-textarea textarea {\n",
 578:        "    height: 30px;\n",
 579:        "    margin: 0 !important;\n",
 580:        "    background-color: var(--aw-input-bg);\n",
 581:        "    border: var(--aw-input-border);\n",
 582:        "    border-radius: 10px;\n",
 583:        "    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);\n",
 584:        "    transition: all 0.25s ease-in-out;\n",
 585:        "}\n",
 586:        ".widget-textarea textarea {\n",
 587:        "    height: 200px;\n",
 588:        "    resize: none;\n",
 589:        "}\n",
 590:        "\n",
 591:        ".widget-dropdown select:focus,\n",
 592:        ".widget-text input[type=\"text\"]:focus,\n",
 593:        ".widget-textarea textarea:focus {\n",
 594:        "    border-color: var(--aw-input-border-focus);\n",
 595:        "}\n",
 596:        "\n",
 597:        ".widget-dropdown select:hover,\n",
 598:        ".widget-text input[type=\"text\"]:hover {\n",
 599:        "    transform: scale(1.003);\n",
 600:        "    background-color: var(--aw-input-bg-hover);\n",
 601:        "    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);\n",
 602:        "}\n",
 603:        ".widget-dropdown option {\n",
 604:        "    background-color: var(--aw-input-bg);\n",
 605:        "}\n",
 606:        "\n",
 607:        "/* Animation when switching empowerment mode */\n",
 608:        ".widget-text.empowerment-text-field,\n",
 609:        ".widget-textarea.empowerment-output  {\n",
 610:        "    transition: all 0.3s ease;\n",
 611:        "    overflow: hidden;\n",
 612:        "}\n",
 613:        "/* Standard state */\n",
 614:        ".widget-text.empowerment-text-field {\n",
 615:        "    opacity: 1;\n",
 616:        "    max-height: 30px;\n",
 617:        "    visibility: visible;\n",
 618:        "}\n",
 619:        ".widget-textarea.empowerment-output {\n",
 620:        "    opacity: 1;\n",
 621:        "    max-height: 200px;\n",
 622:        "    visibility: visible;\n",
 623:        "}\n",
 624:        "/* Hidden state */\n",
 625:        ".widget-text.empowerment-text-field.hidden,\n",
 626:        ".widget-textarea.empowerment-output.hidden {\n",
 627:        "    opacity: 0;\n",
 628:        "    max-height: 0;\n",
 629:        "    margin-top: 0;\n",
 630:        "    margin-bottom: 0;\n",
 631:        "    visibility: hidden;\n",
 632:        "}\n",
 633:        "\n",
 634:        "\n",
 635:        "/* Slider Checkbox style */\n",
 636:        "\n",
 637:        ".widget-checkbox input[type=\"checkbox\"] {\n",
 638:        "    appearance: none;\n",
 639:        "    position: relative;\n",
 640:        "    width: 40px;\n",
 641:        "    height: 20px;\n",
 642:        "    background-color: var(--aw-checkbox-unchecked-bg);\n",
 643:        "    border: none;\n",
 644:        "    border-radius: 10px;\n",
 645:        "    cursor: pointer;\n",
 646:        "    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3);\n",
 647:        "    transition: background-color 0.3s cubic-bezier(0.785, 0.135, 0.15, 0.85);\n",
 648:        "}\n",
 649:        ".widget-checkbox input[type=\"checkbox\"]:checked {\n",
 650:        "    background-color: var(--aw-checkbox-checked-bg);\n",
 651:        "}\n",
 652:        ".inpaint input[type=\"checkbox\"]:checked {\n",
 653:        "    background-color: var(--aw-checkbox-inpaint-bg);\n",
 654:        "}\n",
 655:        ".sdxl input[type=\"checkbox\"]:checked {\n",
 656:        "    background-color: var(--aw-checkbox-sdxl-bg);\n",
 657:        "}\n",
 658:        ".empowerment input[type=\"checkbox\"]:checked {\n",
 659:        "    background-color: var(--aw-checkbox-empowerment-bg);\n",
 660:        "}\n",
 661:        "\n",
 662:        ".widget-checkbox input[type=\"checkbox\"]:before {\n",
 663:        "    content: '';\n",
 664:        "    position: absolute;\n",
 665:        "    top: 50%;\n",
 666:        "    left: 4px;\n",
 667:        "    width: 12px;\n",
 668:        "    height: 12px;\n",
 669:        "    background-color: var(--aw-checkbox-handle-bg);\n",
 670:        "    border-radius: inherit;\n",
 671:        "    box-shadow: 0 0 8px rgba(0, 0, 0, 0.3);\n",
 672:        "    transform: translateY(-50%);\n",
 673:        "    transition: all 0.25s cubic-bezier(0.785, 0.135, 0.15, 0.85);\n",
 674:        "}\n",
 675:        ".widget-checkbox input[type=\"checkbox\"]:checked:before {\n",
 676:        "    left: 20px;\n",
 677:        "    width: 16px;\n",
 678:        "    height: 16px;\n",
 679:        "}\n",
 680:        "\n",
 681:        "\n",
 682:        "/* Popup style of `INFO` window */\n",
 683:        "\n",
 684:        ".info {\n",
 685:        "    position: absolute;\n",
 686:        "    display: inline-block;\n",
 687:        "    top: -5px;\n",
 688:        "    right: 90px;\n",
 689:        "    color: grey;\n",
 690:        "    font-size: var(--aw-text-size);\n",
 691:        "    opacity: 0;\n",
 692:        "    transition: all 0.25s;\n",
 693:        "    user-select: none;\n",
 694:        "}\n",
 695:        "\n",
 696:        ".popup {\n",
 697:        "    position: absolute;\n",
 698:        "    top: 120px;\n",
 699:        "    padding: 12px;\n",
 700:        "    color: var(--aw-popup-color);\n",
 701:        "    font-size: 16px;\n",
 702:        "    text-align: center;\n",
 703:        "    background-color: var(--aw-popup-bg);\n",
 704:        "    backdrop-filter: blur(8px);\n",
 705:        "    border: var(--aw-popup-border);\n",
 706:        "    border-radius: 10px;\n",
 707:        "    box-shadow: 0 0 50px rgba(0, 0, 0, 0.5);\n",
 708:        "    opacity: 0;\n",
 709:        "    transform: rotate(-5deg);\n",
 710:        "    pointer-events: none;\n",
 711:        "    z-index: 999;\n",
 712:        "    transition: all 0.25s cubic-bezier(0.175, 0.885, 0.30, 1.275);\n",
 713:        "}\n",
 714:        "\n",
 715:        ".sample {\n",
 716:        "    margin-top: 25px;\n",
 717:        "    padding: 10px 100px;\n",
 718:        "    color: var(--aw-popup-sample-color);\n",
 719:        "    background-color: var(--aw-popup-sample-bg);\n",
 720:        "    border: var(--aw-popup-sample-border);\n",
 721:        "    border-radius: 10px;\n",
 722:        "    white-space: nowrap;\n",
 723:        "}\n",
 724:        "\n",
 725:        "/* For Empowerment */\n",
 726:        ".empowerment {\n",
 727:        "    position: absolute;\n",
 728:        "    top: 10px;\n",
 729:        "    left: 300px;\n",
 730:        "    opacity: 0;\n",
 731:        "    pointer-events: none;\n",
 732:        "    transition: all 0.25s;\n",
 733:        "}\n",
 734:        "\n",
 735:        ".info.showed,\n",
 736:        ".empowerment.showed {\n",
 737:        "    opacity: 1;\n",
 738:        "    pointer-events: auto;\n",
 739:        "}\n",
 740:        "\n",
 741:        ".info.showed:hover + .popup {\n",
 742:        "    top: 35px;\n",
 743:        "    opacity: 1;\n",
 744:        "    transform: rotate(0deg);\n",
 745:        "}\n",
 746:        "\n",
 747:        "/* Term Colors */\n",
 748:        ".sample_label { color: var(--aw-term-sample-label); }\n",
 749:        ".braces { color: var(--aw-term-braces); }\n",
 750:        ".extension { color: var(--aw-term-extension); }\n",
 751:        ".file_name { color: var(--aw-term-filename); }\n",
 752:        ".required { color: var(--aw-term-required); }\n",
 753:        "\n",
 754:        "\n",
 755:        "/* Button styles */\n",
 756:        "\n",
 757:        ".button {\n",
 758:        "    margin: 0;\n",
 759:        "    color: var(--aw-color-text-primary);\n",
 760:        "    font-size: 15px;\n",
 761:        "    box-sizing: border-box !important;\n",
 762:        "    white-space: nowrap;\n",
 763:        "    cursor: pointer;\n",
 764:        "    user-select: none;\n",
 765:        "    overflow: hidden !important;\n",
 766:        "    transition: background 0.5s ease;\n",
 767:        "}\n",
 768:        ".button_save {\n",
 769:        "    font-weight: 650;\n",
 770:        "    width: 120px;\n",
 771:        "    height: 35px;\n",
 772:        "    background-image: var(--aw-button-gradient);\n",
 773:        "    background-size: 200% 100%;\n",
 774:        "    background-position: left bottom;\n",
 775:        "    border-radius: 15px;\n",
 776:        "}\n",
 777:        ".button_api {\n",
 778:        "    position: relative;\n",
 779:        "    font-size: 12px;\n",
 780:        "    display: inline-flex;\n",
 781:        "    align-items: center;\n",
 782:        "    justify-content: center;\n",
 783:        "    height: 30px !important;\n",
 784:        "    min-width: 45px;\n",
 785:        "    margin-left: 4px; /* SPACE */\n",
 786:        "    padding: 0;\n",
 787:        "    background-image: var(--aw-button-input-gradient);\n",
 788:        "    background-size: 200% 100%;\n",
 789:        "    background-position: left bottom;\n",
 790:        "    border: var(--aw-input-border);\n",
 791:        "    border-radius: 10px;\n",
 792:        "    box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);\n",
 793:        "    transition: all 0.4s ease;\n",
 794:        "}\n",
 795:        ".button_api .icon {\n",
 796:        "    position: absolute;\n",
 797:        "    left: 50%;\n",
 798:        "    transform: translateX(-50%);\n",
 799:        "    transition: all 0.4s ease;\n",
 800:        "    pointer-events: none;\n",
 801:        "}\n",
 802:        ".button_api .text {\n",
 803:        "    display: inline-block;\n",
 804:        "    max-width: 0;\n",
 805:        "    opacity: 0;\n",
 806:        "    pointer-events: none;\n",
 807:        "    transition: all 0.4s ease;\n",
 808:        "}\n",
 809:        "\n",
 810:        ".button:hover {\n",
 811:        "    background-position: right bottom;\n",
 812:        "}\n",
 813:        ".button_save:hover {\n",
 814:        "    background-image: var(--aw-button-save-hover);\n",
 815:        "}\n",
 816:        ".button_api:hover {\n",
 817:        "    max-width: 300px;\n",
 818:        "    padding: 0 12px 0 32px;\n",
 819:        "    background-image: var(--aw-button-api-hover);\n",
 820:        "}\n",
 821:        ".button_api:hover .icon {\n",
 822:        "    left: 15px;\n",
 823:        "    transform: translateX(0);\n",
 824:        "}\n",
 825:        ".button_api:hover .text {\n",
 826:        "    max-width: 200px;\n",
 827:        "    padding-left: 6px;\n",
 828:        "    opacity: 1;\n",
 829:        "}\n",
 830:        "\n",
 831:        "/* Removes ugly stroke from widget buttons. */\n",
 832:        ".button:active {\n",
 833:        "    filter: brightness(0.75) !important;\n",
 834:        "}\n",
 835:        ".jupyter-widgets.lm-Widget:focus {\n",
 836:        "    outline: none;\n",
 837:        "}\n",
 838:        "\n",
 839:        "\n",
 840:        "/* Animation of elements */\n",
 841:        "\n",
 842:        ".container,\n",
 843:        ".gdrive-btn,\n",
 844:        ".button_save {\n",
 845:        "    animation: showedWidgets 0.8s forwards ease;\n",
 846:        "}\n",
 847:        "\n",
 848:        ".container.hide,\n",
 849:        ".gdrive-btn.hide,\n",
 850:        ".button_save.hide {\n",
 851:        "    animation: hideWidgets 0.5s forwards ease;\n",
 852:        "}\n",
 853:        "\n",
 854:        "@keyframes showedWidgets {\n",
 855:        "    0% {\n",
 856:        "        transform: translate3d(-65%, 15%, 0) scale(0) rotate(15deg);\n",
 857:        "        filter: blur(25px) brightness(0.3);\n",
 858:        "        opacity: 0;\n",
 859:        "    }\n",
 860:        "    100% {\n",
 861:        "        transform: translate3d(0, 0, 0) scale(1) rotate(0deg);\n",
 862:        "        filter: blur(0) brightness(1);\n",
 863:        "        opacity: 1;\n",
 864:        "    }\n",
 865:        "}\n",
 866:        "\n",
 867:        "@keyframes hideWidgets {\n",
 868:        "    0% {\n",
 869:        "        transform: translate3d(0, 0, 0) scale(1) rotate3d(1, 0, 0, 0deg);\n",
 870:        "        filter: blur(0) brightness(1);\n",
 871:        "        opacity: 1;\n",
 872:        "    }\n",
 873:        "    100% {\n",
 874:        "        transform: translate3d(0, 5%, 0) scale(0.9) rotate3d(1, 0, 0, 90deg);\n",
 875:        "        filter: blur(15px) brightness(0.5);\n",
 876:        "        opacity: 0;\n",
 877:        "    }\n",
 878:        "}</style>"
 879:       ],
 880:       "text/plain": [
 881:        "<IPython.core.display.HTML object>"
 882:       ]
 883:      },
 884:      "metadata": {},
 885:      "output_type": "display_data"
 886:     },
 887:     {
 888:      "data": {
 889:       "application/vnd.jupyter.widget-view+json": {
 890:        "model_id": "c694880df56949ebac4503b9834196bd",
 891:        "version_major": 2,
 892:        "version_minor": 0
 893:       },
 894:       "text/plain": [
 895:        "VBox(children=(HBox(children=(VBox(children=(VBox(children=(HTML(value='<div class=\"header\">Model Selection (C…"
 896:       ]
 897:      },
 898:      "metadata": {},
 899:      "output_type": "display_data"
 900:     }
 901:    ],
 902:    "source": [
 903:     "import os\n",
 904:     "from pathlib import Path\n",
 905:     "\n",
 906:     "# --- Start of Directory Management ---\n",
 907:     "BASE_DIR = Path(\"/teamspace/studios/this_studio\")\n",
 908:     "if os.getcwd() != str(BASE_DIR):\n",
 909:     "    print(f\"🔄 Changing directory from {os.getcwd()} to {BASE_DIR}\")\n",
 910:     "    os.chdir(BASE_DIR)\n",
 911:     "# --- End of Directory Management ---\n",
 912:     "\n",
 913:     "# Define scripts_dir using BASE_DIR for consistency\n",
 914:     "scripts_dir = BASE_DIR / 'ANXETY' / 'scripts'\n",
 915:     "lang = 'en' # Ensure lang is defined, typically from the first cell\n",
 916:     "\n",
 917:     "# Model selection, vae, control-net and more.\n",
 918:     "%run {scripts_dir}/{lang}/widgets-{lang}.py\n",
 919:     "\n",
 920:     "# --- Ensure we are back in BASE_DIR at the end of the cell ---\n",
 921:     "if os.getcwd() != str(BASE_DIR):\n",
 922:     "    os.chdir(BASE_DIR)\n",
 923:     "# --- End of Directory Management ---\n"
 924:    ]
 925:   },
 926:   {
 927:    "cell_type": "markdown",
 928:    "id": "a538fedf-c7b8-478b-8cfd-3a68ee8bd743",
 929:    "metadata": {},
 930:    "source": [
 931:     "3. Downloading 🔽\n",
 932:     "\n",
 933:     "This cell initiates the downloading process for models, VAEs, extensions, and other necessary components. It will use the patched downloading-en.py (or downloading-ru.py) from your fork, ensuring downloads go to your centralized model storage location."
 934:    ]
 935:   },
 936:   {
 937:    "cell_type": "code",
 938:    "execution_count": 3,
 939:    "id": "456ba90a-3a39-49d1-bd97-6ad4967ef838",
 940:    "metadata": {},
 941:    "outputs": [
 942:     {
 943:      "name": "stdout",
 944:      "output_type": "stream",
 945:      "text": [
 946:       "📦 Processing download selections...\n",
 947:       "DEBUG: Selected Models: ['1. D5K6.0']\n",
 948:       "DEBUG: Selected VAEs: ['1. vae-ft-mse-840000-ema-pruned | 840000 | 840k SD1.5 VAE - vae-ft-mse-840k']\n",
 949:       "✨ Downloader Version: 2025.06.09.8_final_patch\n",
 950:       "📦 Processing download selections...\n",
 951:       "Starting downloads...\n",
 952:       "\u001b[35m【\u001b[0m#\u001b[32m61abfb\u001b[0m 1.7GiB/1.9GiB\u001b[36m(90%)\u001b[0m CN:\u001b[34m16\u001b[0m DL:\u001b[32m284MiB\u001b[0m\u001b[35m】\u001b[0m                                                                                  \n",
 953:       "61abfb|\u001b[32mOK\u001b[0m  |   283MiB/s|/teamspace/studios/this_studio/sd_models_shared/Stable-diffusion/D5K6.0.safetensors\n",
 954:       "\u001b[35m【\u001b[0m#\u001b[32m716d1f\u001b[0m 169MiB/319MiB\u001b[36m(53%)\u001b[0m CN:\u001b[34m16\u001b[0m DL:\u001b[32m206MiB\u001b[0m\u001b[35m】\u001b[0m                                                                                  \n",
 955:       "716d1f|\u001b[32mOK\u001b[0m  |   229MiB/s|/teamspace/studios/this_studio/sd_models_shared/vae/vaeFtMse840000EmaPruned_vaeFtMse840k.safetensors\n",
 956:       "\u001b[35m【\u001b[0m#\u001b[32mbf6161\u001b[0m 297MiB/297MiB\u001b[36m(99%)\u001b[0m CN:\u001b[34m2\u001b[0m DL:\u001b[32m205MiB\u001b[0m\u001b[35m】\u001b[0m                                                                                   \n",
 957:       "bf6161|\u001b[32mOK\u001b[0m  |   204MiB/s|/teamspace/studios/this_studio/sd_models_shared/Lora/concept-female_masturbation-v2.safetensors\n",
 958:       "\u001b[35m【\u001b[0m#\u001b[32m7aa852\u001b[0m 506MiB/689MiB\u001b[36m(73%)\u001b[0m CN:\u001b[34m16\u001b[0m DL:\u001b[32m284MiB\u001b[0m\u001b[35m】\u001b[0m                                                                                  \n",
 959:       "7aa852|\u001b[32mOK\u001b[0m  |   286MiB/s|/teamspace/studios/this_studio/sd_models_shared/ControlNet/control_v11p_sd15_openpose_fp16.safetensors\n",
 960:       "fb6abd|\u001b[32mOK\u001b[0m  |   1.8MiB/s|/teamspace/studios/this_studio/sd_models_shared/ControlNet/control_v11p_sd15_openpose_fp16.yaml\n",
 961:       "🏁 Download processing complete!\n"
 962:      ]
 963:     }
 964:    ],
 965:    "source": [
 966:     "import os\n",
 967:     "from pathlib import Path\n",
 968:     "import json_utils as js # Import json_utils to read settings\n",
 969:     "# This import needs to happen after sys.path is set,\n",
 970:     "# so we'll assume it's set by the first cell's execution,\n",
 971:     "# or we can add it here explicitly if needed.\n",
 972:     "# For simplicity, if json_utils isn't found here, try to load its path first.\n",
 973:     "\n",
 974:     "# --- Start of Directory Management ---\n",
 975:     "BASE_DIR = Path(\"/teamspace/studios/this_studio\")\n",
 976:     "if os.getcwd() != str(BASE_DIR):\n",
 977:     "    print(f\"🔄 Changing directory from {os.getcwd()} to {BASE_DIR}\")\n",
 978:     "    os.chdir(BASE_DIR)\n",
 979:     "# --- End of Directory Management ---\n",
 980:     "\n",
 981:     "# Define scripts_dir and lang using BASE_DIR for consistency\n",
 982:     "scripts_dir = BASE_DIR / 'ANXETY' / 'scripts'\n",
 983:     "lang = 'en' # Ensure lang is defined, typically from the first cell\n",
 984:     "\n",
 985:     "# --- Temporary Code for DEBUGging in Notebook Cell ---\n",
 986:     "# Load settings from settings.json to get the current widget values\n",
 987:     "# This will reflect what was saved by the Widgets cell\n",
 988:     "SETTINGS_PATH = BASE_DIR / 'ANXETY' / 'settings.json'\n",
 989:     "try:\n",
 990:     "    # Ensure modules path is set if not already from the setup cell\n",
 991:     "    anxety_modules_path = BASE_DIR / 'ANXETY' / 'modules'\n",
 992:     "    if str(anxety_modules_path) not in sys.path:\n",
 993:     "        sys.path.insert(0, str(anxety_modules_path))\n",
 994:     "    import json_utils as js\n",
 995:     "    settings_data = js.read(SETTINGS_PATH)\n",
 996:     "    model_selections = settings_data.get('WIDGETS', {}).get('model', ('none',))\n",
 997:     "    vae_selections = settings_data.get('WIDGETS', {}).get('vae', ('none',))\n",
 998:     "except ImportError:\n",
 999:     "    print(\"Warning: Could not import json_utils. Debugging info might be incomplete.\")\n",
1000:     "    model_selections = (\"Error: json_utils missing\",)\n",
1001:     "    vae_selections = (\"Error: json_utils missing\",)\n",
1002:     "except Exception as e:\n",
1003:     "    print(f\"Warning: Could not read settings for debugging: {e}\")\n",
1004:     "    model_selections = (\"Error reading settings\",)\n",
1005:     "    vae_selections = (\"Error reading settings\",)\n",
1006:     "\n",
1007:     "print('📦 Processing download selections...')\n",
1008:     "print(f\"DEBUG: Selected Models: {model_selections}\")\n",
1009:     "print(f\"DEBUG: Selected VAEs: {vae_selections}\")\n",
1010:     "# --- End of Temporary Code for DEBUGging ---\n",
1011:     "\n",
1012:     "# Downloading libraries, repos, models and more.\n",
1013:     "# The downloading script will now correctly use the global model_dir, vae_dir, etc.,\n",
1014:     "# which are already defined in the first cell based on SHARED_MODEL_BASE.\n",
1015:     "%run {scripts_dir}/{lang}/downloading-{lang}.py\n",
1016:     "\n",
1017:     "# --- Ensure we are back in BASE_DIR at the end of the cell ---\n",
1018:     "if os.getcwd() != str(BASE_DIR):\n",
1019:     "    os.chdir(BASE_DIR)\n",
1020:     "# --- End of Directory Management ---"
1021:    ]
1022:   },
1023:   {
1024:    "cell_type": "markdown",
1025:    "id": "09187f0b-5108-4ec9-b251-d4bff537d110",
1026:    "metadata": {},
1027:    "source": [
1028:     "4. Start 🔽\n",
1029:     "\n",
1030:     "This cell launches the Stable Diffusion WebUI. It will execute the patched launch.py script from your fork, applying any platform-specific optimizations and arguments you've included."
1031:    ]
1032:   },
1033:   {
1034:    "cell_type": "code",
1035:    "execution_count": null,
1036:    "id": "35260036-3430-453d-8244-d81ccea04b32",
1037:    "metadata": {},
1038:    "outputs": [],
1039:    "source": [
1040:     "import os\n",
1041:     "from pathlib import Path\n",
1042:     "\n",
1043:     "# --- Start of Directory Management ---\n",
1044:     "BASE_DIR = Path(\"/teamspace/studios/this_studio\")\n",
1045:     "if os.getcwd() != str(BASE_DIR):\n",
1046:     "    print(f\"🔄 Changing directory from {os.getcwd()} to {BASE_DIR}\")\n",
1047:     "    os.chdir(BASE_DIR)\n",
1048:     "# --- End of Directory Management ---\n",
1049:     "\n",
1050:     "# Define scripts_dir using BASE_DIR for consistency\n",
1051:     "scripts_dir = BASE_DIR / 'ANXETY' / 'scripts'\n",
1052:     "\n",
1053:     "# Launch WebUI.\n",
1054:     "%run {scripts_dir}/launch.py -l\n",
1055:     "\n",
1056:     "# --- Ensure we are back in BASE_DIR at the end of the cell ---\n",
1057:     "if os.getcwd() != str(BASE_DIR):\n",
1058:     "    os.chdir(BASE_DIR)\n",
1059:     "# --- End of Directory Management ---\n"
1060:    ]
1061:   },
1062:   {
1063:    "cell_type": "markdown",
1064:    "id": "b83974dc-0f5f-4a5b-8d52-3361c74a9458",
1065:    "metadata": {},
1066:    "source": [
1067:     "Utilities\n",
1068:     "5. Run Cleanup Utility 🔽\n",
1069:     "\n",
1070:     "This cell runs the new Cleanup Utility GUI script, allowing you to manage your environment. This script is downloaded from your fork via the initial setup."
1071:    ]
1072:   },
1073:   {
1074:    "cell_type": "code",
1075:    "execution_count": null,
1076:    "id": "5896fe1b-7db1-40a6-a0a5-1779a53248c4",
1077:    "metadata": {},
1078:    "outputs": [],
1079:    "source": [
1080:     "import os\n",
1081:     "from pathlib import Path\n",
1082:     "\n",
1083:     "# --- Start of Directory Management ---\n",
1084:     "BASE_DIR = Path(\"/teamspace/studios/this_studio\")\n",
1085:     "if os.getcwd() != str(BASE_DIR):\n",
1086:     "    print(f\"🔄 Changing directory from {os.getcwd()} to {BASE_DIR}\")\n",
1087:     "    os.chdir(BASE_DIR)\n",
1088:     "# --- End of Directory Management ---\n",
1089:     "\n",
1090:     "# Define scripts_dir using BASE_DIR for consistency\n",
1091:     "scripts_dir = BASE_DIR / 'ANXETY' / 'scripts'\n",
1092:     "\n",
1093:     "# Run the Cleanup Utility GUI\n",
1094:     "%run {scripts_dir}/auto-cleaner.py\n",
1095:     "\n",
1096:     "# --- Ensure we are back in BASE_DIR at the end of the cell ---\n",
1097:     "if os.getcwd() != str(BASE_DIR):\n",
1098:     "    os.chdir(BASE_DIR)\n",
1099:     "# --- End of Directory Management ---\n"
1100:    ]
1101:   },
1102:   {
1103:    "cell_type": "code",
1104:    "execution_count": null,
1105:    "id": "f8a56c35-0d86-4826-a5c7-ba901a5708e9",
1106:    "metadata": {},
1107:    "outputs": [],
1108:    "source": [
1109:     "from pathlib import Path\n",
1110:     "import shutil\n",
1111:     "import os\n",
1112:     "import sys\n",
1113:     "\n",
1114:     "# --- Start of Directory Management ---\n",
1115:     "BASE_DIR = Path(\"/teamspace/studios/this_studio\")\n",
1116:     "if os.getcwd() != str(BASE_DIR):\n",
1117:     "    print(f\"🔄 Changing directory from {os.getcwd()} to {BASE_DIR}\")\n",
1118:     "    os.chdir(BASE_DIR)\n",
1119:     "# --- End of Directory Management ---\n",
1120:     "\n",
1121:     "# --- VERY IMPORTANT WARNING ---\n",
1122:     "# This cell will DELETE almost everything in your Lightning AI instance.\n",
1123:     "# It will only preserve this notebook file and 'main.py'.\n",
1124:     "# Ensure you understand what is being deleted before running.\n",
1125:     "# This operation is IRREVERSIBLE.\n",
1126:     "\n",
1127:     "print(\"!!! DANGER: YOU ARE ABOUT TO DELETE ALMOST ALL FILES !!!\")\n",
1128:     "print(\"!!! PLEASE READ CAREFULLY BEFORE PROCEEDING !!!\")\n",
1129:     "print(\"\\nThis cell will delete all folders and files in your current studio instance, EXCEPT:\")\n",
1130:     "print(\" - This notebook file (e.g., 'LightningAnxiety (1) (1) (2).ipynb')\")\n",
1131:     "print(\" - The 'main.py' file (if it exists in the root)\")\n",
1132:     "print(\"\\nTHIS WILL REQUIRE YOU TO RERUN THE ENTIRE NOTEBOOK FROM THE FIRST CELL FOR A FRESH START.\")\n",
1133:     "print(\"If you have any custom files you wish to keep, MOVE THEM OUTSIDE THIS STUDIO INSTANCE NOW.\")\n",
1134:     "print(\"Proceed only if you want a completely blank studio environment.\")\n",
1135:     "print(\"\\nType 'YES_DELETE_ALL' (case-sensitive) to confirm deletion and execute, then press Enter.\")\n",
1136:     "print(\"Anything else will abort the operation.\")\n",
1137:     "\n",
1138:     "confirmation = input(\"Confirmation: \")\n",
1139:     "\n",
1140:     "if confirmation.strip() == \"YES_DELETE_ALL\": # Case-sensitive comparison\n",
1141:     "    # Get the home/studio path\n",
1142:     "    # On Lightning AI, this is typically /teamspace/studios/this_studio\n",
1143:     "    HOME_PATH = Path.home()\n",
1144:     "\n",
1145:     "    # Get the current notebook's filename\n",
1146:     "    # Use a more robust way to find the notebook file name, as __file__ is not always reliable in notebooks\n",
1147:     "    notebook_filename = \"LightningAnxiety (1) (1) (2).ipynb\" # Explicitly set your notebook filename here for reliability\n",
1148:     "    notebook_path = HOME_PATH / notebook_filename\n",
1149:     "\n",
1150:     "    main_py_path = HOME_PATH / \"main.py\"\n",
1151:     "\n",
1152:     "    # Define items to EXCLUDE from deletion\n",
1153:     "    EXCLUDE_LIST = [\n",
1154:     "        notebook_path,\n",
1155:     "        main_py_path\n",
1156:     "    ]\n",
1157:     "\n",
1158:     "    print(f\"\\n--- Starting Comprehensive Deletion in {HOME_PATH} ---\")\n",
1159:     "    deleted_count = 0\n",
1160:     "    skipped_count = 0\n",
1161:     "\n",
1162:     "    for item in HOME_PATH.iterdir():\n",
1163:     "        # Convert item to absolute path for consistent comparison with EXCLUDE_LIST\n",
1164:     "        abs_item = item.resolve()\n",
1165:     "        if abs_item in EXCLUDE_LIST:\n",
1166:     "            print(f\"ℹ️ Skipping protected item: {item.name}\")\n",
1167:     "            skipped_count += 1\n",
1168:     "            continue\n",
1169:     "\n",
1170:     "        print(f\"🗑️ Attempting to delete: {item.name} ({item})...\")\n",
1171:     "        try:\n",
1172:     "            if item.is_dir():\n",
1173:     "                shutil.rmtree(item)\n",
1174:     "            else:\n",
1175:     "                item.unlink() # Delete file\n",
1176:     "            print(f\"✅ Successfully deleted: {item.name}\")\n",
1177:     "            deleted_count += 1\n",
1178:     "        except Exception as e:\n",
1179:     "            print(f\"❌ Error deleting {item.name} ({item}): {e}\")\n",
1180:     "\n",
1181:     "    print(\"\\n--- Comprehensive Cleanup Process Complete ---\")\n",
1182:     "    print(f\"Summary: {deleted_count} items deleted, {skipped_count} items skipped (protected).\")\n",
1183:     "    print(\"Please restart your runtime and run the notebook from the first cell for a fresh start.\")\n",
1184:     "else:\n",
1185:     "    print(\"\\nOperation aborted. No folders were deleted.\\n\")\n",
1186:     "\n",
1187:     "# --- Ensure we are back in BASE_DIR at the end of the cell ---\n",
1188:     "if os.getcwd() != str(BASE_DIR):\n",
1189:     "    os.chdir(BASE_DIR)\n",
1190:     "# --- End of Directory Management ---\n"
1191:    ]
1192:   },
1193:   {
1194:    "cell_type": "code",
1195:    "execution_count": null,
1196:    "id": "60190e9e-4d90-47ff-804f-6efeb6c1ad6a",
1197:    "metadata": {},
1198:    "outputs": [],
1199:    "source": []
1200:   }
1201:  ],
1202:  "metadata": {
1203:   "kernelspec": {
1204:    "display_name": "Python 3",
1205:    "language": "python",
1206:    "name": "python3"
1207:   },
1208:   "language_info": {
1209:    "codemirror_mode": {
1210:     "name": "ipython",
1211:     "version": 3
1212:    },
1213:    "file_extension": ".py",
1214:    "mimetype": "text/x-python",
1215:    "name": "python",
1216:    "nbconvert_exporter": "python",
1217:    "pygments_lexer": "ipython3",
1218:    "version": "3.10.10"
1219:   }
1220:  },
1221:  "nbformat": 4,
1222:  "nbformat_minor": 5
1223: }
```

## File: scripts/en/downloading-en.py
```python
  1: # ~ download.py | by ANXETY ~ (All-in-One Fix)
  2: 
  3: from webui_utils import handle_setup_timer
  4: from CivitaiAPI import CivitAiAPI
  5: from Manager import m_download
  6: import json_utils as js
  7: 
  8: from IPython.display import clear_output
  9: from pathlib import Path
 10: import subprocess
 11: import shlex
 12: import time
 13: import json
 14: import sys
 15: import re
 16: import os
 17: 
 18: # --- Setup & Constants ---
 19: DOWNLOADER_VERSION = "2025.06.09.8_final_patch"
 20: CD = os.chdir
 21: HOME = Path(js.read(os.path.join(Path.home(), 'ANXETY', 'settings.json'), 'ENVIRONMENT.home_path', str(Path.home())))
 22: SCR_PATH = HOME / 'ANXETY'
 23: SCRIPTS = SCR_PATH / 'scripts'
 24: SETTINGS_PATH = SCR_PATH / 'settings.json'
 25: 
 26: class COLORS: R,G,Y,B,lB,X = "\033[31m","\033[32m","\033[33m","\033[34m","\033[36;1m","\033[0m"
 27: COL = COLORS
 28: 
 29: print(f"✨ Downloader Version: {DOWNLOADER_VERSION}")
 30: 
 31: # --- Load Settings ---
 32: settings = js.read(SETTINGS_PATH)
 33: env_settings = settings.get('ENVIRONMENT', {})
 34: widget_settings = settings.get('WIDGETS', {})
 35: webui_settings = settings.get('WEBUI', {})
 36: 
 37: # Explicitly load widget values
 38: XL_models = widget_settings.get('XL_models', False)
 39: inpainting_model = widget_settings.get('inpainting_model', False)
 40: model_selections = widget_settings.get('model', ('none',))
 41: vae_selections = widget_settings.get('vae', ('none',))
 42: lora_selections = widget_settings.get('lora', ('none',))
 43: controlnet_selections = widget_settings.get('controlnet', ('none',))
 44: latest_webui = widget_settings.get('latest_webui', True)
 45: latest_extensions = widget_settings.get('latest_extensions', True)
 46: 
 47: # Path Definitions
 48: model_dir = Path(webui_settings.get('model_dir'))
 49: vae_dir = Path(webui_settings.get('vae_dir'))
 50: lora_dir = Path(webui_settings.get('lora_dir'))
 51: control_dir = Path(webui_settings.get('control_dir'))
 52: extension_dir = Path(webui_settings.get('extension_dir'))
 53: WEBUI_PATH = Path(webui_settings.get('webui_path'))
 54: 
 55: # --- Data Loading ---
 56: model_files_path = SCRIPTS / ('_xl-models-data.py' if XL_models else '_models-data.py')
 57: with open(model_files_path, 'r', encoding='utf-8') as f: exec(f.read(), globals())
 58: 
 59: loras_data_path = SCRIPTS / '_loras-data.py'
 60: with open(loras_data_path, 'r', encoding='utf-8') as f: exec(f.read(), globals())
 61: 
 62: model_list = sdxl_models_data if XL_models else sd15_model_data
 63: vae_list = sdxl_vae_data if XL_models else sd15_vae_data
 64: lora_list_to_use = lora_data.get('sdxl_loras', {}) if XL_models else lora_data.get('sd15_loras', {})
 65: 
 66: # --- Download Logic ---
 67: def handle_submodels(selections, model_dict, dst_dir, inpainting=False):
 68:     download_list = []
 69:     if not isinstance(selections, (list, tuple)): return download_list
 70:     
 71:     cleaned_selections = [re.sub(r'^\d+\.\s*', '', sel) for sel in selections]
 72:     
 73:     for selection_name in cleaned_selections:
 74:         if selection_name in ['none']: continue
 75:         if selection_name == 'ALL':
 76:             for model_group_item in model_dict.values(): # Changed loop variable name to avoid confusion
 77:                 # Normalize model_group_item to a list for iteration
 78:                 items_to_process = model_group_item if isinstance(model_group_item, list) else [model_group_item]
 79:                 
 80:                 for item in items_to_process:
 81:                     download_list.append(f"{item['url']} {dst_dir} {item.get('name')}")
 82:             continue
 83:         
 84:         if selection_name in model_dict:
 85:             model_group = model_dict[selection_name]
 86:             
 87:             # Normalize model_group to a list for iteration
 88:             items_to_process = model_group if isinstance(model_group, list) else [model_group]
 89:             
 90:             for model_info in items_to_process:
 91:                 name = model_info.get('name') or os.path.basename(model_info['url'])
 92:                 if not inpainting and "inpainting" in name.lower():
 93:                     continue
 94:                 download_list.append(f"{model_info['url']} {dst_dir} {name}")
 95:     return download_list
 96: 
 97: # --- Main Execution ---
 98: if latest_webui or latest_extensions:
 99:     action = 'WebUI and Extensions' if latest_webui and latest_extensions else ('WebUI' if latest_webui else 'Extensions')
100:     print(f"⌚️ Updating {action}...")
101:     subprocess.run(['git', 'config', '--global', 'user.email', 'you@example.com'], capture_output=True)
102:     subprocess.run(['git', 'config', '--global', 'user.name', 'Your Name'], capture_output=True)
103:     if latest_webui:
104:         subprocess.run(['git', '-C', str(WEBUI_PATH), 'pull'], capture_output=True)
105:     if latest_extensions:
106:         os.makedirs(extension_dir, exist_ok=True) # Ensure the directory exists before listing
107:         for entry in os.listdir(str(extension_dir)):
108:             dir_path = os.path.join(str(extension_dir), entry)
109:             if os.path.isdir(dir_path) and os.path.exists(os.path.join(dir_path, '.git')):
110:                 subprocess.run(['git', '-C', str(dir_path), 'pull'], capture_output=True)
111:     print(f"✨ Update {action} Completed!")
112: 
113: print('📦 Processing download selections...')
114: # DEBUG statements moved to notebook cell based on previous interaction for direct visibility.
115: # These lines were intended to be in the notebook cell for direct output:
116: # print(f"DEBUG: Selected Models: {model_selections}")
117: # print(f"DEBUG: Selected VAEs: {vae_selections}")
118: 
119: line_entries = []
120: line_entries.extend(handle_submodels(model_selections, model_list, model_dir, inpainting_model))
121: line_entries.extend(handle_submodels(vae_selections, vae_list, vae_dir))
122: line_entries.extend(handle_submodels(lora_selections, lora_list_to_use, lora_dir))
123: line_entries.extend(handle_submodels(controlnet_selections, controlnet_list, control_dir))
124: 
125: download_line = ', '.join(line_entries)
126: 
127: if download_line:
128:     print("Starting downloads...")
129:     m_download(download_line, log=True)
130: else:
131:     print("No models selected for download.")
132: 
133: print('\r🏁 Download processing complete!')
```

## File: scripts/en/widgets-en.py
```python
  1: # ~ widgets.py | by ANXETY ~ (All-in-One Fix)
  2: 
  3: from widget_factory import WidgetFactory
  4: from webui_utils import update_current_webui
  5: import json_utils as js
  6: import ipywidgets as widgets
  7: from pathlib import Path
  8: import os
  9: import re
 10: 
 11: # --- Constants and Platform Setup ---
 12: try:
 13:     HOME = Path(js.read(os.path.join(Path.home(), 'ANXETY', 'settings.json'), 'ENVIRONMENT.home_path', str(Path.home())))
 14: except Exception:
 15:     HOME = Path.home()
 16: 
 17: SCR_PATH = HOME / 'ANXETY'
 18: SETTINGS_PATH = SCR_PATH / 'settings.json'
 19: SCRIPTS = SCR_PATH / 'scripts'
 20: CSS = SCR_PATH / 'CSS'
 21: JS = SCR_PATH / 'JS'
 22: widgets_css = CSS / 'main-widgets.css'
 23: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name', 'local')
 24: 
 25: # --- Helper Functions ---
 26: factory = WidgetFactory()
 27: 
 28: def read_model_data(file_path, data_key_in_file, prefixes=['none']):
 29:     """Reads data from a file, extracts a dictionary, and returns a numbered list of its keys."""
 30:     local_vars = {}
 31:     if not file_path.exists():
 32:         print(f"Warning: Data file not found at {file_path}. Skipping.")
 33:         return prefixes
 34:     with open(file_path, 'r', encoding='utf-8') as f:
 35:         try:
 36:             exec(f.read(), {}, local_vars)
 37:         except Exception as e:
 38:             print(f"Error executing data file {file_path}: {e}")
 39:             return prefixes
 40:     data_dict = local_vars
 41:     for key_part in data_key_in_file.split('.'):
 42:         data_dict = data_dict.get(key_part, {})
 43:         if not isinstance(data_dict, dict):
 44:             return prefixes
 45:     names = list(data_dict.keys())
 46:     numbered_names = [f"{i+1}. {name}" for i, name in enumerate(names)]
 47:     return prefixes + numbered_names
 48: 
 49: # --- Widget Definitions ---
 50: factory.load_css(widgets_css)
 51: 
 52: # Data file paths
 53: sd15_models_path = SCRIPTS / '_models-data.py'
 54: sdxl_models_path = SCRIPTS / '_xl-models-data.py'
 55: loras_data_path = SCRIPTS / '_loras-data.py'
 56: 
 57: # WebUI selection
 58: webui_selection = {
 59:     'A1111': "--xformers --no-half-vae", 'ComfyUI': "--use-sage-attention --dont-print-server",
 60:     'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory",
 61:     'Classic': "--persistent-patches --cuda-stream --pin-shared-memory",
 62:     'ReForge': "--xformers --cuda-stream --pin-shared-memory", 'SD-UX': "--xformers --no-half-vae"
 63: }
 64: 
 65: # --- Create Widgets ---
 66: model_header = factory.create_header('Model Selection (Ctrl+Click for multiple)')
 67: model_options = read_model_data(sd15_models_path, 'sd15_model_data')
 68: model_widget = factory.create_select_multiple(model_options, 'Models:', ('none',))
 69: inpainting_model_widget = factory.create_checkbox('Inpainting Models', False, ['inpaint'], layout={'width': 'auto'})
 70: XL_models_widget = factory.create_checkbox('SDXL', False, ['sdxl'], layout={'width': 'auto'})
 71: switch_model_widget = factory.create_hbox([inpainting_model_widget, XL_models_widget])
 72: 
 73: vae_header = factory.create_header('VAE Selection')
 74: vae_options = read_model_data(sd15_models_path, 'sd15_vae_data', ['none', 'ALL'])
 75: vae_widget = factory.create_select_multiple(vae_options, 'VAEs:', ('none',))
 76: 
 77: lora_header = factory.create_header('LoRA Selection')
 78: lora_options = read_model_data(loras_data_path, 'lora_data.sd15_loras', ['none', 'ALL'])
 79: lora_widget = factory.create_select_multiple(lora_options, 'LoRAs:', ('none',))
 80: 
 81: controlnet_header = factory.create_header('ControlNet Selection')
 82: controlnet_options = read_model_data(sd15_models_path, 'controlnet_list', ['none', 'ALL'])
 83: controlnet_widget = factory.create_select_multiple(controlnet_options, 'ControlNets:', ('none',))
 84: 
 85: additional_header = factory.create_header('Additional Settings')
 86: latest_webui_widget, latest_extensions_widget = factory.create_checkbox('Update WebUI', True), factory.create_checkbox('Update Extensions', True)
 87: change_webui_widget = factory.create_dropdown(list(webui_selection.keys()), 'WebUI:', 'Forge', layout={'width': 'auto'})
 88: commandline_arguments_widget = factory.create_text('Arguments:', webui_selection.get('Forge', ''))
 89: 
 90: save_button = factory.create_button('Save & Close', ['button', 'button_save'])
 91: GDrive_button = factory.create_button('', layout={'width': '48px', 'height': '48px'}, class_names=['gdrive-btn'])
 92: if ENV_NAME != 'Google Colab': GDrive_button.layout.display = 'none'
 93: 
 94: # --- Layout Assembly ---
 95: model_col = factory.create_vbox([model_header, model_widget, switch_model_widget])
 96: vae_col = factory.create_vbox([vae_header, vae_widget])
 97: lora_col = factory.create_vbox([lora_header, lora_widget])
 98: cnet_col = factory.create_vbox([controlnet_header, controlnet_widget])
 99: download_box = factory.create_vbox([model_col, vae_col, lora_col, cnet_col], class_names=['container'])
100: additional_box = factory.create_vbox([additional_header, factory.create_hbox([latest_webui_widget, latest_extensions_widget, change_webui_widget]), commandline_arguments_widget], class_names=['container'])
101: WIDGET_LIST = factory.create_vbox([factory.create_hbox([download_box, GDrive_button]), additional_box, save_button], class_names=['mainContainer'])
102: factory.display(WIDGET_LIST)
103: 
104: # --- Callbacks ---
105: def on_xl_toggle(change, widget):
106:     is_xl = change.new
107:     model_path = sdxl_models_path if is_xl else sd15_models_path
108:     model_key = 'sdxl_models_data' if is_xl else 'sd15_model_data'
109:     vae_key = 'sdxl_vae_data' if is_xl else 'sd15_vae_data'
110:     lora_key = 'lora_data.sdxl_loras' if is_xl else 'lora_data.sd15_loras'
111:     cnet_key = 'controlnet_list'
112:     model_widget.options = read_model_data(model_path, model_key)
113:     vae_widget.options = read_model_data(model_path, vae_key, ['none', 'ALL'])
114:     lora_widget.options = read_model_data(loras_data_path, lora_key, ['none', 'ALL'])
115:     controlnet_widget.options = read_model_data(model_path, cnet_key, ['none', 'ALL'])
116:     model_widget.value, vae_widget.value, lora_widget.value, controlnet_widget.value = ('none',), ('none',), ('none',), ('none',)
117: 
118: def on_webui_change(change, widget):
119:     commandline_arguments_widget.value = webui_selection.get(change.new, '')
120: 
121: # --- Settings ---
122: SETTINGS_KEYS = [
123:     'XL_models', 'model', 'inpainting_model', 'vae', 'lora', 'controlnet',
124:     'latest_webui', 'latest_extensions', 'change_webui', 'commandline_arguments'
125: ]
126: def save_settings():
127:     widget_values = {}
128:     for key in SETTINGS_KEYS:
129:         widget_name = f"{key}_widget"
130:         if widget_name in globals():
131:             widget_values[key] = globals()[widget_name].value
132:     js.save(SETTINGS_PATH, 'WIDGETS', widget_values)
133:     js.save(SETTINGS_PATH, 'mountGDrive', getattr(GDrive_button, 'toggle', False))
134:     update_current_webui(change_webui_widget.value)
135: 
136: def load_settings():
137:     if js.key_exists(SETTINGS_PATH, 'WIDGETS'):
138:         widget_data = js.read(SETTINGS_PATH, 'WIDGETS')
139:         for key in SETTINGS_KEYS:
140:             if key in widget_data and f"{key}_widget" in globals():
141:                 globals()[f"{key}_widget"].value = widget_data.get(key)
142:     GDrive_button.toggle = js.read(SETTINGS_PATH, 'mountGDrive', False)
143:     GDrive_button.add_class('active') if GDrive_button.toggle else GDrive_button.remove_class('active')
144: 
145: def on_save_click(button):
146:     save_settings()
147:     factory.close(list(WIDGET_LIST.children), ['hide'], delay=0.8)
148: 
149: # --- Initialisation ---
150: factory.connect_widgets([(XL_models_widget, 'value')], on_xl_toggle)
151: factory.connect_widgets([(change_webui_widget, 'value')], on_webui_change)
152: save_button.on_click(on_save_click)
153: load_settings()
```

## File: scripts/ru/downloading-ru.py
```python
  1: # ~ download.py | by ANXETY ~
  2: 
  3: from webui_utils import handle_setup_timer    # WEBUI
  4: from CivitaiAPI import CivitAiAPI             # CivitAI API
  5: from Manager import m_download                # Every Download
  6: import json_utils as js                       # JSON
  7: 
  8: from IPython.display import clear_output
  9: from IPython.utils import capture
 10: from urllib.parse import urlparse
 11: from IPython import get_ipython
 12: from datetime import timedelta
 13: from pathlib import Path
 14: import subprocess
 15: import requests
 16: import zipfile
 17: import shutil
 18: import shlex
 19: import time
 20: import json
 21: import sys
 22: import re
 23: import os
 24: 
 25: 
 26: CD = os.chdir
 27: ipySys = get_ipython().system
 28: ipyRun = get_ipython().run_line_magic
 29: 
 30: # Constants
 31: HOME = Path.home()
 32: VENV = HOME / 'venv'
 33: SCR_PATH = Path(HOME / 'ANXETY')
 34: SCRIPTS = SCR_PATH / 'scripts'
 35: SETTINGS_PATH = SCR_PATH / 'settings.json'
 36: 
 37: LANG = js.read(SETTINGS_PATH, 'ENVIRONMENT.lang')
 38: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
 39: UI = js.read(SETTINGS_PATH, 'WEBUI.current')
 40: WEBUI = js.read(SETTINGS_PATH, 'WEBUI.webui_path')
 41: 
 42: 
 43: # Text Colors (\033)
 44: class COLORS:
 45:     R  =  "\033[31m"     # Red
 46:     G  =  "\033[32m"     # Green
 47:     Y  =  "\033[33m"     # Yellow
 48:     B  =  "\033[34m"     # Blue
 49:     lB =  "\033[36;1m"   # lightBlue
 50:     X  =  "\033[0m"      # Reset
 51: 
 52: COL = COLORS
 53: 
 54: 
 55: ## =================== LIBRARIES | VENV ==================
 56: 
 57: def install_dependencies(commands):
 58:     """Run a list of installation commands."""
 59:     for cmd in commands:
 60:         try:
 61:             subprocess.run(shlex.split(cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 62:         except Exception:
 63:             pass
 64: 
 65: def setup_venv(url):
 66:     """Customize the virtual environment using the specified URL."""
 67:     CD(HOME)
 68:     # url = "https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31017-venv-torch251-cu121-C-fca.tar.lz4"
 69:     fn = Path(url).name
 70: 
 71:     m_download(f"{url} {HOME} {fn}")
 72: 
 73:     # Install dependencies based on environment
 74:     install_commands = []
 75:     if ENV_NAME == 'Kaggle':
 76:         install_commands.extend([
 77:             'pip install ipywidgets jupyterlab_widgets --upgrade',
 78:             'rm -f /usr/lib/python3.10/sitecustomize.py'
 79:         ])
 80: 
 81:     install_commands.append('sudo apt-get -y install lz4 pv')
 82:     install_dependencies(install_commands)
 83: 
 84:     # Unpack and clean
 85:     ipySys(f"pv {fn} | lz4 -d | tar xf -")
 86:     Path(fn).unlink()
 87: 
 88:     BIN = str(VENV / 'bin')
 89:     PKG = str(VENV / 'lib/python3.10/site-packages')
 90: 
 91:     os.environ['PYTHONWARNINGS'] = 'ignore'
 92: 
 93:     sys.path.insert(0, PKG)
 94:     if BIN not in os.environ['PATH']:
 95:         os.environ['PATH'] = BIN + ':' + os.environ['PATH']
 96:     if PKG not in os.environ['PYTHONPATH']:
 97:         os.environ['PYTHONPATH'] = PKG + ':' + os.environ['PYTHONPATH']
 98: 
 99: def install_packages(install_lib):
100:     """Install packages from the provided library dictionary."""
101:     for index, (package, install_cmd) in enumerate(install_lib.items(), start=1):
102:         print(f"\r[{index}/{len(install_lib)}] {COL.G}>>{COL.X} Installing {COL.Y}{package}{COL.X}..." + ' ' * 35, end='')
103:         try:
104:             result = subprocess.run(install_cmd, shell=True, capture_output=True)
105:             if result.returncode != 0:
106:                 print(f"\n{COL.R}Error installing {package}{COL.X}")
107:         except Exception:
108:             pass
109: 
110: # Check and install dependencies
111: if not js.key_exists(SETTINGS_PATH, 'ENVIRONMENT.install_deps', True):
112:     install_lib = {
113:         ## Libs
114:         'aria2': "pip install aria2",
115:         'gdown': "pip install gdown",
116:         ## Tunnels
117:         'localtunnel': "npm install -g localtunnel",
118:         'cloudflared': "wget -qO /usr/bin/cl https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64; chmod +x /usr/bin/cl",
119:         'zrok': "wget -qO zrok_1.0.4_linux_amd64.tar.gz https://github.com/openziti/zrok/releases/download/v1.0.4/zrok_1.0.4_linux_amd64.tar.gz; tar -xzf zrok_1.0.4_linux_amd64.tar.gz -C /usr/bin; rm -f zrok_1.0.4_linux_amd64.tar.gz",
120:         'ngrok': "wget -qO ngrok-v3-stable-linux-amd64.tgz https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz; tar -xzf ngrok-v3-stable-linux-amd64.tgz -C /usr/bin; rm -f ngrok-v3-stable-linux-amd64.tgz"
121:     }
122: 
123:     print('💿 Установка библиотек займет немного времени.')
124:     install_packages(install_lib)
125:     clear_output()
126:     js.update(SETTINGS_PATH, 'ENVIRONMENT.install_deps', True)
127: 
128: # Install VENV
129: current_ui = js.read(SETTINGS_PATH, 'WEBUI.current')
130: latest_ui = js.read(SETTINGS_PATH, 'WEBUI.latest')
131: 
132: # Determine whether to reinstall venv
133: venv_needs_reinstall = (
134:     not VENV.exists()  # venv is missing
135:     # Check category change (Classic <-> other)
136:     or (latest_ui == 'Classic') != (current_ui == 'Classic')
137: )
138: 
139: if venv_needs_reinstall:
140:     if VENV.exists():
141:         print("🗑️ Удаление старого venv...")
142:         shutil.rmtree(VENV)
143:         clear_output()
144: 
145:     if current_ui == 'Classic':
146:         venv_url = "https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31112-venv-torch251-cu121-C-Classic.tar.lz4"
147:         py_version = '(3.11.12)'
148:     else:
149:         venv_url = "https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31017-venv-torch251-cu121-C-fca.tar.lz4"
150:         py_version = '(3.10.17)'
151: 
152:     print(f"♻️ Установка VENV {py_version}, это займет некоторое время...")
153:     setup_venv(venv_url)
154:     clear_output()
155: 
156:     # Update latest UI version...
157:     js.update(SETTINGS_PATH, 'WEBUI.latest', current_ui)
158: 
159: # if not os.path.exists(VENV):
160: #     print('♻️ Установка VENV, это займет некоторое время...')
161: #     setup_venv()
162: #     clear_output()
163: 
164: ## ================ loading settings V5 ==================
165: 
166: def load_settings(path):
167:     """Load settings from a JSON file."""
168:     try:
169:         return {
170:             **js.read(path, 'ENVIRONMENT'),
171:             **js.read(path, 'WIDGETS'),
172:             **js.read(path, 'WEBUI')
173:         }
174:     except (json.JSONDecodeError, IOError) as e:
175:         print(f"Error loading settings: {e}")
176:         return {}
177: 
178: # Load settings
179: settings = load_settings(SETTINGS_PATH)
180: locals().update(settings)
181: 
182: ## ======================== WEBUI ========================
183: 
184: if UI in ['A1111', 'SD-UX'] and not os.path.exists('/root/.cache/huggingface/hub/models--Bingsu--adetailer'):
185:     print('🚚 Распаковка кэша моделей ADetailer...')
186: 
187:     name_zip = 'hf_cache_adetailer'
188:     chache_url = 'https://huggingface.co/NagisaNao/ANXETY/resolve/main/hf_chache_adetailer.zip'
189: 
190:     zip_path = f"{HOME}/{name_zip}.zip"
191:     m_download(f"{chache_url} {HOME} {name_zip}")
192:     ipySys(f"unzip -q -o {zip_path} -d /")
193:     ipySys(f"rm -rf {zip_path}")
194: 
195:     clear_output()
196: 
197: start_timer = js.read(SETTINGS_PATH, 'ENVIRONMENT.start_timer')
198: 
199: if not os.path.exists(WEBUI):
200:     start_install = time.time()
201:     print(f"⌚ Распаковка Stable Diffusion... | WEBUI: {COL.B}{UI}{COL.X}", end='')
202: 
203:     ipyRun('run', f"{SCRIPTS}/UIs/{UI}.py")
204:     handle_setup_timer(WEBUI, start_timer)		# Setup timer (for timer-extensions)
205: 
206:     install_time = time.time() - start_install
207:     minutes, seconds = divmod(int(install_time), 60)
208:     print(f"\r🚀 Распаковка {COL.B}{UI}{COL.X} Завершена! {minutes:02}:{seconds:02} ⚡" + ' '*25)
209: 
210: else:
211:     print(f"🔧 Текущий WebUI: {COL.B}{UI}{COL.X}")
212:     print('🚀 Распаковка завершена. Пропуск. ⚡')
213: 
214:     timer_env = handle_setup_timer(WEBUI, start_timer)
215:     elapsed_time = str(timedelta(seconds=time.time() - timer_env)).split('.')[0]
216:     print(f"⌚️ Продолжительность сеанса: {COL.Y}{elapsed_time}{COL.X}")
217: 
218: 
219: ## Changes extensions and WebUi
220: if latest_webui or latest_extensions:
221:     action = 'WebUI и Расширений' if latest_webui and latest_extensions else ('WebUI' if latest_webui else 'Расширений')
222:     print(f"⌚️ Обновление {action}...", end='')
223:     with capture.capture_output():
224:         ipySys('git config --global user.email "you@example.com"')
225:         ipySys('git config --global user.name "Your Name"')
226: 
227:         ## Update Webui
228:         if latest_webui:
229:             CD(WEBUI)
230:             # ipySys('git restore .')
231:             # ipySys('git pull -X theirs --rebase --autostash')
232: 
233:             ipySys('git stash push --include-untracked')
234:             ipySys('git pull --rebase')
235:             ipySys('git stash pop')
236: 
237:         ## Update extensions
238:         if latest_extensions:
239:             # ipySys('{\'for dir in \' + WEBUI + \'/extensions/*/; do cd \\'$dir\\' && git reset --hard && git pull; done\'}')
240:             for entry in os.listdir(f"{WEBUI}/extensions"):
241:                 dir_path = f"{WEBUI}/extensions/{entry}"
242:                 if os.path.isdir(dir_path):
243:                     subprocess.run(['git', 'reset', '--hard'], cwd=dir_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
244:                     subprocess.run(['git', 'pull'], cwd=dir_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
245: 
246:     print(f"\r✨ Обновление {action} Завершено!")
247: 
248: 
249: # === FIXING EXTENSIONS ===
250: with capture.capture_output():
251:     # --- Umi-Wildcard ---
252:     ipySys("sed -i '521s/open=\\(False\\|True\\)/open=False/' {WEBUI}/extensions/Umi-AI-Wildcards/scripts/wildcard_recursive.py")    # Closed accordion by default
253: 
254: 
255: ## Version switching
256: if commit_hash:
257:     print('🔄 Переключаемся на указанную версию...', end='')
258:     with capture.capture_output():
259:         CD(WEBUI)
260:         ipySys('git config --global user.email "you@example.com"')
261:         ipySys('git config --global user.name "Your Name"')
262:         ipySys('git reset --hard {commit_hash}')
263:         ipySys('git pull origin {commit_hash}')    # Get last changes in branch
264:     print(f"\r🔄 Переключение завершено! Текущий коммит: {COL.B}{commit_hash}{COL.X}")
265: 
266: 
267: # === Google Drive Mounting | EXCLUSIVE for Colab ===
268: from google.colab import drive
269: mountGDrive = js.read(SETTINGS_PATH, 'mountGDrive')  # Mount/unmount flag
270: 
271: # Configuration
272: GD_BASE = "/content/drive/MyDrive/sdAIgen"
273: SYMLINK_CONFIG = [
274:     {   # model
275:         'local_dir': model_dir,
276:         'gdrive_subpath': 'Checkpoints',
277:     },
278:     {   # vae
279:         'local_dir': vae_dir,
280:         'gdrive_subpath': 'VAE',
281:     },
282:     {   # lora
283:         'local_dir': lora_dir,
284:         'gdrive_subpath': 'Lora',
285:     }
286: ]
287: 
288: def create_symlink(src_path, gdrive_path, log=False):
289:     """Create symbolic link with content migration and cleanup"""
290:     try:
291:         src_exists = os.path.exists(src_path)
292:         is_real_dir = src_exists and os.path.isdir(src_path) and not os.path.islink(src_path)
293: 
294:         # Handle real directory migration
295:         if is_real_dir and os.path.exists(gdrive_path):
296:             for item in os.listdir(src_path):
297:                 src_item = os.path.join(src_path, item)
298:                 dst_item = os.path.join(gdrive_path, item)
299: 
300:                 if os.path.exists(dst_item):
301:                     shutil.rmtree(dst_item) if os.path.isdir(dst_item) else os.remove(dst_item)
302:                 shutil.move(src_item, dst_item)
303: 
304:             shutil.rmtree(src_path)
305:             if log:
306:                 print(f"Moved contents from {src_path} to {gdrive_path}")
307: 
308:         # Cleanup existing path
309:         if os.path.exists(src_path) and not is_real_dir:
310:             if os.path.islink(src_path):
311:                 os.unlink(src_path)
312:             else:
313:                 os.remove(src_path)
314: 
315:         # Create new symlink
316:         if not os.path.exists(src_path):
317:             os.symlink(gdrive_path, src_path)
318:             if log:
319:                 print(f"Created symlink: {src_path} → {gdrive_path}")
320: 
321:     except Exception as e:
322:         print(f"Error processing {src_path}: {str(e)}")
323: 
324: def handle_gdrive(mount_flag, log=False):
325:     """Main handler for Google Drive mounting and symlink management"""
326:     if mount_flag:
327:         if os.path.exists("/content/drive/MyDrive"):
328:             print("🎉 Google Drive подключен~")
329:         else:
330:             try:
331:                 print("⏳ Подключаемся к Google Drive...", end='')
332:                 with capture.capture_output():
333:                     drive.mount('/content/drive')
334:                 print("\r🚀 Google Drive успешно подключен!")
335:             except Exception as e:
336:                 clear_output()
337:                 print(f"❌ Mounting failed: {str(e)}\n")
338:                 return
339: 
340:         try:
341:             # Create base directory structure
342:             os.makedirs(GD_BASE, exist_ok=True)
343:             for cfg in SYMLINK_CONFIG:
344:                 path = os.path.join(GD_BASE, cfg['gdrive_subpath'])
345:                 os.makedirs(path, exist_ok=True)
346:             print(f"📁 → {GD_BASE}")
347: 
348:             # Create symlinks
349:             for cfg in SYMLINK_CONFIG:
350:                 src = os.path.join(cfg['local_dir'], 'GDrive')
351:                 dst = os.path.join(GD_BASE, cfg['gdrive_subpath'])
352:                 create_symlink(src, dst, log)
353: 
354:             print("✅ Симлинки успешно созданы!")
355: 
356:         except Exception as e:
357:             print(f"❌ Setup error: {str(e)}\n")
358: 
359:         # Trashing
360:         cmd = f"find {GD_BASE} -type d -name .ipynb_checkpoints -exec rm -rf {{}} +"
361:         subprocess.run(shlex.split(cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
362: 
363:     else:
364:         if os.path.exists("/content/drive/MyDrive"):
365:             try:
366:                 print("⏳ Отключаемся от Google Drive...", end='')
367:                 with capture.capture_output():
368:                     drive.flush_and_unmount()
369:                     os.system("rm -rf /content/drive")
370:                 print("\r✅ Диск успешно отключен и удалён!")
371: 
372:                 # Remove symlinks
373:                 for cfg in SYMLINK_CONFIG:
374:                     link_path = os.path.join(cfg['local_dir'], 'GDrive')
375:                     if os.path.islink(link_path):
376:                         os.unlink(link_path)
377: 
378:                 print("🗑️ Симлинки успешно удалены!")
379: 
380:             except Exception as e:
381:                 print(f"❌ Unmount error: {str(e)}\n")
382: 
383: handle_gdrive(mountGDrive)
384: 
385: 
386: # Get XL or 1.5 models list
387: ## model_list | vae_list | controlnet_list
388: model_files = '_xl-models-data.py' if XL_models else '_models-data.py'
389: with open(f"{SCRIPTS}/{model_files}") as f:
390:     exec(f.read())
391: 
392: ## Downloading model and stuff | oh~ Hey! If you're freaked out by that code too, don't worry, me too!
393: print('📦 Скачивание моделей и прочего...', end='')
394: 
395: extension_repo = []
396: PREFIX_MAP = {
397:     # prefix : (dir_path , short-tag)
398:     'model': (model_dir, '$ckpt'),
399:     'vae': (vae_dir, '$vae'),
400:     'lora': (lora_dir, '$lora'),
401:     'embed': (embed_dir, '$emb'),
402:     'extension': (extension_dir, '$ext'),
403:     'adetailer': (adetailer_dir, '$ad'),
404:     'control': (control_dir, '$cnet'),
405:     'upscale': (upscale_dir, '$ups'),
406:     # Other
407:     'clip': (clip_dir, '$clip'),
408:     'unet': (unet_dir, '$unet'),
409:     'vision': (vision_dir, '$vis'),
410:     'encoder': (encoder_dir, '$enc'),
411:     'diffusion': (diffusion_dir, '$diff'),
412:     'config': (config_dir, '$cfg')
413: }
414: for dir_path, _ in PREFIX_MAP.values():
415:     os.makedirs(dir_path, exist_ok=True)
416: 
417: ''' Formatted Info Output '''
418: 
419: def _center_text(text, terminal_width=45):
420:     padding = (terminal_width - len(text)) // 2
421:     return f"{' ' * padding}{text}{' ' * padding}"
422: 
423: def format_output(url, dst_dir, file_name, image_url=None, image_name=None):
424:     """Formats and prints download details with colored text."""
425:     info = '[NONE]'
426:     if file_name:
427:         info = _center_text(f"[{file_name.rsplit('.', 1)[0]}]")
428:     if not file_name and 'drive.google.com' in url:
429:       info = _center_text('[GDrive]')
430: 
431:     sep_line = '───' * 20
432: 
433:     print()
434:     print(f"{COL.G}{sep_line}{COL.lB}{info}{COL.G}{sep_line}{COL.X}")
435:     print(f"{COL.Y}{'URL:':<12}{COL.X}{url}")
436:     print(f"{COL.Y}{'SAVE DIR:':<12}{COL.B}{dst_dir}")
437:     print(f"{COL.Y}{'FILE NAME:':<12}{COL.B}{file_name}{COL.X}")
438:     if 'civitai' in url and image_url:
439:         print(f"{COL.G}{'[Preview]:':<12}{COL.X}{image_name} → {image_url}")
440:     print()
441: 
442: ''' Main Download Code '''
443: 
444: def _clean_url(url):
445:     url_cleaners = {
446:         'huggingface.co': lambda u: u.replace('/blob/', '/resolve/').split('?')[0],
447:         'github.com': lambda u: u.replace('/blob/', '/raw/')
448:     }
449:     for domain, cleaner in url_cleaners.items():
450:         if domain in url:
451:             return cleaner(url)
452:     return url
453: 
454: def _extract_filename(url):
455:     if match := re.search(r'\[(.*?)\]', url):
456:         return match.group(1)
457:     if any(d in urlparse(url).netloc for d in ["civitai.com", "drive.google.com"]):
458:         return None
459:     return Path(urlparse(url).path).name
460: 
461: def _unpack_zips():
462:     """Recursively extract and delete all .zip files in PREFIX_MAP directories."""
463:     for dir_path, _ in PREFIX_MAP.values():
464:         for zip_file in Path(dir_path).rglob('*.zip'):
465:             with zipfile.ZipFile(zip_file, 'r') as zf:
466:                 zf.extractall(zip_file.with_suffix(''))
467:             zip_file.unlink()
468: 
469: # Download Core
470: 
471: def _process_download_link(link):
472:     """Processes a download link, splitting prefix, URL, and filename."""
473:     link = _clean_url(link)
474:     if ':' in link:
475:         prefix, path = link.split(':', 1)
476:         if prefix in PREFIX_MAP:
477:             return prefix, re.sub(r'\[.*?\]', '', path), _extract_filename(path)
478:     return None, link, None
479: 
480: def download(line):
481:     """Downloads files from comma-separated links, processes prefixes, and unpacks zips post-download."""
482:     for link in filter(None, map(str.strip, line.split(','))):
483:         prefix, url, filename = _process_download_link(link)
484: 
485:         if prefix:
486:             dir_path, _ = PREFIX_MAP[prefix]
487:             if prefix == 'extension':
488:                 extension_repo.append((url, filename))
489:                 continue
490:             try:
491:                 manual_download(url, dir_path, filename, prefix)
492:             except Exception as e:
493:                 print(f"\n> Download error: {e}")
494:         else:
495:             url, dst_dir, file_name = url.split()
496:             manual_download(url, dst_dir, file_name)
497: 
498:     _unpack_zips()
499: 
500: def manual_download(url, dst_dir, file_name=None, prefix=None):
501:     clean_url = url
502:     image_url, image_name = None, None
503: 
504:     if 'civitai' in url:
505:         api = CivitAiAPI(civitai_token)
506:         if not (data := api.validate_download(url, file_name)):
507:             return
508: 
509:         model_type, file_name = data.model_type, data.model_name    # Type, name
510:         clean_url, url = data.clean_url, data.download_url          # Clean_URL, URL
511:         image_url, image_name = data.image_url, data.image_name     # Img_URL, Img_Name
512: 
513:         # Download preview images
514:         if image_url and image_name:
515:             m_download(f"{image_url} {dst_dir} {image_name}")
516: 
517:     elif any(s in url for s in ('github', 'huggingface.co')):
518:         if file_name and '.' not in file_name:
519:             file_name += f".{clean_url.split('.')[-1]}"
520: 
521:     # Formatted info output
522:     format_output(clean_url, dst_dir, file_name, image_url, image_name)
523: 
524:     # Downloading
525:     m_download(f"{url} {dst_dir} {file_name or ''}", log=True)
526: 
527: ''' SubModels - Added URLs '''
528: 
529: # Separation of merged numbers
530: def _parse_selection_numbers(num_str, max_num):
531:     """Split a string of numbers into unique integers, considering max_num as the upper limit."""
532:     num_str = num_str.replace(',', ' ').strip()
533:     unique_numbers = set()
534:     max_length = len(str(max_num))
535: 
536:     for part in num_str.split():
537:         if not part.isdigit():
538:             continue
539: 
540:         # Check if the entire part is a valid number
541:         part_int = int(part)
542:         if part_int <= max_num:
543:             unique_numbers.add(part_int)
544:             continue  # No need to split further
545: 
546:         # Split the part into valid numbers starting from the longest possible
547:         current_position = 0
548:         part_len = len(part)
549:         while current_position < part_len:
550:             found = False
551:             # Try lengths from max_length down to 1
552:             for length in range(min(max_length, part_len - current_position), 0, -1):
553:                 substring = part[current_position:current_position + length]
554:                 if substring.isdigit():
555:                     num = int(substring)
556:                     if num <= max_num and num != 0:
557:                         unique_numbers.add(num)
558:                         current_position += length
559:                         found = True
560:                         break
561:             if not found:
562:                 # Move to the next character if no valid number found
563:                 current_position += 1
564: 
565:     return sorted(unique_numbers)
566: 
567: def handle_submodels(selection, num_selection, model_dict, dst_dir, base_url, inpainting_model=False):
568:     selected = []
569:     if selection == "ALL":
570:         selected = sum(model_dict.values(), [])
571:     elif selection in model_dict:
572:         selected.extend(model_dict[selection])
573: 
574:     if num_selection:
575:         max_num = len(model_dict)
576:         for num in _parse_selection_numbers(num_selection, max_num):
577:             if 1 <= num <= max_num:
578:                 name = list(model_dict.keys())[num - 1]
579:                 selected.extend(model_dict[name])
580: 
581:     unique_models = {}
582:     for model in selected:
583:         name = model.get('name') or os.path.basename(model['url'])
584:         if not inpainting_model and "inpainting" in name:
585:             continue
586:         unique_models[name] = {
587:             'url': model['url'],
588:             'dst_dir': model.get('dst_dir', dst_dir),
589:             'name': name
590:         }
591: 
592:     return base_url + ', '.join(
593:         f"{m['url']} {m['dst_dir']} {m['name']}"
594:         for m in unique_models.values()
595:     )
596: 
597: line = ""
598: line = handle_submodels(model, model_num, model_list, model_dir, line)
599: line = handle_submodels(vae, vae_num, vae_list, vae_dir, line)
600: line = handle_submodels(controlnet, controlnet_num, controlnet_list, control_dir, line)
601: 
602: ''' File.txt - added urls '''
603: 
604: def _process_lines(lines):
605:     """Processes text lines, extracts valid URLs with tags/filenames, and ensures uniqueness."""
606:     current_tag = None
607:     processed_entries = set()  # Store (tag, clean_url) to check uniqueness
608:     result_urls = []
609: 
610:     for line in lines:
611:         clean_line = line.strip().lower()
612: 
613:         # Update the current tag when detected
614:         for prefix, (_, short_tag) in PREFIX_MAP.items():
615:             if (f"# {prefix}".lower() in clean_line) or (short_tag and short_tag.lower() in clean_line):
616:                 current_tag = prefix
617:                 break
618: 
619:         if not current_tag:
620:             continue
621: 
622:         # Normalise the delimiters and process each URL
623:         normalized_line = re.sub(r'[\s,]+', ',', line.strip())
624:         for url_entry in normalized_line.split(','):
625:             url = url_entry.split('#')[0].strip()
626:             if not url.startswith('http'):
627:                 continue
628: 
629:             clean_url = re.sub(r'\[.*?\]', '', url)
630:             entry_key = (current_tag, clean_url)    # Uniqueness is determined by a pair (tag, URL)
631: 
632:             if entry_key not in processed_entries:
633:                 filename = _extract_filename(url_entry)
634:                 formatted_url = f"{current_tag}:{clean_url}"
635:                 if filename:
636:                     formatted_url += f"[{filename}]"
637: 
638:                 result_urls.append(formatted_url)
639:                 processed_entries.add(entry_key)
640: 
641:     return ', '.join(result_urls) if result_urls else ''
642: 
643: def process_file_downloads(file_urls, additional_lines=None):
644:     """Reads URLs from files/HTTP sources."""
645:     lines = []
646: 
647:     if additional_lines:
648:         lines.extend(additional_lines.splitlines())
649: 
650:     for source in file_urls:
651:         if source.startswith('http'):
652:             try:
653:                 response = requests.get(_clean_url(source))
654:                 response.raise_for_status()
655:                 lines.extend(response.text.splitlines())
656:             except requests.RequestException:
657:                 continue
658:         else:
659:             try:
660:                 with open(source, 'r', encoding='utf-8') as f:
661:                     lines.extend(f.readlines())
662:             except FileNotFoundError:
663:                 continue
664: 
665:     return _process_lines(lines)
666: 
667: # File URLs processing
668: urls_sources = (Model_url, Vae_url, LoRA_url, Embedding_url, Extensions_url, ADetailer_url)
669: file_urls = [f"{f}.txt" if not f.endswith('.txt') else f for f in custom_file_urls.replace(',', '').split()] if custom_file_urls else []
670: 
671: # p -> prefix ; u -> url | Remember: don't touch the prefix!
672: prefixed_urls = [f"{p}:{u}" for p, u in zip(PREFIX_MAP, urls_sources) if u for u in u.replace(',', '').split()]
673: line += ', ' + ', '.join(prefixed_urls + [process_file_downloads(file_urls, empowerment_output)])
674: 
675: if detailed_download == 'on':
676:     print(f"\n\n{COL.Y}# ====== Подробная Загрузка ====== #\n{COL.X}")
677:     download(line)
678:     print(f"\n{COL.Y}# =============================== #\n{COL.X}")
679: else:
680:     with capture.capture_output():
681:         download(line)
682: 
683: print('\r🏁 Скачивание Завершено!' + ' '*15)
684: 
685: 
686: ## Install of Custom extensions
687: def _clone_repository(repo, repo_name, extension_dir):
688:     """Clones the repository to the specified directory."""
689:     repo_name = repo_name or repo.split('/')[-1]
690:     command = f"cd {extension_dir} && git clone --depth 1 --recursive {repo} {repo_name} && cd {repo_name} && git fetch"
691:     ipySys(command)
692: 
693: extension_type = 'нодов' if UI == 'ComfyUI' else 'расширений'
694: 
695: if extension_repo:
696:     print(f"✨ Установка кастомных {extension_type}...", end='')
697:     with capture.capture_output():
698:         for repo, repo_name in extension_repo:
699:             _clone_repository(repo, repo_name, extension_dir)
700:     print(f"\r📦 Установлено '{len(extension_repo)}' кастомных {extension_type}!")
701: 
702: 
703: # === SPECIAL ===
704: ## Sorting models `bbox` and `segm` | Only ComfyUI
705: if UI == 'ComfyUI':
706:     dirs = {'segm': '-seg.pt', 'bbox': None}
707:     for d in dirs:
708:         os.makedirs(os.path.join(adetailer_dir, d), exist_ok=True)
709: 
710:     for filename in os.listdir(adetailer_dir):
711:         src = os.path.join(adetailer_dir, filename)
712: 
713:         if os.path.isfile(src) and filename.endswith('.pt'):
714:             dest_dir = 'segm' if filename.endswith('-seg.pt') else 'bbox'
715:             dest = os.path.join(adetailer_dir, dest_dir, filename)
716: 
717:             if os.path.exists(dest):
718:                 os.remove(src)
719:             else:
720:                 shutil.move(src, dest)
721: 
722: 
723: ## List Models and stuff
724: ipyRun('run', f"{SCRIPTS}/download-result.py")
```

## File: scripts/ru/widgets-ru.py
```python
  1: # ~ widgets.py | by ANXETY ~
  2: 
  3: from widget_factory import WidgetFactory        # WIDGETS
  4: from webui_utils import update_current_webui    # WEBUI
  5: import json_utils as js                         # JSON
  6: 
  7: import ipywidgets as widgets
  8: from pathlib import Path
  9: import os
 10: 
 11: 
 12: # Constants
 13: HOME = Path.home()
 14: SCR_PATH = Path(HOME / 'ANXETY')
 15: SETTINGS_PATH = SCR_PATH / 'settings.json'
 16: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
 17: 
 18: SCRIPTS = SCR_PATH / 'scripts'
 19: 
 20: CSS = SCR_PATH / 'CSS'
 21: JS = SCR_PATH / 'JS'
 22: widgets_css = CSS / 'main-widgets.css'
 23: widgets_js = JS / 'main-widgets.js'
 24: 
 25: 
 26: ## ======================= WIDGETS =======================
 27: 
 28: def create_expandable_button(text, url):
 29:     return factory.create_html(f'''
 30:     <a href="{url}" target="_blank" class="button button_api">
 31:         <span class="icon"><</span>
 32:         <span class="text">{text}</span>
 33:     </a>
 34:     ''')
 35: 
 36: def read_model_data(file_path, data_type):
 37:     """Reads model, VAE, or ControlNet data from the specified file."""
 38:     type_map = {
 39:         'model': ('model_list', ['none']),
 40:         'vae': ('vae_list', ['none', 'ALL']),
 41:         'cnet': ('controlnet_list', ['none', 'ALL'])
 42:     }
 43:     key, prefixes = type_map[data_type]
 44:     local_vars = {}
 45: 
 46:     with open(file_path) as f:
 47:         exec(f.read(), {}, local_vars)
 48: 
 49:     names = list(local_vars[key].keys())
 50:     return prefixes + names
 51: 
 52: webui_selection = {
 53:     'A1111':   "--xformers --no-half-vae",
 54:     'ComfyUI': "--use-sage-attention --dont-print-server",
 55:     'Forge':   "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory",
 56:     'Classic': "--persistent-patches --cuda-stream --pin-shared-memory",    # Remove: --xformers
 57:     'ReForge': "--xformers --cuda-stream --pin-shared-memory",
 58:     'SD-UX':   "--xformers --no-half-vae"
 59: }
 60: 
 61: # Initialize the WidgetFactory
 62: factory = WidgetFactory()
 63: HR = widgets.HTML('<hr>')
 64: 
 65: # --- MODEL ---
 66: """Create model selection widgets."""
 67: model_header = factory.create_header('Выбор Модели')
 68: model_options = read_model_data(f"{SCRIPTS}/_models-data.py", 'model')
 69: model_widget = factory.create_dropdown(model_options, 'Модель:', '4. Counterfeit [Anime] [V3] + INP')
 70: model_num_widget = factory.create_text('Номер Модели:', '', 'Введите номера моделей для скачивания.')
 71: inpainting_model_widget = factory.create_checkbox('Inpainting Модели', False, class_names=['inpaint'], layout={'width': '25%'})
 72: XL_models_widget = factory.create_checkbox('SDXL', False, class_names=['sdxl'])
 73: 
 74: switch_model_widget = factory.create_hbox([inpainting_model_widget, XL_models_widget])
 75: 
 76: # --- VAE ---
 77: """Create VAE selection widgets."""
 78: vae_header = factory.create_header('Выбор VAE')
 79: vae_options = read_model_data(f"{SCRIPTS}/_models-data.py", 'vae')
 80: vae_widget = factory.create_dropdown(vae_options, 'Vae:', '3. Blessed2.vae')
 81: vae_num_widget = factory.create_text('Номер Vae:', '', 'Введите номера vae для скачивания.')
 82: 
 83: # --- ADDITIONAL ---
 84: """Create additional configuration widgets."""
 85: additional_header = factory.create_header('Дополнительно')
 86: latest_webui_widget = factory.create_checkbox('Обновить WebUI', True)
 87: latest_extensions_widget = factory.create_checkbox('Обновить Расширения', True)
 88: check_custom_nodes_deps_widget = factory.create_checkbox('Чекать зависимости Custom-Nodes', True)
 89: change_webui_widget = factory.create_dropdown(list(webui_selection.keys()), 'WebUI:', 'A1111', layout={'width': 'auto'})
 90: detailed_download_widget = factory.create_dropdown(['off', 'on'], 'Подробная Загрузка:', 'off', layout={'width': 'auto'})
 91: choose_changes_widget = factory.create_hbox(
 92:     [
 93:         latest_webui_widget,
 94:         latest_extensions_widget,
 95:         check_custom_nodes_deps_widget,   # Only ComfyUI
 96:         change_webui_widget,
 97:         detailed_download_widget
 98:     ],
 99:     layout={'justify_content': 'space-between'}
100: )
101: 
102: controlnet_options = read_model_data(f"{SCRIPTS}/_models-data.py", 'cnet')
103: controlnet_widget = factory.create_dropdown(controlnet_options, 'ControlNet:', 'none')
104: controlnet_num_widget = factory.create_text('Номер ControlNet:', '', 'Введите номера моделей ControlNet для скачивания.')
105: commit_hash_widget = factory.create_text('Commit Hash:', '', 'Переключение между ветвями или коммитами.')
106: 
107: civitai_token_widget = factory.create_text('CivitAI Token:', '', 'Введите свой API-токен CivitAi.')
108: civitai_button = create_expandable_button('Получить CivitAI Токен', 'https://civitai.com/user/account')
109: civitai_widget = factory.create_hbox([civitai_token_widget, civitai_button])
110: 
111: huggingface_token_widget = factory.create_text('HuggingFace Token:')
112: huggingface_button = create_expandable_button('Получить HuggingFace Токен', 'https://huggingface.co/settings/tokens')
113: huggingface_widget = factory.create_hbox([huggingface_token_widget, huggingface_button])
114: 
115: ngrok_token_widget = factory.create_text('Ngrok Token:')
116: ngrok_button = create_expandable_button('Получить Ngrok Токен', 'https://dashboard.ngrok.com/get-started/your-authtoken')
117: ngrok_widget = factory.create_hbox([ngrok_token_widget, ngrok_button])
118: 
119: zrok_token_widget = factory.create_text('Zrok Token:')
120: zrok_button = create_expandable_button('Зарегать Zrok Токен', 'https://colab.research.google.com/drive/1d2sjWDJi_GYBUavrHSuQyHTDuLy36WpU')
121: zrok_widget = factory.create_hbox([zrok_token_widget, zrok_button])
122: 
123: commandline_arguments_widget = factory.create_text('Аргументы:', webui_selection['A1111'])
124: 
125: accent_colors_options = ['anxety', 'blue', 'green', 'peach', 'pink', 'red', 'yellow']
126: theme_accent_widget = factory.create_dropdown(accent_colors_options, 'Акцент Темы:', 'anxety',
127:                                               layout={'width': 'auto', 'margin': '0 0 0 8px'})    # margin-left
128: 
129: additional_footer = factory.create_hbox([commandline_arguments_widget, theme_accent_widget])
130: 
131: additional_widget_list = [
132:     additional_header,
133:     choose_changes_widget,
134:     HR,
135:     controlnet_widget, controlnet_num_widget,
136:     commit_hash_widget,
137:     civitai_widget, huggingface_widget, zrok_widget, ngrok_widget,
138:     HR,
139:     # commandline_arguments_widget,
140:     additional_footer
141: ]
142: 
143: # --- CUSTOM DOWNLOAD ---
144: """Create Custom-Download Selection widgets."""
145: custom_download_header_popup = factory.create_html('''
146: <div class="header" style="cursor: pointer;" onclick="toggleContainer()">Кастомная Загрузка</div>
147: <div class="info" id="info_dl">INFO</div>
148: <div class="popup">
149:     Разделите несколько URL-адресов запятой/пробелом.
150:     Для <span class="file_name">пользовательского имени</span> файла/расширения укажите его через <span class="braces">[]</span> после URL без пробелов.
151:     <span class="required">Для файлов обязательно укажите</span> - <span class="extension">Расширение Файла.</span>
152:     <div class="sample">
153:         <span class="sample_label">Пример для Файла:</span>
154:         https://civitai.com/api/download/models/229782<span class="braces">[</span><span class="file_name">Detailer</span><span class="extension">.safetensors</span><span class="braces">]</span>
155:         <br>
156:         <span class="sample_label">Пример для Расширения:</span>
157:         https://github.com/hako-mikan/sd-webui-regional-prompter<span class="braces">[</span><span class="file_name">Regional-Prompter</span><span class="braces">]</span>
158:     </div>
159: </div>
160: ''')
161: 
162: empowerment_widget = factory.create_checkbox('Расширение возможностей', False, class_names=['empowerment'])
163: empowerment_output_widget = factory.create_textarea(
164: '', '', """Используйте специальные теги. Портативный аналог "Файл (txt)"
165: Теги: model (ckpt), vae, lora, embed (emb), extension (ext), adetailer (ad), control (cnet), upscale (ups), clip, unet, vision (vis), encoder (enc), diffusion (diff), config (cfg)
166: Короткие-теги: начинаются с '$' без пробела -> $ckpt
167: ------ Например ------
168: 
169: # Lora
170: https://civitai.com/api/download/models/229782
171: 
172: $ext
173: https://github.com/hako-mikan/sd-webui-cd-tuner[CD-Tuner]
174: """)
175: 
176: Model_url_widget = factory.create_text('Model:')
177: Vae_url_widget = factory.create_text('Vae:')
178: LoRA_url_widget = factory.create_text('LoRa:')
179: Embedding_url_widget = factory.create_text('Embedding:')
180: Extensions_url_widget = factory.create_text('Extensions:')
181: ADetailer_url_widget = factory.create_text('ADetailer:')
182: custom_file_urls_widget = factory.create_text('Файл (txt):')
183: 
184: # --- Save Button ---
185: """Create button widgets."""
186: save_button = factory.create_button('Сохранить', class_names=['button', 'button_save'])
187: 
188: 
189: ## ============ MODULE | GDrive Toggle Button ============
190: """Create Google Drive toggle button for Colab only."""
191: from pathlib import Path
192: 
193: TOOLTIPS = ("Отключить Гугл Диск", "Подключить Гугл Диск")
194: BTN_STYLE = {'width': '48px', 'height': '48px'}
195: 
196: GD_status = js.read(SETTINGS_PATH, 'mountGDrive') or False
197: GDrive_button = factory.create_button('', layout=BTN_STYLE, class_names=['gdrive-btn'])
198: 
199: # Init
200: GDrive_button.tooltip = TOOLTIPS[0] if GD_status else TOOLTIPS[1]
201: 
202: if ENV_NAME == 'Google Colab':
203:     GDrive_button.toggle = GD_status
204:     if GDrive_button.toggle:
205:         GDrive_button.add_class('active')
206: 
207:     def handle_toggle(btn):
208:         """Toggle Google Drive button state"""
209:         btn.toggle = not btn.toggle
210:         btn.tooltip = TOOLTIPS[0] if btn.toggle else TOOLTIPS[1]
211:         btn.add_class('active') if btn.toggle else btn.remove_class('active')
212: 
213:     GDrive_button.on_click(handle_toggle)
214: else:
215:     GDrive_button.layout.display = 'none'   # Hide GD-btn if ENV is not Colab
216: 
217: 
218: ## ================== DISPLAY / SETTINGS =================
219: 
220: factory.load_css(widgets_css)   # load CSS (widgets)
221: factory.load_js(widgets_js)     # load JS (widgets)
222: 
223: # Display sections
224: model_widgets = [model_header, model_widget, model_num_widget, switch_model_widget]
225: vae_widgets = [vae_header, vae_widget, vae_num_widget]
226: additional_widgets = additional_widget_list
227: custom_download_widgets = [
228:     custom_download_header_popup,
229:     empowerment_widget,
230:     empowerment_output_widget,
231:     Model_url_widget,
232:     Vae_url_widget,
233:     LoRA_url_widget,
234:     Embedding_url_widget,
235:     Extensions_url_widget,
236:     ADetailer_url_widget,
237:     custom_file_urls_widget
238: ]
239: 
240: # Create Boxes
241: # model_box = factory.create_vbox(model_widgets, class_names=['container'])
242: model_content = factory.create_vbox(model_widgets, class_names=['container'])   # With GD-btn :#
243: model_box = factory.create_hbox([model_content, GDrive_button], layout={'width': '1150px'})   # fix layout width...
244: 
245: vae_box = factory.create_vbox(vae_widgets, class_names=['container'])
246: additional_box = factory.create_vbox(additional_widgets, class_names=['container'])
247: custom_download_box = factory.create_vbox(custom_download_widgets, class_names=['container', 'container_cdl'])
248: 
249: WIDGET_LIST = factory.create_vbox([model_box, vae_box, additional_box, custom_download_box, save_button],
250:                                   class_names=['mainContainer'])
251: factory.display(WIDGET_LIST)
252: 
253: ## ================== CALLBACK FUNCTION ==================
254: 
255: # Initialize visibility | hidden
256: check_custom_nodes_deps_widget.layout.display = 'none'
257: empowerment_output_widget.add_class('empowerment-output')
258: empowerment_output_widget.add_class('hidden')
259: 
260: # Callback functions for XL options
261: def update_XL_options(change, widget):
262:     selected = change['new']
263: 
264:     default_model_values = {
265:         True: ('4. WAI-illustrious [Anime] [V14] [XL]', 'none', 'none'),           # XL models
266:         False: ('4. Counterfeit [Anime] [V3] + INP', '3. Blessed2.vae', 'none')    # SD 1.5 models
267:     }
268: 
269:     # Get data - MODELs | VAEs | CNETs
270:     data_file = '_xl-models-data.py' if selected else '_models-data.py'
271:     model_widget.options = read_model_data(f"{SCRIPTS}/{data_file}", 'model')
272:     vae_widget.options = read_model_data(f"{SCRIPTS}/{data_file}", 'vae')
273:     controlnet_widget.options = read_model_data(f"{SCRIPTS}/{data_file}", 'cnet')
274: 
275:     # Set default values from the dictionary
276:     model_widget.value, vae_widget.value, controlnet_widget.value = default_model_values[selected]
277: 
278: # Callback functions for updating widgets
279: def update_change_webui(change, widget):
280:     selected_webui = change['new']
281:     commandline_arguments = webui_selection.get(selected_webui, '')
282:     commandline_arguments_widget.value = commandline_arguments
283: 
284:     if selected_webui == 'ComfyUI':
285:         latest_extensions_widget.layout.display = 'none'
286:         latest_extensions_widget.value = False
287:         check_custom_nodes_deps_widget.layout.display = ''
288:         theme_accent_widget.layout.display = 'none'
289:         theme_accent_widget.value = 'anxety'
290:         Extensions_url_widget.description = 'Custom Nodes:'
291:     else:
292:         latest_extensions_widget.layout.display = ''
293:         latest_extensions_widget.value = True
294:         check_custom_nodes_deps_widget.layout.display = 'none'
295:         theme_accent_widget.layout.display = ''
296:         theme_accent_widget.value = 'anxety'
297:         Extensions_url_widget.description = 'Extensions:'
298: 
299: # Callback functions for Empowerment
300: def update_empowerment(change, widget):
301:     selected_emp = change['new']
302: 
303:     customDL_widgets = [
304:         Model_url_widget,
305:         Vae_url_widget,
306:         LoRA_url_widget,
307:         Embedding_url_widget,
308:         Extensions_url_widget,
309:         ADetailer_url_widget
310:     ]
311:     for widget in customDL_widgets:    # For switching animation
312:         widget.add_class('empowerment-text-field')
313: 
314:     # idk why, but that's the way it's supposed to be >_<'
315:     if selected_emp:
316:         for wg in customDL_widgets:
317:             wg.add_class('hidden')
318:         empowerment_output_widget.remove_class('hidden')
319:     else:
320:         for wg in customDL_widgets:
321:             wg.remove_class('hidden')
322:         empowerment_output_widget.add_class('hidden')
323: 
324: # Connecting widgets
325: factory.connect_widgets([(change_webui_widget, 'value')], update_change_webui)
326: factory.connect_widgets([(XL_models_widget, 'value')], update_XL_options)
327: factory.connect_widgets([(empowerment_widget, 'value')], update_empowerment)
328: 
329: ## ============== Load / Save - Settings V4 ==============
330: 
331: SETTINGS_KEYS = [
332:       'XL_models', 'model', 'model_num', 'inpainting_model', 'vae', 'vae_num',
333:       'latest_webui', 'latest_extensions', 'check_custom_nodes_deps', 'change_webui', 'detailed_download',
334:       'controlnet', 'controlnet_num', 'commit_hash',
335:       'civitai_token', 'huggingface_token', 'zrok_token', 'ngrok_token', 'commandline_arguments', 'theme_accent',
336:       # CustomDL
337:       'empowerment', 'empowerment_output',
338:       'Model_url', 'Vae_url', 'LoRA_url', 'Embedding_url', 'Extensions_url', 'ADetailer_url',
339:       'custom_file_urls'
340: ]
341: 
342: def save_settings():
343:     """Save widget values to settings."""
344:     widgets_values = {key: globals()[f"{key}_widget"].value for key in SETTINGS_KEYS}
345:     js.save(SETTINGS_PATH, 'WIDGETS', widgets_values)
346: 
347:     # Save Status GDrive-btn
348:     js.save(SETTINGS_PATH, 'mountGDrive', True if GDrive_button.toggle else False)
349: 
350:     update_current_webui(change_webui_widget.value)  # Update Selected WebUI in setting.json
351: 
352: def load_settings():
353:     """Load widget values from settings."""
354:     if js.key_exists(SETTINGS_PATH, 'WIDGETS'):
355:         widget_data = js.read(SETTINGS_PATH, 'WIDGETS')
356:         for key in SETTINGS_KEYS:
357:             if key in widget_data:
358:                 globals()[f"{key}_widget"].value = widget_data.get(key, '')
359: 
360:     # Load Status GDrive-btn
361:     GD_status = js.read(SETTINGS_PATH, 'mountGDrive') or False
362:     GDrive_button.toggle = (GD_status == True)
363:     if GDrive_button.toggle:
364:         GDrive_button.add_class('active')
365:     else:
366:         GDrive_button.remove_class('active')
367: 
368: def save_data(button):
369:     """Handle save button click."""
370:     save_settings()
371:     # factory.close(list(WIDGET_LIST.children), class_names=['hide'], delay=0.8)
372:     all_widgets = [model_content, vae_box, additional_box, custom_download_box, save_button, GDrive_button]
373:     factory.close(all_widgets, class_names=['hide'], delay=0.8)
374: 
375: load_settings()
376: save_button.on_click(save_data)
```

## File: scripts/UIs/A1111.py
```python
  1: # ~ A1111.py | by ANXETY ~
  2: 
  3: from Manager import m_download, m_clone    # Every Download | Clone
  4: import json_utils as js                    # JSON
  5: 
  6: from IPython.display import clear_output
  7: from IPython.utils import capture
  8: from IPython import get_ipython
  9: from pathlib import Path
 10: import subprocess
 11: import asyncio
 12: import os
 13: import shutil # Import shutil for rmtree
 14: 
 15: CD = os.chdir
 16: ipySys = get_ipython().system
 17: 
 18: # Constants
 19: UI = 'A1111'
 20: 
 21: HOME = Path.home()
 22: WEBUI = HOME / UI
 23: VENV = HOME / 'venv'
 24: SCR_PATH = HOME / 'ANXETY'
 25: SETTINGS_PATH = SCR_PATH / 'settings.json'
 26: 
 27: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
 28: 
 29: REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
 30: FORK_REPO = js.read(SETTINGS_PATH, 'ENVIRONMENT.fork')
 31: BRANCH = js.read(SETTINGS_PATH, 'ENVIRONMENT.branch')
 32: EXTS = js.read(SETTINGS_PATH, 'WEBUI.extension_dir')
 33: 
 34: CD(HOME)
 35: 
 36: ## ================== WEB UI OPERATIONS ==================
 37: 
 38: async def _download_file(url, directory, filename):
 39:     """Downloads a single file."""
 40:     os.makedirs(directory, exist_ok=True)
 41:     file_path = os.path.join(directory, filename)
 42: 
 43:     if os.path.exists(file_path):
 44:         os.remove(file_path)
 45: 
 46:     process = await asyncio.create_subprocess_shell(
 47:         f"curl -sLo {file_path} {url}",
 48:         stdout=subprocess.DEVNULL,
 49:         stderr=subprocess.DEVNULL
 50:     )
 51:     await process.communicate()
 52: 
 53: async def download_files(file_list):
 54:     """Downloads multiple files asynchronously."""
 55:     tasks = []
 56:     for file_info in file_list:
 57:         parts = file_info.split(',')
 58:         url = parts[0].strip()
 59:         directory = parts[1].strip() if len(parts) > 1 else WEBUI   # Default Save Path
 60:         filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
 61:         tasks.append(_download_file(url, directory, filename))
 62:     await asyncio.gather(*tasks)
 63: 
 64: async def download_configuration():
 65:     """Downloads configuration files and clones extensions."""
 66:     ## FILES
 67:     url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
 68:     configs = [
 69:         # settings
 70:         f"{url_cfg}/{UI}/config.json",
 71:         f"{url_cfg}/{UI}/ui-config.json",
 72:         f"{url_cfg}/styles.csv",
 73:         f"{url_cfg}/user.css",
 74:         # other | UI
 75:         f"{url_cfg}/card-no-preview.png, {WEBUI}/html",
 76:         f"{url_cfg}/notification.mp3",
 77:         # other | tunneling
 78:         f"{url_cfg}/gradio-tunneling.py, {VENV}/lib/python3.10/site-packages/gradio_tunneling, main.py"  # Replace py-Script
 79:     ]
 80:     await download_files(configs)
 81: 
 82:     ## REPOS
 83:     extensions_list = [
 84:         ## ANXETY Edits
 85:         'https://github.com/anxety-solo/webui_timer timer',
 86:         'https://github.com/anxety-solo/anxety-theme',
 87:         'https://github.com/anxety-solo/sd-civitai-browser-plus Civitai-Browser-Plus',
 88: 
 89:         ## NEW Extensions
 90:         'https://github.com/Haoming02/sd-webui-mosaic-outpaint',
 91:         'https://github.com/continue-revolution/sd-webui-segment-anything',
 92:         'https://github.com/kainatquaderee/sd-webui-reactor-Nsfw_freedom',
 93:         'https://github.com/a2569875/lora-prompt-tool',
 94:         'https://github.com/Uminosachi/sd-webui-inpaint-anything',
 95:         'https://github.com/redmercy69/sd-webui-stripper',
 96:         'https://github.com/diffus-me/sd-webui-facefusion',
 97:         'https://github.com/glucauze/sd-webui-faceswaplab',
 98:         'https://github.com/IntellectzProductions/sd-webui-faceswap',
 99:         'https://github.com/yownas/sd-webui-faceswapper',
100:         'https://github.com/leeguandong/sd_webui_outpainting',
101:         'https://github.com/thoraxe69/sd-webui-roop',
102: 
103:         ## Gutris1
104:         'https://github.com/gutris1/sd-image-viewer Image-Viewer',
105:         'https://github.com/gutris1/sd-image-info Image-Info',
106:         'https://github.com/gutris1/sd-hub SD-Hub',
107: 
108:         ## OTHER | ON
109:         'https://github.com/Bing-su/adetailer',
110:     ]
111:     if ENV_NAME == 'Kaggle':
112:         extensions_list.append('https://github.com/gutris1/sd-encrypt-image Encrypt-Image')
113: 
114:     os.makedirs(EXTS, exist_ok=True)
115:     CD(EXTS)
116: 
117:     tasks = []
118:     for command in extensions_list:
119:         tasks.append(asyncio.create_subprocess_shell(
120:             f"git clone --depth 1 {command}",
121:             stdout=subprocess.DEVNULL,
122:             stderr=subprocess.DEVNULL
123:         ))
124: 
125:     await asyncio.gather(*tasks)
126: 
127: def unpack_webui():
128:     """Unpacks the WebUI zip file and cleans up model-related directories."""
129:     zip_path = f"{HOME}/{UI}.zip"
130:     m_download(f"{REPO_URL} {HOME} {UI}.zip")
131:     ipySys(f"unzip -q -o {zip_path} -d {WEBUI}")
132:     ipySys(f"rm -rf {zip_path}")
133:     
134:     # --- START OF MODIFICATION ---
135:     # Define model-related directories that should NOT be in the WebUI folder
136:     # as they are handled by the shared model base.
137:     model_dirs_to_clean = [
138:         WEBUI / 'models',
139:         WEBUI / 'VAE',
140:         WEBUI / 'Lora',
141:         WEBUI / 'embeddings',
142:         WEBUI / 'ControlNet',
143:     ]
144: 
145:     print(f"🧹 Cleaning up unzipped model-related directories within {UI}...")
146:     for d in model_dirs_to_clean:
147:         if d.exists() and d.is_dir():
148:             print(f"   Deleting: {d}")
149:             try:
150:                 shutil.rmtree(d)
151:             except OSError as e:
152:                 print(f"   Error deleting {d}: {e}")
153:     # --- END OF MODIFICATION ---
154: 
155: ## ====================== MAIN CODE ======================
156: if __name__ == '__main__':
157:     with capture.capture_output():
158:         unpack_webui()
159:         asyncio.run(download_configuration())
```

## File: scripts/UIs/Classic.py
```python
  1: # ~ Classic.py | by ANXETY ~
  2: 
  3: from Manager import m_download, m_clone    # Every Download | Clone
  4: import json_utils as js                    # JSON
  5: 
  6: from IPython.display import clear_output
  7: from IPython.utils import capture
  8: from IPython import get_ipython
  9: from pathlib import Path
 10: import subprocess
 11: import asyncio
 12: import os
 13: import shutil # Import shutil for rmtree
 14: 
 15: CD = os.chdir
 16: ipySys = get_ipython().system
 17: 
 18: # Constants
 19: UI = 'Classic'
 20: 
 21: HOME = Path.home()
 22: WEBUI = HOME / UI
 23: VENV = HOME / 'venv'
 24: SCR_PATH = HOME / 'ANXETY'
 25: SETTINGS_PATH = SCR_PATH / 'settings.json'
 26: 
 27: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
 28: 
 29: REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
 30: FORK_REPO = js.read(SETTINGS_PATH, 'ENVIRONMENT.fork')
 31: BRANCH = js.read(SETTINGS_PATH, 'ENVIRONMENT.branch')
 32: EXTS = js.read(SETTINGS_PATH, 'WEBUI.extension_dir')
 33: 
 34: CD(HOME)
 35: 
 36: 
 37: ## ================== WEB UI OPERATIONS ==================
 38: 
 39: async def _download_file(url, directory, filename):
 40:     """Downloads a single file."""
 41:     os.makedirs(directory, exist_ok=True)
 42:     file_path = os.path.join(directory, filename)
 43: 
 44:     if os.path.exists(file_path):
 45:         os.remove(file_path)
 46: 
 47:     process = await asyncio.create_subprocess_shell(
 48:         f"curl -sLo {file_path} {url}",
 49:         stdout=subprocess.DEVNULL,
 50:         stderr=subprocess.DEVNULL
 51:     )
 52:     await process.communicate()
 53: 
 54: async def download_files(file_list):
 55:     """Downloads multiple files asynchronously."""
 56:     tasks = []
 57:     for file_info in file_list:
 58:         parts = file_info.split(',')
 59:         url = parts[0].strip()
 60:         directory = parts[1].strip() if len(parts) > 1 else WEBUI   # Default Save Path
 61:         filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
 62:         tasks.append(_download_file(url, directory, filename))
 63:     await asyncio.gather(*tasks)
 64: 
 65: async def download_configuration():
 66:     """Downloads configuration files and clones extensions."""
 67:     ## FILES
 68:     url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
 69:     configs = [
 70:         # settings
 71:         f"{url_cfg}/{UI}/config.json",
 72:         f"{url_cfg}/{UI}/ui-config.json",
 73:         f"{url_cfg}/styles.csv",
 74:         f"{url_cfg}/user.css",
 75:         # other | UI
 76:         f"{url_cfg}/notification.mp3",
 77:         # other | tunneling
 78:         f"{url_cfg}/gradio-tunneling.py, {VENV}/lib/python3.11/site-packages/gradio_tunneling, main.py"  # Replace py-Script
 79:     ]
 80:     await download_files(configs)
 81: 
 82:     ## REPOS
 83:     extensions_list = [
 84:         ## ANXETY Edits
 85:         'https://github.com/anxety-solo/webui_timer timer',
 86:         'https://github.com/anxety-solo/anxety-theme',
 87:         'https://github.com/anxety-solo/sd-civitai-browser-plus Civitai-Browser-Plus',
 88: 
 89:         ## Gutris1
 90:         # 'https://github.com/gutris1/sd-image-viewer Image-Viewer',    # Not Working
 91:         'https://github.com/gutris1/sd-image-info Image-Info',
 92:         'https://github.com/gutris1/sd-hub SD-Hub',
 93: 
 94:         ## OTHER | ON
 95:         'https://github.com/Bing-su/adetailer',
 96: 
 97:         ## NEW Extensions
 98:         'https://github.com/Haoming02/sd-webui-mosaic-outpaint',
 99:         'https://github.com/continue-revolution/sd-webui-segment-anything',
100:         'https://github.com/kainatquaderee/sd-webui-reactor-Nsfw_freedom',
101:         'https://github.com/a2569875/lora-prompt-tool',
102:         'https://github.com/Uminosachi/sd-webui-inpaint-anything',
103:         'https://github.com/redmercy69/sd-webui-stripper',
104:         'https://github.com/diffus-me/sd-webui-facefusion',
105:         'https://github.com/glucauze/sd-webui-faceswaplab',
106:         'https://github.com/IntellectzProductions/sd-webui-faceswap',
107:         'https://github.com/yownas/sd-webui-faceswapper',
108:         'https://github.com/leeguandong/sd_webui_outpainting',
109:         'https://github.com/thoraxe69/sd-webui-roop',
110: 
111:         ## OTHER | OFF
112:         # 'https://github.com/thomasasfk/sd-webui-aspect-ratio-helper Aspect-Ratio-Helper',
113:         # 'https://github.com/zanllp/sd-webui-infinite-image-browsing Infinite-Image-Browsing',
114:         # 'https://github.com/Haoming02/sd-forge-couple SD-Couple',
115:         # 'https://github.com/ilian6806/stable-diffusion-webui-state State',
116:         # 'https://github.com/DominikDoom/a1111-sd-webui-tagcomplete TagComplete',
117:         # 'https://github.com/Tsukreya/Umi-AI-Wildcards'
118:     ]
119:     if ENV_NAME == 'Kaggle':
120:         extensions_list.append('https://github.com/gutris1/sd-encrypt-image Encrypt-Image')
121: 
122:     os.makedirs(EXTS, exist_ok=True)
123:     CD(EXTS)
124: 
125:     tasks = []
126:     for command in extensions_list:
127:         tasks.append(asyncio.create_subprocess_shell(
128:             f"git clone --depth 1 {command}",
129:             stdout=subprocess.DEVNULL,
130:             stderr=subprocess.DEVNULL
131:         ))
132: 
133:     await asyncio.gather(*tasks)
134: 
135: def unpack_webui():
136:     """Unpacks the WebUI zip file and cleans up model-related directories."""
137:     zip_path = f"{HOME}/{UI}.zip"
138:     m_download(f"{REPO_URL} {HOME} {UI}.zip")
139:     ipySys(f"unzip -q -o {zip_path} -d {WEBUI}")
140:     ipySys(f"rm -rf {zip_path}")
141: 
142:     # --- START OF MODIFICATION ---
143:     # Define model-related directories that should NOT be in the WebUI folder
144:     # as they are handled by the shared model base.
145:     model_dirs_to_clean = [
146:         WEBUI / 'Stable-diffusion', # For Classic UI
147:         WEBUI / 'VAE',
148:         WEBUI / 'Lora',
149:         WEBUI / 'embeddings',
150:         WEBUI / 'ESRGAN', # Upscale models for Classic
151:         # Add any other subdirectories that might contain large model files
152:         # but are not needed within the UI's specific folder.
153:     ]
154: 
155:     print(f"🧹 Cleaning up unzipped model-related directories within {UI}...")
156:     for d in model_dirs_to_clean:
157:         if d.exists() and d.is_dir():
158:             print(f"   Deleting: {d}")
159:             try:
160:                 shutil.rmtree(d)
161:             except OSError as e:
162:                 print(f"   Error deleting {d}: {e}")
163:     # --- END OF MODIFICATION ---
164: 
165: def fixes_modules():
166:     """Applies specific fixes to Classic UI modules."""
167:     path = WEBUI / "modules/cmd_args.py"
168:     if not path.exists():
169:         return
170: 
171:     marker = '# Arguments added by ANXETY'
172:     with open(path, 'r+', encoding='utf-8') as f:
173:         if marker in f.read():
174:             return
175: 
176:         f.write(f"\n\n{marker}\n")
177:         f.write('parser.add_argument("--hypernetwork-dir", type=normalized_filepath, '
178:                'default=os.path.join(models_path, \'hypernetworks\'), help="hypernetwork directory")')
179: 
180: ## ====================== MAIN CODE ======================
181: if __name__ == '__main__':
182:     with capture.capture_output():
183:         unpack_webui()
184:         asyncio.run(download_configuration())
185:         fixes_modules()
```

## File: scripts/UIs/ComfyUI.py
```python
  1: # ~ ComfyUI.py | by ANXETY ~
  2: 
  3: from Manager import m_download, m_clone    # Every Download | Clone
  4: import json_utils as js                    # JSON
  5: 
  6: from IPython.display import clear_output
  7: from IPython.utils import capture
  8: from IPython import get_ipython
  9: from pathlib import Path
 10: import subprocess
 11: import asyncio
 12: import os
 13: import shutil # Import shutil for rmtree
 14: 
 15: CD = os.chdir
 16: ipySys = get_ipython().system
 17: 
 18: # Constants
 19: UI = 'ComfyUI'
 20: 
 21: HOME = Path.home()
 22: VENV = HOME / 'venv'
 23: WEBUI = HOME / UI
 24: SCR_PATH = HOME / 'ANXETY'
 25: SETTINGS_PATH = SCR_PATH / 'settings.json'
 26: 
 27: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
 28: 
 29: REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
 30: FORK_REPO = js.read(SETTINGS_PATH, 'ENVIRONMENT.fork')
 31: BRANCH = js.read(SETTINGS_PATH, 'ENVIRONMENT.branch')
 32: EXTS = js.read(SETTINGS_PATH, 'WEBUI.extension_dir')
 33: 
 34: CD(HOME)
 35: 
 36: 
 37: ## ================== WEB UI OPERATIONS ==================
 38: 
 39: async def _download_file(url, directory, filename):
 40:     """Downloads a single file."""
 41:     os.makedirs(directory, exist_ok=True)
 42:     file_path = os.path.join(directory, filename)
 43:     process = await asyncio.create_subprocess_shell(
 44:         f"curl -sLo {file_path} {url}",
 45:         stdout=subprocess.DEVNULL,
 46:         stderr=subprocess.DEVNULL
 47:     )
 48:     await process.communicate()
 49: 
 50: async def download_files(file_list):
 51:     """Downloads multiple files asynchronously."""
 52:     tasks = []
 53:     for file_info in file_list:
 54:         parts = file_info.split(',')
 55:         url = parts[0].strip()
 56:         directory = parts[1].strip() if len(parts) > 1 else WEBUI   # Default Save Path
 57:         filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
 58:         tasks.append(_download_file(url, directory, filename))
 59:     await asyncio.gather(*tasks)
 60: 
 61: async def download_configuration():
 62:     """Downloads configuration files and clones extensions."""
 63:     ## FILES
 64:     url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
 65:     files = [
 66:         # settings
 67:         f"{url_cfg}/{UI}/install-deps.py",
 68:         f"{url_cfg}/{UI}/comfy.settings.json, {WEBUI}/user/default",                         # ComfyUI settings
 69:         f"{url_cfg}/{UI}/Comfy-Manager/config.ini, {WEBUI}/user/default/ComfyUI-Manager",    # ComfyUI-Manager settings
 70:         # workflows
 71:         f"{url_cfg}/{UI}/workflows/anxety-workflow.json, {WEBUI}/user/default/workflows",
 72:         # other | tunneling
 73:         f"{url_cfg}/gradio-tunneling.py, {VENV}/lib/python3.10/site-packages/gradio_tunneling, main.py"  # Replace py-Script
 74:     ]
 75:     await download_files(files)
 76: 
 77:     ## REPOS
 78:     extensions_list = [
 79:         'https://github.com/Fannovel16/comfyui_controlnet_aux',
 80:         'https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet',
 81:         'https://github.com/hayden-fr/ComfyUI-Model-Manager',
 82:         'https://github.com/jags111/efficiency-nodes-comfyui',
 83:         'https://github.com/ltdrdata/ComfyUI-Impact-Pack',
 84:         'https://github.com/ltdrdata/ComfyUI-Impact-Subpack',
 85:         'https://github.com/ltdrdata/ComfyUI-Manager',
 86:         'https://github.com/pythongosssss/ComfyUI-Custom-Scripts',
 87:         'https://github.com/pythongosssss/ComfyUI-WD14-Tagger',
 88:         'https://github.com/ssitu/ComfyUI_UltimateSDUpscale',
 89:         'https://github.com/WASasquatch/was-node-suite-comfyui'
 90:     ]
 91:     os.makedirs(EXTS, exist_ok=True)
 92:     CD(EXTS)
 93: 
 94:     tasks = []
 95:     for command in extensions_list:
 96:         tasks.append(asyncio.create_subprocess_shell(
 97:             f"git clone --depth 1 --recursive {command}",
 98:             stdout=subprocess.DEVNULL,
 99:             stderr=subprocess.DEVNULL
100:         ))
101: 
102:     await asyncio.gather(*tasks)
103: 
104: def unpack_webui():
105:     """Unpacks the WebUI zip file and cleans up model-related directories."""
106:     zip_path = f"{HOME}/{UI}.zip"
107:     m_download(f"{REPO_URL} {HOME} {UI}.zip")
108:     ipySys(f"unzip -q -o {zip_path} -d {WEBUI}")
109:     ipySys(f"rm -rf {zip_path}")
110:     
111:     # --- START OF MODIFICATION ---
112:     # Define model-related directories that should NOT be in the WebUI folder
113:     # as they are handled by the shared model base for ComfyUI.
114:     model_dirs_to_clean = [
115:         WEBUI / 'models', # Sometimes present, needs to be removed
116:         WEBUI / 'checkpoints',
117:         WEBUI / 'vae',
118:         WEBUI / 'loras',
119:         # 'custom_nodes' is typically handled by extensions cloning directly to EXTS (WEBUI/custom_nodes)
120:         # So it's generally safe to remove if found here, as proper nodes are in EXTS.
121:         WEBUI / 'custom_nodes', 
122:         WEBUI / 'embeddings', # ComfyUI might unpack this as 'embeddings'
123:         WEBUI / 'controlnet', # ComfyUI might unpack this as 'controlnet'
124:         WEBUI / 'upscale_models' # For ComfyUI
125:     ]
126: 
127:     print(f"🧹 Cleaning up unzipped model-related directories within {UI}...")
128:     for d in model_dirs_to_clean:
129:         if d.exists() and d.is_dir():
130:             print(f"   Deleting: {d}")
131:             try:
132:                 shutil.rmtree(d)
133:             except OSError as e:
134:                 print(f"   Error deleting {d}: {e}")
135:     # --- END OF MODIFICATION ---
136: 
137: ## ====================== MAIN CODE ======================
138: if __name__ == '__main__':
139:     with capture.capture_output():
140:         unpack_webui()
141:         asyncio.run(download_configuration())
```

## File: scripts/UIs/Forge.py
```python
  1: # ~ Forge.py | by ANXETY ~
  2: 
  3: from Manager import m_download, m_clone    # Every Download | Clone
  4: import json_utils as js                    # JSON
  5: 
  6: from IPython.display import clear_output
  7: # from IPython.utils import capture # REMOVED: To show verbose output
  8: from IPython import get_ipython
  9: from pathlib import Path
 10: import subprocess
 11: import asyncio
 12: import os
 13: import shutil # Import shutil for rmtree
 14: 
 15: CD = os.chdir
 16: ipySys = get_ipython().system
 17: 
 18: # Constants
 19: UI = 'Forge'
 20: 
 21: HOME = Path.home()
 22: WEBUI = HOME / UI
 23: VENV = HOME / 'venv'
 24: SCR_PATH = HOME / 'ANXETY'
 25: SETTINGS_PATH = SCR_PATH / 'settings.json'
 26: 
 27: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
 28: 
 29: REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
 30: FORK_REPO = js.read(SETTINGS_PATH, 'ENVIRONMENT.fork')
 31: BRANCH = js.read(SETTINGS_PATH, 'ENVIRONMENT.branch')
 32: EXTS = js.read(SETTINGS_PATH, 'WEBUI.extension_dir')
 33: 
 34: CD(HOME)
 35: 
 36: 
 37: ## ================== WEB UI OPERATIONS ==================
 38: 
 39: async def _download_file(url, directory, filename):
 40:     """Downloads a single file."""
 41:     os.makedirs(directory, exist_ok=True)
 42:     file_path = os.path.join(directory, filename)
 43: 
 44:     if os.path.exists(file_path):
 45:         os.remove(file_path)
 46: 
 47:     process = await asyncio.create_subprocess_shell(
 48:         f"curl -sLo {file_path} {url}",
 49:         stdout=subprocess.DEVNULL,
 50:         stderr=subprocess.DEVNULL
 51:     )
 52:     await process.communicate()
 53: 
 54: async def download_files(file_list):
 55:     """Downloads multiple files asynchronously."""
 56:     tasks = []
 57:     for file_info in file_list:
 58:         parts = file_info.split(',')
 59:         url = parts[0].strip()
 60:         directory = parts[1].strip() if len(parts) > 1 else WEBUI   # Default Save Path
 61:         filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
 62:         tasks.append(_download_file(url, directory, filename))
 63:     await asyncio.gather(*tasks)
 64: 
 65: async def download_configuration():
 66:     """Downloads configuration files and clones extensions."""
 67:     ## FILES
 68:     url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
 69:     configs = [
 70:         # settings
 71:         f"{url_cfg}/{UI}/config.json",
 72:         f"{url_cfg}/{UI}/ui-config.json",
 73:         f"{url_cfg}/styles.csv",
 74:         f"{url_cfg}/user.css",
 75:         # other | UI
 76:         f"{url_cfg}/card-no-preview.png, {WEBUI}/html",
 77:         f"{url_cfg}/notification.mp3",
 78:         # other | tunneling
 79:         f"{url_cfg}/gradio-tunneling.py, {VENV}/lib/python3.10/site-packages/gradio_tunneling, main.py"  # Replace py-Script
 80:     ]
 81:     await download_files(configs)
 82: 
 83:     ## REPOS
 84:     extensions_list = [
 85:         ## ANXETY Edits
 86:         'https://github.com/anxety-solo/webui_timer timer',
 87:         'https://github.com/anxety-solo/anxety-theme',
 88:         'https://github.com/anxety-solo/sd-civitai-browser-plus Civitai-Browser-Plus',
 89: 
 90:         ## Gutris1
 91:         'https://github.com/gutris1/sd-image-viewer Image-Viewer',
 92:         'https://github.com/gutris1/sd-image-info Image-Info',
 93:         'https://github.com/gutris1/sd-hub SD-Hub',
 94: 
 95:         ## OTHER | ON
 96:         'https://github.com/Bing-su/adetailer',
 97: 
 98:         ## NEW Extensions
 99:         'https://github.com/Haoming02/sd-webui-mosaic-outpaint',
100:         'https://github.com/continue-revolution/sd-webui-segment-anything',
101:         'https://github.com/kainatquaderee/sd-webui-reactor-Nsfw_freedom',
102:         'https://github.com/a2569875/lora-prompt-tool',
103:         'https://github.com/Uminosachi/sd-webui-inpaint-anything',
104:         'https://github.com/redmercy69/sd-webui-stripper',
105:         'https://github.com/diffus-me/sd-webui-facefusion',
106:         'https://github.com/glucauze/sd-webui-faceswaplab',
107:         'https://github.com/IntellectzProductions/sd-webui-faceswap',
108:         'https://github.com/yownas/sd-webui-faceswapper',
109:         'https://github.com/leeguandong/sd_webui_outpainting',
110:         'https://github.com/thoraxe69/sd-webui-roop',
111: 
112:         ## OTHER | OFF
113:         # 'https://github.com/thomasasfk/sd-webui-aspect-ratio-helper Aspect-Ratio-Helper',
114:         # 'https://github.com/zanllp/sd-webui-infinite-image-Browse Infinite-Image-Browse',
115:         # 'https://github.com/Haoming02/sd-forge-couple SD-Couple',
116:         # 'https://github.com/ilian6806/stable-diffusion-webui-state State',
117:         # 'https://github.com/hako-mikan/sd-webui-supermerger Supermerger',
118:         # 'https://github.com/DominikDoom/a1111-sd-webui-tagcomplete TagComplete',
119:         # 'https://github.com/Tsukreya/Umi-AI-Wildcards',
120:         # 'https://github.com/picobyte/stable-diffusion-webui-wd14-tagger wd14-tagger'
121:     ]
122:     if ENV_NAME == 'Kaggle':
123:         extensions_list.append('https://github.com/gutris1/sd-encrypt-image Encrypt-Image')
124: 
125:     os.makedirs(EXTS, exist_ok=True)
126:     CD(EXTS)
127: 
128:     tasks = []
129:     for command in extensions_list:
130:         tasks.append(asyncio.create_subprocess_shell(
131:             f"git clone --depth 1 {command}",
132:             stdout=subprocess.DEVNULL, # Keep stdout for errors
133:             stderr=subprocess.DEVNULL  # Keep stderr for errors
134:         ))
135: 
136:     await asyncio.gather(*tasks)
137: 
138: def unpack_webui():
139:     """Unpacks the WebUI zip file and cleans up model-related directories."""
140:     zip_path = f"{HOME}/{UI}.zip"
141:     m_download(f"{REPO_URL} {HOME} {UI}.zip")
142:     # ipySys(f"unzip -q -o {zip_path} -d {WEBUI}") # REMOVED -q for verbose output
143:     ipySys(f"unzip -o {zip_path} -d {WEBUI}") # Show unzip output
144:     ipySys(f"rm -rf {zip_path}")
145:     
146:     # --- START OF MODIFICATION ---
147:     # Define model-related directories that should NOT be in the WebUI folder
148:     # as they are handled by the shared model base.
149:     model_dirs_to_clean = [
150:         WEBUI / 'models',
151:         WEBUI / 'VAE',
152:         WEBUI / 'Lora',
153:         WEBUI / 'embeddings',
154:         WEBUI / 'ControlNet',
155:         # Add any other subdirectories that might contain large model files
156:         # but are not needed within the UI's specific folder.
157:     ]
158: 
159:     print(f"🧹 Cleaning up unzipped model-related directories within {UI}...")
160:     for d in model_dirs_to_clean:
161:         if d.exists() and d.is_dir():
162:             print(f"   Deleting: {d}")
163:             try:
164:                 shutil.rmtree(d)
165:             except OSError as e:
166:                 print(f"   Error deleting {d}: {e}")
167:     # --- END OF MODIFICATION ---
168: 
169: ## ====================== MAIN CODE ======================
170: if __name__ == '__main__':
171:     # with capture.capture_output(): # REMOVED: To show verbose output
172:     unpack_webui()
173:     asyncio.run(download_configuration())
```

## File: scripts/UIs/ReForge.py
```python
  1: # ~ ReForge.py | by ANXETY ~
  2: 
  3: from Manager import m_download, m_clone    # Every Download | Clone
  4: import json_utils as js                    # JSON
  5: 
  6: from IPython.display import clear_output
  7: from IPython.utils import capture
  8: from IPython import get_ipython
  9: from pathlib import Path
 10: import subprocess
 11: import asyncio
 12: import os
 13: import shutil # Import shutil for rmtree
 14: 
 15: 
 16: CD = os.chdir
 17: ipySys = get_ipython().system
 18: 
 19: # Constants
 20: UI = 'ReForge'
 21: 
 22: HOME = Path.home()
 23: WEBUI = HOME / UI
 24: VENV = HOME / 'venv'
 25: SCR_PATH = HOME / 'ANXETY'
 26: SETTINGS_PATH = SCR_PATH / 'settings.json'
 27: 
 28: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
 29: 
 30: REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
 31: FORK_REPO = js.read(SETTINGS_PATH, 'ENVIRONMENT.fork')
 32: BRANCH = js.read(SETTINGS_PATH, 'ENVIRONMENT.branch')
 33: EXTS = js.read(SETTINGS_PATH, 'WEBUI.extension_dir')
 34: 
 35: CD(HOME)
 36: 
 37: 
 38: ## ================== WEB UI OPERATIONS ==================
 39: 
 40: async def _download_file(url, directory, filename):
 41:     """Downloads a single file."""
 42:     os.makedirs(directory, exist_ok=True)
 43:     file_path = os.path.join(directory, filename)
 44: 
 45:     if os.path.exists(file_path):
 46:         os.remove(file_path)
 47: 
 48:     process = await asyncio.create_subprocess_shell(
 49:         f"curl -sLo {file_path} {url}",
 50:         stdout=subprocess.DEVNULL,
 51:         stderr=subprocess.DEVNULL
 52:     )
 53:     await process.communicate()
 54: 
 55: async def download_files(file_list):
 56:     """Downloads multiple files asynchronously."""
 57:     tasks = []
 58:     for file_info in file_list:
 59:         parts = file_info.split(',')
 60:         url = parts[0].strip()
 61:         directory = parts[1].strip() if len(parts) > 1 else WEBUI   # Default Save Path
 62:         filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
 63:         tasks.append(_download_file(url, directory, filename))
 64:     await asyncio.gather(*tasks)
 65: 
 66: async def download_configuration():
 67:     """Downloads configuration files and clones extensions."""
 68:     ## FILES
 69:     url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
 70:     configs = [
 71:         # settings
 72:         f"{url_cfg}/{UI}/config.json",
 73:         f"{url_cfg}/{UI}/ui-config.json",
 74:         f"{url_cfg}/styles.csv",
 75:         f"{url_cfg}/user.css",
 76:         # other | UI
 77:         f"{url_cfg}/card-no-preview.png, {WEBUI}/html",
 78:         f"{url_cfg}/notification.mp3",
 79:         # other | tunneling
 80:         f"{url_cfg}/gradio-tunneling.py, {VENV}/lib/python3.10/site-packages/gradio_tunneling, main.py"  # Replace py-Script
 81:     ]
 82:     await download_files(configs)
 83: 
 84:     ## REPOS
 85:     extensions_list = [
 86:         ## ANXETY Edits
 87:         'https://github.com/anxety-solo/webui_timer timer',
 88:         'https://github.com/anxety-solo/anxety-theme',
 89:         'https://github.com/anxety-solo/sd-civitai-browser-plus Civitai-Browser-Plus',
 90: 
 91:         ## Gutris1
 92:         'https://github.com/gutris1/sd-image-viewer Image-Viewer',
 93:         'https://github.com/gutris1/sd-image-info Image-Info',
 94:         'https://github.com/gutris1/sd-hub SD-Hub',
 95: 
 96:         ## OTHER | ON
 97:         'https://github.com/Bing-su/adetailer',
 98: 
 99:         ## NEW Extensions
100:         'https://github.com/Haoming02/sd-webui-mosaic-outpaint',
101:         'https://github.com/continue-revolution/sd-webui-segment-anything',
102:         'https://github.com/kainatquaderee/sd-webui-reactor-Nsfw_freedom',
103:         'https://github.com/a2569875/lora-prompt-tool',
104:         'https://github.com/Uminosachi/sd-webui-inpaint-anything',
105:         'https://github.com/redmercy69/sd-webui-stripper',
106:         'https://github.com/diffus-me/sd-webui-facefusion',
107:         'https://github.com/glucauze/sd-webui-faceswaplab',
108:         'https://github.com/IntellectzProductions/sd-webui-faceswap',
109:         'https://github.com/yownas/sd-webui-faceswapper',
110:         'https://github.com/leeguandong/sd_webui_outpainting',
111:         'https://github.com/thoraxe69/sd-webui-roop',
112: 
113:         ## OTHER | OFF
114:         # 'https://github.com/thomasasfk/sd-webui-aspect-ratio-helper Aspect-Ratio-Helper',
115:         # 'https://github.com/zanllp/sd-webui-infinite-image-browsing Infinite-Image-Browsing',
116:         # 'https://github.com/hako-mikan/sd-webui-regional-prompter Regional-Prompter',
117:         # 'https://github.com/ilian6806/stable-diffusion-webui-state State',
118:         # 'https://github.com/hako-mikan/sd-webui-supermerger Supermerger',
119:         # 'https://github.com/DominikDoom/a1111-sd-webui-tagcomplete TagComplete',
120:         # 'https://github.com/Tsukreya/Umi-AI-Wildcards',
121:         # 'https://github.com/picobyte/stable-diffusion-webui-wd14-tagger wd14-tagger'
122:     ]
123:     if ENV_NAME == 'Kaggle':
124:         extensions_list.append('https://github.com/gutris1/sd-encrypt-image Encrypt-Image')
125: 
126:     os.makedirs(EXTS, exist_ok=True)
127:     CD(EXTS)
128: 
129:     tasks = []
130:     for command in extensions_list:
131:         tasks.append(asyncio.create_subprocess_shell(
132:             f"git clone --depth 1 {command}",
133:             stdout=subprocess.DEVNULL,
134:             stderr=subprocess.DEVNULL
135:         ))
136: 
137:     await asyncio.gather(*tasks)
138: 
139: def unpack_webui():
140:     """Unpacks the WebUI zip file and cleans up model-related directories."""
141:     zip_path = f"{HOME}/{UI}.zip"
142:     m_download(f"{REPO_URL} {HOME} {UI}.zip")
143:     ipySys(f"unzip -q -o {zip_path} -d {WEBUI}")
144:     ipySys(f"rm -rf {zip_path}")
145:     
146:     # --- START OF MODIFICATION ---
147:     # Define model-related directories that should NOT be in the WebUI folder
148:     # as they are handled by the shared model base.
149:     model_dirs_to_clean = [
150:         WEBUI / 'models',
151:         WEBUI / 'VAE',
152:         WEBUI / 'Lora',
153:         WEBUI / 'embeddings',
154:         WEBUI / 'ControlNet',
155:         # Add any other subdirectories that might contain large model files
156:         # but are not needed within the UI's specific folder.
157:     ]
158: 
159:     print(f"🧹 Cleaning up unzipped model-related directories within {UI}...")
160:     for d in model_dirs_to_clean:
161:         if d.exists() and d.is_dir():
162:             print(f"   Deleting: {d}")
163:             try:
164:                 shutil.rmtree(d)
165:             except OSError as e:
166:                 print(f"   Error deleting {d}: {e}")
167:     # --- END OF MODIFICATION ---
168: 
169: ## ====================== MAIN CODE ======================
170: if __name__ == '__main__':
171:     with capture.capture_output():
172:         unpack_webui()
173:         asyncio.run(download_configuration())
```

## File: scripts/UIs/SD-UX.py
```python
  1: # ~ SD-UX.py | by ANXETY ~
  2: 
  3: from Manager import m_download, m_clone    # Every Download | Clone
  4: import json_utils as js                    # JSON
  5: 
  6: from IPython.display import clear_output
  7: from IPython.utils import capture
  8: from IPython import get_ipython
  9: from pathlib import Path
 10: import subprocess
 11: import asyncio
 12: import os
 13: import shutil # Import shutil for rmtree
 14: 
 15: CD = os.chdir
 16: ipySys = get_ipython().system
 17: 
 18: # Constants
 19: UI = 'SD-UX'
 20: 
 21: HOME = Path.home()
 22: WEBUI = HOME / UI
 23: VENV = HOME / 'venv'
 24: SCR_PATH = HOME / 'ANXETY'
 25: SETTINGS_PATH = SCR_PATH / 'settings.json'
 26: 
 27: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
 28: 
 29: REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
 30: FORK_REPO = js.read(SETTINGS_PATH, 'ENVIRONMENT.fork')
 31: BRANCH = js.read(SETTINGS_PATH, 'ENVIRONMENT.branch')
 32: EXTS = js.read(SETTINGS_PATH, 'WEBUI.extension_dir')
 33: 
 34: CD(HOME)
 35: 
 36: 
 37: ## ================== WEB UI OPERATIONS ==================
 38: 
 39: async def _download_file(url, directory, filename):
 40:     """Downloads a single file."""
 41:     os.makedirs(directory, exist_ok=True)
 42:     file_path = os.path.join(directory, filename)
 43: 
 44:     if os.path.exists(file_path):
 45:         os.remove(file_path)
 46: 
 47:     process = await asyncio.create_subprocess_shell(
 48:         f"curl -sLo {file_path} {url}",
 49:         stdout=subprocess.DEVNULL,
 50:         stderr=subprocess.DEVNULL
 51:     )
 52:     await process.communicate()
 53: 
 54: async def download_files(file_list):
 55:     """Downloads multiple files asynchronously."""
 56:     tasks = []
 57:     for file_info in file_list:
 58:         parts = file_info.split(',')
 59:         url = parts[0].strip()
 60:         directory = parts[1].strip() if len(parts) > 1 else WEBUI   # Default Save Path
 61:         filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
 62:         tasks.append(_download_file(url, directory, filename))
 63:     await asyncio.gather(*tasks)
 64: 
 65: async def download_configuration():
 66:     """Downloads configuration files and clones extensions."""
 67:     ## FILES
 68:     url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
 69:     configs = [
 70:         # settings
 71:         f"{url_cfg}/{UI}/config.json",
 72:         f"{url_cfg}/{UI}/ui-config.json",
 73:         f"{url_cfg}/styles.csv",
 74:         f"{url_cfg}/user.css",
 75:         # other | UI
 76:         f"{url_cfg}/card-no-preview.png, {WEBUI}/html",
 77:         f"{url_cfg}/notification.mp3",
 78:         # other | tunneling
 79:         f"{url_cfg}/gradio-tunneling.py, {VENV}/lib/python3.10/site-packages/gradio_tunneling, main.py"  # Replace py-Script
 80:     ]
 81:     await download_files(configs)
 82: 
 83:     ## REPOS
 84:     extensions_list = [
 85:         ## ANXETY Edits
 86:         'https://github.com/anxety-solo/webui_timer timer',
 87:         'https://github.com/anxety-solo/anxety-theme-ux',
 88:         'https://github.com/anxety-solo/sd-civitai-browser-plus Civitai-Browser-Plus',
 89: 
 90:         ## Gutris1
 91:         'https://github.com/gutris1/sd-image-viewer Image-Viewer',
 92:         'https://github.com/gutris1/sd-image-info Image-Info',
 93:         'https://github.com/gutris1/sd-hub SD-Hub',
 94: 
 95:         ## OTHER | ON
 96:         'https://github.com/Bing-su/adetailer',
 97: 
 98:         ## NEW Extensions
 99:         'https://github.com/Haoming02/sd-webui-mosaic-outpaint',
100:         'https://github.com/continue-revolution/sd-webui-segment-anything',
101:         'https://github.com/kainatquaderee/sd-webui-reactor-Nsfw_freedom',
102:         'https://github.com/a2569875/lora-prompt-tool',
103:         'https://github.com/Uminosachi/sd-webui-inpaint-anything',
104:         'https://github.com/redmercy69/sd-webui-stripper',
105:         'https://github.com/diffus-me/sd-webui-facefusion',
106:         'https://github.com/glucauze/sd-webui-faceswaplab',
107:         'https://github.com/IntellectzProductions/sd-webui-faceswap',
108:         'https://github.com/yownas/sd-webui-faceswapper',
109:         'https://github.com/leeguandong/sd_webui_outpainting',
110:         'https://github.com/thoraxe69/sd-webui-roop',
111: 
112:         ## OTHER | OFF
113:         # 'https://github.com/thomasasfk/sd-webui-aspect-ratio-helper Aspect-Ratio-Helper',
114:         # 'https://github.com/Mikubill/sd-webui-controlnet ControlNet',
115:         # 'https://github.com/zanllp/sd-webui-infinite-image-browsing Infinite-Image-Browsing',
116:         # 'https://github.com/hako-mikan/sd-webui-regional-prompter Regional-Prompter',
117:         # 'https://github.com/ilian6806/stable-diffusion-webui-state State',
118:         # 'https://github.com/hako-mikan/sd-webui-supermerger Supermerger',
119:         # 'https://github.com/DominikDoom/a1111-sd-webui-tagcomplete TagComplete',
120:         # 'https://github.com/Tsukreya/Umi-AI-Wildcards',
121:         # 'https://github.com/picobyte/stable-diffusion-webui-wd14-tagger wd14-tagger'
122:     ]
123:     if ENV_NAME == 'Kaggle':
124:         extensions_list.append('https://github.com/gutris1/sd-encrypt-image Encrypt-Image')
125: 
126:     os.makedirs(EXTS, exist_ok=True)
127:     CD(EXTS)
128: 
129:     tasks = []
130:     for command in extensions_list:
131:         tasks.append(asyncio.create_subprocess_shell(
132:             f"git clone --depth 1 {command}",
133:             stdout=subprocess.DEVNULL,
134:             stderr=subprocess.DEVNULL
135:         ))
136: 
137:     await asyncio.gather(*tasks)
138: 
139: def unpack_webui():
140:     """Unpacks the WebUI zip file and cleans up model-related directories."""
141:     zip_path = f"{HOME}/{UI}.zip"
142:     m_download(f"{REPO_URL} {HOME} {UI}.zip")
143:     ipySys(f"unzip -q -o {zip_path} -d {WEBUI}")
144:     ipySys(f"rm -rf {zip_path}")
145:     
146:     # --- START OF MODIFICATION ---
147:     # Define model-related directories that should NOT be in the WebUI folder
148:     # as they are handled by the shared model base.
149:     model_dirs_to_clean = [
150:         WEBUI / 'models',
151:         WEBUI / 'VAE',
152:         WEBUI / 'Lora',
153:         WEBUI / 'embeddings',
154:         WEBUI / 'ControlNet',
155:         # Add any other subdirectories that might contain large model files
156:         # but are not needed within the UI's specific folder.
157:     ]
158: 
159:     print(f"🧹 Cleaning up unzipped model-related directories within {UI}...")
160:     for d in model_dirs_to_clean:
161:         if d.exists() and d.is_dir():
162:             print(f"   Deleting: {d}")
163:             try:
164:                 shutil.rmtree(d)
165:             except OSError as e:
166:                 print(f"   Error deleting {d}: {e}")
167:     # --- END OF MODIFICATION ---
168: 
169: ## ====================== MAIN CODE ======================
170: if __name__ == '__main__':
171:     with capture.capture_output():
172:         unpack_webui()
173:         asyncio.run(download_configuration())
```

## File: scripts/_loras-data.py
```python
 1: # CORRECTED LORA DATA SCRIPT
 2: 
 3: lora_data = {
 4:     "sd15_loras": {
 5:         "female masturbation concepts - v2-LyCORIS-LoCon": [{"url": "https://civitai.com/api/download/models/50851", "name": "concept-female_masturbation-v2.safetensors"}],
 6:         "brothaman": [{"url": "https://huggingface.co/maximstar00/cute_pussy/resolve/main/brothaman.safetensors", "name": "brothaman.safetensors"}],
 7:         "Female masturbation - mastv1": [{"url": "https://civitai.com/api/download/models/44430", "name": "mastv1.safetensors"}],
 8:         "POV yuri cunnilingus - v1": [{"url": "https://civitai.com/api/download/models/58906", "name": "qqq-cunnilingus_pov-v1.safetensors"}],
 9:         "Cute Pussy  - v2.0": [{"url": "https://civitai.com/api/download/models/112806", "name": "CutePussyVer2S.safetensors"}],
10:         "PornMaster-\u81ea\u62cd\u3001\u7a7f\u8863\u670d\u81ea\u6170\u3001\u88f8\u4f53\u81ea\u6170\u3001\u900f\u89c6\u3001\u9ad8\u6f6e\u8138& Selfie\u3001clothed masturbation\u3001naked masturbation\u3001see-through \u3001orgasm - V2-LYCORIS": [{"url": "https://civitai.com/api/download/models/344345", "name": "clothed masturbation_V2.safetensors"}],
11:         "Female masturbation - v0.5": [{"url": "https://civitai.com/api/download/models/174016", "name": "female_masturbation_v0.5.safetensors"}],
12:         "Female Masturbation [Boob Fondling and Fingering] - v1": [{"url": "https://civitai.com/api/download/models/20546", "name": "masturbation-v1.safetensors"}],
13:         "PornMaster-Pro \u8272\u60c5\u5927\u5e08 - FULL-V4-inpainting - FULL-V4-inpainting": [{"url": "https://civitai.com/api/download/models/102709", "name": "pornmasterProFULLV4_fullV4-inpainting.safetensors"}],
14:         "Hands Down Clothes - v1.0": [{"url": "https://civitai.com/api/download/models/144437", "name": "hand-down-clothes.safetensors"}],
15:         "yuri cunnilingus - lora - v1.0": [{"url": "https://civitai.com/api/download/models/283261", "name": "yuri_cunnilingus_v1.safetensors"}],
16:         "Sexy Catholic school uniform |anime+realistic| - v1.0": [{"url": "https://civitai.com/api/download/models/110260", "name": "CatholicSchoolUniformDogu.safetensors"}],
17:         "Hand in panties - v0.82": [{"url": "https://civitai.com/api/download/models/170310", "name": "hand_in_panties_v0.82.safetensors"}],
18:         "ppussy": [{"url": "https://huggingface.co/Remphanstar/Rojos/resolve/main/ppussy.safetensors", "name": "ppussy.safetensors"}],
19:         "Sexy School Uniform | olaz - v1": [{"url": "https://civitai.com/api/download/models/169692", "name": "sexyschooluniformv1.safetensors"}],
20:         "Labiaplasty (Innie Pussy Adjuster) [SD1.5 + SDXL] - v2.0": [{"url": "https://civitai.com/api/download/models/167994", "name": "m99_labiaplasty_pussy_2.safetensors"}],
21:         "School Dress Collection By Stable Yogi - SF_School_Dress": [{"url": "https://civitai.com/api/download/models/332880", "name": "SF_School_Dress_By_Stable_Yogi.safetensors"}],
22:         "Panties pulled aside fuck | Sex Lora 011 | Perfect - v1.0": [{"url": "https://civitai.com/api/download/models/63998", "name": "panties_pulled_aside_fuck.v1.0.safetensors"}],
23:         "yuri cunnilingus - v4": [{"url": "https://civitai.com/api/download/models/58951", "name": "qqq-yuri-cunnilingus-v4.safetensors"}],
24:         "Panties to side LoRA - v2": [{"url": "https://civitai.com/api/download/models/45127", "name": "PantiesToSide-v2.safetensors"}],
25:     },
26:     "sdxl_loras": {
27:         "BT Lowering Pants - Pony v1": [{"url": "https://civitai.com/api/download/models/393888", "name": "BT_Lowering_Pants_Pony.safetensors"}],
28:         "Lesbian fingering - v1.0": [{"url": "https://civitai.com/api/download/models/1030934", "name": "Lesbian_fingering.safetensors"}],
29:         "Yuri Mutual Masturbation - v1.0-XL": [{"url": "https://civitai.com/api/download/models/567342", "name": "Yuri Mutual Masturbation.safetensors"}],
30:         "Real Pussy - Cameltoe - v3 XL": [{"url": "https://civitai.com/api/download/models/802232", "name": "Pussy_Cameltoe_v3_XL.safetensors"}],
31:         "Striped Micro Lingerie PONY XL - v2.0": [{"url": "https://civitai.com/api/download/models/518802", "name": "hud_str_ling_v2_XLP.safetensors"}],
32:         "Nudify XL: Better Bodies - v1 Lite": [{"url": "https://civitai.com/api/download/models/177674", "name": "nudify_xl_lite.safetensors"}],
33:         "Fingering Under Clothes/Implied Masturbation | Concept LoRA | SDXL Pony - V1": [{"url": "https://civitai.com/api/download/models/427792", "name": "Lunas-Implied-Fingering-SDXL-A1.safetensors"}],
34:         "NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Available) - v1.0 (Full - Recommended)": [{"url": "https://civitai.com/api/download/models/160240", "name": "NsfwPovAllInOneLoraSdxl-000009.safetensors"}],
35:         "Masturbating Under Panties - v1.0-Pony": [{"url": "https://civitai.com/api/download/models/624818", "name": "MASTURBATING UNDER PANTIES.safetensors"}],
36:         "Multiple XL Sliders - Age, weight, Hands, etc - age_pony": [{"url": "https://civitai.com/api/download/models/686514", "name": "agepony8.pt"}],
37:         "\u30af\u30ed\u30c3\u30c1\u305a\u3089\u3057/panties aside(XL,Pony) - v2.0 pony": [{"url": "https://civitai.com/api/download/models/1567868", "name": "panty aside_pony_V2.0.safetensors"}],
38:         "School Swimsuit and Kneehighs / \u30b9\u30af\u6c34\u30cb\u30fc\u30bd - XLv1.0": [{"url": "https://civitai.com/api/download/models/478142", "name": "school swimsuit kneehigh XL-v1.safetensors"}],
39:         "LEAKCORE (LEAKED NUDES STYLE, Realism, Amateur) - v1.0 (LUSTIFY)": [{"url": "https://civitai.com/api/download/models/1627770", "name": "leaked_nudes_style_v1_fixed.safetensors"}],
40:         "Pony Amateur \u2728 - Standard (V2)": [{"url": "https://civitai.com/api/download/models/717403", "name": "zy_AmateurStyle_v2.safetensors"}],
41:         "Lesbian pussy licking - v1.0": [{"url": "https://civitai.com/api/download/models/859154", "name": "Lesbian_pussy_licking.safetensors"}],
42:         "Real Pussy - Peach - Rear v2 XL": [{"url": "https://civitai.com/api/download/models/1604857", "name": "Pussy_Peach_Rear_v2_XL.safetensors"}],
43:     }
44: }
```

## File: scripts/_models-data.py
```python
 1: # SD 1.5 MODELS
 2: sd15_model_data = {
 3:     "D5K6.0": {"url": "https://huggingface.co/Remphanstar/Rojos/resolve/main/D5K6.0.safetensors?download=true", "name": "D5K6.0.safetensors"},
 4:     "Merged amateurs - Mixed Amateurs": {"url": "https://civitai.com/api/download/models/179318", "name": "mergedAmateurs_mixedAmateurs.safetensors"},
 5:     "PornMaster-Pro \u8272\u60c5\u5927\u5e08 - V10.1-VAE-inpainting - V10.1-VAE-inpainting": {"url": "https://civitai.com/api/download/models/937781", "name": "pornmasterProV101VAE_v101VAE-inpainting.safetensors"},
 6:     "Merged Amateurs - Mixed Amateurs | Inpainting Model - v1.0": {"url": "https://civitai.com/api/download/models/188884", "name": "mergedAmateursMixed_v10-inpainting.safetensors"},
 7:     "epiCRealism pureEvolution InPainting - v1.0": {"url": "https://civitai.com/api/download/models/95864", "name": "epicrealism_v10-inpainting.safetensors"},
 8:     "fuego_v2_tkl4_fp26(1)": {"url": "https://huggingface.co/Remphanstar/Rojos/resolve/main/fuego_v2_tkl4_fp26(1).safetensors", "name": "fuego_v2_tkl4_fp26(1).safetensors"},
 9:     "PornMaster-Pro \u8272\u60c5\u5927\u5e08 - FULL-V4-inpainting - FULL-V4-inpainting": {"url": "https://civitai.com/api/download/models/102709", "name": "pornmasterProFULLV4_fullV4-inpainting.safetensors"},
10:     "LazyMix+ (Real Amateur Nudes) - v4.0": {"url": "https://civitai.com/models/10961/lazymix-real-amateur-nudes", "name": "lazymixRealAmateur_v40.safetensors"},
11:     "PornMaster-Pro \u8272\u60c5\u5927\u5e08 - FULL-V5-inpainting - FULL-V5-inpainting": {"url": "https://civitai.com/api/download/models/176934", "name": "pornmasterProFULLV5_fullV5-inpainting.safetensors"},
12:     "SD.15-AcornMoarMindBreak": {"url": "https://huggingface.co/Remphanstar/Rojos/resolve/main/SD.15-AcornMoarMindBreak.safetensors", "name": "SD.15-AcornMoarMindBreak.safetensors"},
13: }
14: 
15: # SD 1.5 VAES
16: sd15_vae_data = {
17:     "vae-ft-mse-840000-ema-pruned | 840000 | 840k SD1.5 VAE - vae-ft-mse-840k": {"url": "https://civitai.com/api/download/models/311162", "name": "vaeFtMse840000EmaPruned_vaeFtMse840k.safetensors"},
18:     "ClearVAE(SD1.5) - v2.3": {"url": "https://civitai.com/api/download/models/88156", "name": "clearvaeSD15_v23.safetensors"},
19: }
20: 
21: 
22: ## CONTROLNET
23: 
24: controlnet_list = {
25:     "1. Openpose": [
26:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors"},
27:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_openpose_fp16.yaml"}
28:     ],
29:     "2. Canny": [
30:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors"},
31:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_canny_fp16.yaml"}
32:     ],
33:     "3. Depth": [
34:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors"},
35:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1p_sd15_depth_fp16.yaml"}
36:     ],
37:     "4. Lineart": [
38:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors"},
39:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_lineart_fp16.yaml"},
40:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors"},
41:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15s2_lineart_anime_fp16.yaml"}
42:     ],
43:     "5. ip2p": [
44:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors"},
45:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_ip2p_fp16.yaml"}
46:     ],
47:     "6. Shuffle": [
48:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors"},
49:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_shuffle_fp16.yaml"}
50:     ],
51:     "7. Inpaint": [
52:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors"},
53:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_inpaint_fp16.yaml"}
54:     ],
55:     "8. MLSD": [
56:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors"},
57:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_mlsd_fp16.yaml"}
58:     ],
59:     "9. Normalbae": [
60:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors"},
61:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_normalbae_fp16.yaml"}
62:     ],
63:     "10. Scribble": [
64:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble_fp16.safetensors"},
65:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_scribble_fp16.yaml"}
66:     ],
67:     "11. Seg": [
68:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg_fp16.safetensors"},
69:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_seg_fp16.yaml"}
70:     ],
71:     "12. Softedge": [
72:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge_fp16.safetensors"},
73:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_softedge_fp16.yaml"}
74:     ],
75:     "13. Tile": [
76:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile_fp16.safetensors"},
77:         {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1e_sd15_tile_fp16.yaml"}
78:     ]
79: }
```

## File: scripts/_xl-models-data.py
```python
 1: # SDXL MODELS
 2: sdxl_models_data = {
 3:     "uberRealisticPornMerge-xlV6Final-inpainting   BEST SO FAR!!! - PonyXL-Hybrid v1": {"url": "https://civitai.com/api/download/models/1024962", "name": "uberrealisticpornmerge_ponyxlHybridV1.safetensors"},
 4:     "lustifySDXLNSFW_oltINPAINTING": {"url": "https://huggingface.co/RandomGulag/lustifySDXLNSFW_oltINPAINTING/resolve/main/lustifySDXLNSFW_oltINPAINTING.safetensors", "name": "lustifySDXLNSFW_oltINPAINTING.safetensors"},
 5:     "PornMaster-Pro \u8272\u60c5\u5927\u5e08 - SDXL - SDXL-V2-VAE": {"url": "https://civitai.com/api/download/models/1167499", "name": "pornmasterProSDXL_sdxlV2VAE.safetensors"},
 6:     "True Amateur Feeling XL - v2": {"url": "https://civitai.com/api/download/models/907265", "name": "trueAmateurFeelingXL_v2.safetensors"},
 7:     "Sippy": {"url": "https://huggingface.co/Red1618/Zhu/resolve/main/Sippy.safetensors?download=true", "name": "Sippy.safetensors"},
 8:     "SDXL-DWXL": {"url": "https://huggingface.co/Remphanstar/Rojos/resolve/main/SDXL-DWXL.fp16.safetensors", "name": "SDXL-DWXL.fp16.safetensors"},
 9:     "PornMaster-\u8272\u60c5\u5927\u5e08 - V7-FP16-VAE": {"url": "https://civitai.com/api/download/models/938228", "name": "pornmaster_v7FP16VAE.safetensors"},
10: }
11: 
12: # SDXL VAES
13: sdxl_vae_data = {
14:     "Pony Standard VAE - V1.0": {"url": "https://civitai.com/api/download/models/785437", "name": "ponyStandardVAE_v10.safetensors"},
15:     "FIX FP16 Errors SDXL - Lower Memory use! --- sdxl-vae-fp16-fix by madebyollin - v1.0": {"url": "https://civitai.com/api/download/models/155933", "name": "fixFP16ErrorsSDXLLowerMemoryUse_v10.safetensors"},
16:     "SDXL VAE - SDXL-VAE": {"url": "https://civitai.com/api/download/models/333245", "name": "sdxlVAE_sdxlVAE.safetensors"},
17: }
18: 
19: ## CONTROLNET
20: 
21: controlnet_list = {
22:     "1. Kohya Controllite XL Blur": [
23:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_blur.safetensors"},
24:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_blur_anime.safetensors"}
25:     ],
26:     "2. Kohya Controllite XL Canny": [
27:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_canny.safetensors"},
28:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_canny_anime.safetensors"}
29:     ],
30:     "3. Kohya Controllite XL Depth": [
31:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_depth.safetensors"},
32:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_depth_anime.safetensors"}
33:     ],
34:     "4. Kohya Controllite XL Openpose Anime": [
35:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_openpose_anime.safetensors"},
36:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_openpose_anime_v2.safetensors"}
37:     ],
38:     "5. Kohya Controllite XL Scribble Anime": [
39:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_scribble_anime.safetensors"}
40:     ],
41:     "6. T2I Adapter XL Canny": [
42:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_canny.safetensors"}
43:     ],
44:     "7. T2I Adapter XL Openpose": [
45:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_openpose.safetensors"}
46:     ],
47:     "8. T2I Adapter XL Sketch": [
48:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_sketch.safetensors"}
49:     ],
50:     "9. T2I Adapter Diffusers XL Canny": [
51:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_canny.safetensors"}
52:     ],
53:     "10. T2I Adapter Diffusers XL Depth Midas": [
54:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_depth_midas.safetensors"}
55:     ],
56:     "11. T2I Adapter Diffusers XL Depth Zoe": [
57:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_depth_zoe.safetensors"}
58:     ],
59:     "12. T2I Adapter Diffusers XL Lineart": [
60:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_lineart.safetensors"}
61:     ],
62:     "13. T2I Adapter Diffusers XL Openpose": [
63:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_openpose.safetensors"}
64:     ],
65:     "14. T2I Adapter Diffusers XL Sketch": [
66:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_sketch.safetensors"}
67:     ],
68:     "15. IP Adapter SDXL": [
69:         {'url': "https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter_sdxl.safetensors"}
70:     ],
71:     "16. IP Adapter SDXL VIT-H": [
72:         {'url': "https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter_sdxl_vit-h.safetensors"}
73:     ],
74:     "17. Diffusers XL Canny Mid": [
75:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/diffusers_xl_canny_mid.safetensors"}
76:     ],
77:     "18. Diffusers XL Depth Mid": [
78:         {'url': "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/diffusers_xl_depth_mid.safetensors"}
79:     ],
80:     "19. Controlnet Union SDXL 1.0": [
81:         {'url': "https://huggingface.co/xinsir/controlnet-union-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors", 'name': "controlnet-union-sdxl-1.0.safetensors"}
82:     ],
83:     "20. Controlnet Union SDXL Pro Max": [
84:         {'url': "https://huggingface.co/xinsir/controlnet-union-sdxl-1.0/resolve/main/diffusion_pytorch_model_promax.safetensors", 'name': "controlnet-union-sdxl-promax.safetensors"}
85:     ]
86: }
```

## File: scripts/auto-cleaner.py
```python
  1: # ~ auto-cleaner.py | by ANXETY ~
  2: 
  3: from widget_factory import WidgetFactory    # WIDGETS
  4: import json_utils as js                     # JSON
  5: 
  6: from IPython.display import display, HTML, clear_output
  7: import ipywidgets as widgets
  8: from pathlib import Path
  9: import psutil
 10: import json
 11: import time
 12: import os
 13: import shutil # Added for comprehensive deletion
 14: 
 15: # Constants
 16: HOME = Path.home()
 17: SCR_PATH = HOME / 'ANXETY'
 18: SETTINGS_PATH = SCR_PATH / 'settings.json'
 19: 
 20: CSS = SCR_PATH / 'CSS'
 21: cleaner_css = CSS / 'auto-cleaner.css'
 22: 
 23: 
 24: ## ================ loading settings V5 ==================
 25: 
 26: def load_settings(path):
 27:     """Load settings from a JSON file."""
 28:     try:
 29:         return {
 30:             **js.read(path, 'ENVIRONMENT'),
 31:             **js.read(path, 'WIDGETS'),
 32:             **js.read(path, 'WEBUI')
 33:         }
 34:     except (json.JSONDecodeError, IOError) as e:
 35:         print(f"Error loading settings: {e}")
 36:         return {}
 37: 
 38: # Load settings
 39: settings = load_settings(SETTINGS_PATH)
 40: locals().update(settings)
 41: 
 42: ## ================= AutoCleaner function ================
 43: 
 44: def _update_memory_info():
 45:     """Updates and displays current disk space information."""
 46:     disk_space = psutil.disk_usage(os.getcwd())
 47:     total = disk_space.total / (1024 ** 3)
 48:     used = disk_space.used / (1024 ** 3)
 49:     free = disk_space.free / (1024 ** 3)
 50: 
 51:     storage_info.value = f'''
 52:     <div class="storage_info">Total storage: {total:.2f} GB <span style="color: #555">|</span> Used: {used:.2f} GB <span style="color: #555">|</span> Free: {free:.2f} GB</div>
 53:     '''
 54: 
 55: def clean_directory(directory, directory_type):
 56:     """Cleans a specific directory by removing certain file types."""
 57:     trash_extensions = {'.txt', '.aria2', '.ipynb_checkpoints'}
 58:     image_extensions = {'.png', '.jpg', '.jpeg', '.gif'}
 59:     deleted_files = 0
 60: 
 61:     if not Path(directory).is_dir():
 62:         print(f"ℹ️ Directory '{directory}' does not exist. Skipping.")
 63:         return 0
 64: 
 65:     for root, dirs, files in os.walk(directory):
 66:         for file in files:
 67:             file_path = Path(root) / file
 68: 
 69:             # Skip protected files like .gitkeep or similar
 70:             if file_path.name == '.gitkeep':
 71:                 continue
 72: 
 73:             if directory_type == 'Models' and file.endswith(tuple(image_extensions)):
 74:                 try:
 75:                     file_path.unlink()
 76:                     deleted_files += 1
 77:                 except Exception as e:
 78:                     print(f"❌ Error deleting image {file_path}: {e}")
 79:                 continue
 80: 
 81:             if file.endswith(tuple(trash_extensions)) or ('.' in file and not file.endswith(('.safetensors', '.ckpt', '.pt', '.zip', '.json', '.yaml', '.csv', '.ini'))):
 82:                 try:
 83:                     file_path.unlink()
 84:                     deleted_files += 1
 85:                 except Exception as e:
 86:                     print(f"❌ Error deleting trash file {file_path}: {e}")
 87: 
 88:     return deleted_files
 89: 
 90: # --- START OF MODIFICATION ---
 91: # No longer using a global status variable or interactive confirmation
 92: def clean_all_except_notebook_and_main():
 93:     """Deletes all files and folders in the current working directory except the notebook and main.py."""
 94:     output.clear_output()
 95:     with output:
 96:         print("!!! Initiating COMPREHENSIVE DELETION !!!")
 97:         print("This will remove almost everything in your studio instance.")
 98:         print("This action is irreversible and requires a runtime restart for a clean state.")
 99:         print("\n--- Proceeding with deletion in 5 seconds... (Ctrl+C to abort) ---")
100:         time.sleep(5) # Give user a moment to react and Ctrl+C if needed
101: 
102:         HOME_PATH = Path.home() # Use Path.home() to target the studio root
103: 
104:         # Get the current notebook's filename reliably within the execution environment
105:         notebook_filename = None
106:         for fname in os.listdir(HOME_PATH):
107:             if fname.endswith('.ipynb') and 'LightningAnxiety' in fname: # Heuristic for your notebook name
108:                 notebook_filename = fname
109:                 break
110:         
111:         notebook_path = HOME_PATH / notebook_filename if notebook_filename else None
112:         main_py_path = HOME_PATH / "main.py"
113: 
114:         EXCLUDE_LIST = []
115:         if notebook_path and notebook_path.exists():
116:             EXCLUDE_LIST.append(notebook_path.resolve()) # Resolve to absolute path for consistent comparison
117:             print(f"ℹ️ Protecting notebook: {notebook_path.name}")
118:         if main_py_path.exists():
119:             EXCLUDE_LIST.append(main_py_path.resolve()) # Resolve to absolute path
120:             print(f"ℹ️ Protecting main.py: {main_py_path.name}")
121:         
122:         deleted_count = 0
123:         skipped_count = 0
124: 
125:         # Iterate through contents of HOME_PATH and delete
126:         print(f"\n--- Starting Comprehensive Deletion in {HOME_PATH} ---")
127:         for item in HOME_PATH.iterdir():
128:             # Convert item to absolute path for consistent comparison with EXCLUDE_LIST
129:             abs_item = item.resolve()
130:             if abs_item in EXCLUDE_LIST:
131:                 skipped_count += 1
132:                 continue # Skip protected items
133: 
134:             print(f"🗑️ Deleting: {item.name}...")
135:             try:
136:                 if item.is_dir():
137:                     shutil.rmtree(item)
138:                 else:
139:                     item.unlink() # Delete file
140:                 print(f"✅ Deleted: {item.name}")
141:                 deleted_count += 1
142:             except Exception as e:
143:                 print(f"❌ Error deleting {item.name}: {e}")
144:         
145:         print("\n--- Global Cleanup Process Complete ---")
146:         print(f"Summary: {deleted_count} items deleted, {skipped_count} items skipped (protected).")
147:         print("Please restart your runtime and run the notebook from the first cell for a fresh start.")
148:     _update_memory_info()
149: 
150: # --- END OF MODIFICATION ---
151: 
152: def generate_messages(deleted_files_dict):
153:     """Generates informative messages about deleted files."""
154:     messages = []
155: 
156:     for key, value in deleted_files_dict.items():
157:         object_word = key
158:         messages.append(f"Deleted {value} {object_word}")
159:     return messages
160: 
161: def execute_button_press(button):
162:     """Handles logic when the 'Execute Cleaning' button is pressed."""
163:     selected_cleaners = auto_cleaner_widget.value
164:     deleted_files_dict = {}
165: 
166:     output.clear_output() # Clear previous output each time
167: 
168:     if 'Delete All Except Notebook & Main.py' in selected_cleaners:
169:         clean_all_except_notebook_and_main() # Call the new global cleanup function
170:     else:
171:         for option in selected_cleaners:
172:             if option in directories:
173:                 with output: # Direct output to the output widget
174:                     print(f"🗑️ Cleaning {option}...")
175:                 deleted_count = clean_directory(directories[option], option)
176:                 deleted_files_dict[option] = deleted_count
177:                 with output: # Direct output to the output widget
178:                     for message in generate_messages({option: deleted_count}):
179:                         message_widget = HTML(f'<p class="output_message animated_message">{message}</p>')
180:                         display(message_widget)
181: 
182:     _update_memory_info()
183: 
184: def hide_button_press(button):
185:     """Handles logic when the 'Hide Widget' button is pressed."""
186:     factory.close(container, class_names=['hide'], delay=0.5)
187: 
188: ## ================= AutoCleaner Widgets =================
189: 
190: # Initialize the WidgetFactory
191: factory = WidgetFactory()
192: HR = widgets.HTML('<hr>')
193: 
194: # Load Css
195: factory.load_css(cleaner_css)
196: 
197: # --- START OF MODIFICATION ---
198: # Get WebUI path from settings.json for the 'Delete All' option's protected folders list
199: # This assumes settings.json has been populated by setup.py
200: try:
201:     settings_data = js.read(SETTINGS_PATH, 'WEBUI', {})
202:     current_webui_path = Path(settings_data.get('webui_path', str(HOME / 'webui')))
203: except Exception:
204:     current_webui_path = HOME / 'webui' # Fallback
205: # --- END OF MODIFICATION ---
206: 
207: directories = {
208:     'Images': output_dir,
209:     'Models': model_dir,
210:     'Vae': vae_dir,
211:     'LoRa': lora_dir,
212:     'ControlNet Models': control_dir
213:     # Add other categories if needed, using the paths established by webui_utils.py
214:     # e.g., 'Embeddings': embed_dir,
215:     # 'Extensions': extension_dir, # Extensions usually in WEBUI folder, be careful with this
216: }
217: 
218: # --- START OF MODIFICATION ---
219: clean_options = list(directories.keys())
220: # Add the new 'Delete All Except Notebook & Main.py' option
221: clean_options.append('Delete All Except Notebook & Main.py') 
222: # --- END OF MODIFICATION ---
223: 
224: instruction_label = factory.create_html('''
225: <span class="instruction">Use <span style="color: #B2B2B2;">ctrl</span> or <span style="color: #B2B2B2;">shift</span> for multiple selections.</span>
226: ''')
227: auto_cleaner_widget = factory.create_select_multiple(clean_options, '', [], layout={'width': 'auto'}, class_names=['custom_select_multiple'])
228: output = widgets.Output().add_class('output_panel')
229: # ---
230: execute_button = factory.create_button('Execute Cleaning', class_names=['button_execute', 'cleaner_button'])
231: hide_button = factory.create_button('Hide Widget', class_names=['button_hide', 'cleaner_button'])
232: 
233: # Button Click
234: execute_button.on_click(execute_button_press)
235: hide_button.on_click(hide_button_press)
236: # ---
237: storage_info = factory.create_html(f'''
238: <div class="storage_info">Total storage: {psutil.disk_usage(os.getcwd()).total / (1024 ** 3):.2f} GB <span style="color: #555">|</span> Used: {psutil.disk_usage(os.getcwd()).used / (1024 ** 3):.2f} GB <span style="color: #555">|</span> Free: {psutil.disk_usage(os.getcwd()).free / (1024 ** 3):.2f} GB</div>
239: ''')
240: # ---
241: buttons = factory.create_hbox([execute_button, hide_button])
242: lower_information_panel = factory.create_hbox([buttons, storage_info], class_names=['lower_information_panel'])
243: 
244: # Create a horizontal layout for the selection and output areas
245: hbox_layout = factory.create_hbox([auto_cleaner_widget, output], class_names=['selection_output_layout'])
246: 
247: container = factory.create_vbox([instruction_label, HR, hbox_layout, HR, lower_information_panel],
248:                                 layout={'width': '1080px'}, class_names=['cleaner_container'])
249: 
250: factory.display(container)
```

## File: scripts/cleaner_gui.py
```python
  1: import ipywidgets as widgets
  2: from IPython.display import display, clear_output, HTML
  3: from pathlib import Path
  4: import shutil
  5: import os
  6: import sys
  7: 
  8: # Assume json_utils is available since setup.py should have added modules to sys.path
  9: try:
 10:     import json_utils as js
 11: except ImportError:
 12:     # Fallback if json_utils isn't imported for some reason
 13:     class FallbackJsonUtils:
 14:         def read(self, *args, **kwargs):
 15:             return {}
 16:     js = FallbackJsonUtils()
 17:     print("Warning: json_utils not found, using fallback for settings.")
 18: 
 19: 
 20: # Constants (read from settings.json or derive)
 21: SETTINGS_PATH = Path.home() / 'ANXETY' / 'settings.json'
 22: 
 23: # Attempt to load settings to get paths
 24: try:
 25:     settings = js.read(SETTINGS_PATH)
 26:     HOME_PATH = Path(settings.get('ENVIRONMENT', {}).get('home_path', str(Path.home())))
 27:     SCR_PATH = Path(settings.get('ENVIRONMENT', {}).get('scr_path', str(Path.home() / 'ANXETY')))
 28:     WEBUI_PATH = Path(settings.get('WEBUI', {}).get('webui_path', str(HOME_PATH / 'webui')))
 29:     VENV_PATH = Path(settings.get('ENVIRONMENT', {}).get('venv_path', str(HOME_PATH / 'venv')))
 30:     SHARED_MODEL_BASE = Path(HOME_PATH / 'sd_models_shared') # Consistent with webui_utils.py
 31: except Exception as e:
 32:     # Fallback for paths if settings.json cannot be read or is incomplete
 33:     print(f"Warning: Could not load full settings for cleaner paths ({e}). Using default derived paths.")
 34:     HOME_PATH = Path.home()
 35:     SCR_PATH = HOME_PATH / 'ANXETY'
 36:     WEBUI_PATH = HOME_PATH / 'webui' # Fallback
 37:     VENV_PATH = HOME_PATH / 'venv'
 38:     SHARED_MODEL_BASE = HOME_PATH / 'sd_models_shared'
 39: 
 40: 
 41: def delete_folder(path, description):
 42:     """Deletes a folder if it exists, with confirmation and feedback."""
 43:     if path.exists():
 44:         clear_output(wait=True)
 45:         print(f"🗑️ Attempting to delete: {description} ({path})...")
 46:         try:
 47:             shutil.rmtree(path)
 48:             print(f"✅ Successfully deleted: {description}")
 49:         except Exception as e:
 50:             print(f"❌ Error deleting {description} ({path}): {e}")
 51:     else:
 52:         clear_output(wait=True)
 53:         print(f"ℹ️ {description} ({path}) does not exist. Skipping.")
 54: 
 55: def delete_anxiety_folder(button):
 56:     delete_folder(SCR_PATH, "ANXETY folder")
 57: 
 58: def delete_script_generated_folders(button):
 59:     clear_output(wait=True)
 60:     print("🗑️ Initiating deletion of all major script-generated content...")
 61:     
 62:     folders_to_delete = [
 63:         SCR_PATH, # The ANXETY folder
 64:         SHARED_MODEL_BASE, # The shared models folder
 65:         VENV_PATH, # The Python virtual environment
 66:         WEBUI_PATH # The currently installed WebUI (e.g., ReForge)
 67:     ]
 68: 
 69:     for folder in folders_to_delete:
 70:         delete_folder(folder, f"'{folder.name}' folder")
 71:     
 72:     print("\nCleanup attempt complete.")
 73: 
 74: # --- GUI Setup ---
 75: output_area = widgets.Output()
 76: 
 77: header = widgets.HTML("<h3>🧹 sdAIgen Cleanup Utility</h3>")
 78: 
 79: anxiety_button = widgets.Button(description="Delete ANXETY Folder", button_style='danger')
 80: anxiety_button.on_click(delete_anxiety_folder)
 81: 
 82: script_generated_button = widgets.Button(description="Delete All Script-Generated Content", button_style='danger')
 83: script_generated_button.on_click(delete_script_generated_folders)
 84: 
 85: warning_html = widgets.HTML("""
 86:     <p style="color: red; font-weight: bold;">
 87:         WARNING: These actions are irreversible and will delete files. Use with extreme caution.
 88:     </p>
 89:     <p style="color: yellow;">
 90:         "Delete All Script-Generated Content" will remove:
 91:         <ul>
 92:             <li>Your `ANXETY` scripts and settings.</li>
 93:             <li>All models in your `sd_models_shared` folder.</li>
 94:             <li>Your Python virtual environment (`venv`).</li>
 95:             <li>Your selected WebUI installation (e.g., `ReForge`).</li>
 96:         </ul>
 97:         This will effectively revert your environment to a clean state, requiring a full re-setup from the first cell.
 98:     </p>
 99: """)
100: 
101: display(header, warning_html, anxiety_button, script_generated_button, output_area)
102: 
103: # Redirect print statements to the output_area (for the GUI buttons)
104: def custom_print_to_output_area(*args, **kwargs):
105:     with output_area:
106:         built_in_print(*args, **kwargs)
107: 
108: # Save original print function
109: built_in_print = print
110: sys.stdout = custom_print_to_output_area
111: sys.stderr = custom_print_to_output_area
```

## File: scripts/download-result.py
```python
  1: # ~ download-result.py | by ANXETY ~
  2: 
  3: from widget_factory import WidgetFactory    # WIDGETS
  4: import json_utils as js                     # JSON
  5: 
  6: import ipywidgets as widgets
  7: from pathlib import Path
  8: import json
  9: import time
 10: import re
 11: import os
 12: 
 13: 
 14: # Constants
 15: HOME = Path.home()
 16: SCR_PATH = Path(HOME / 'ANXETY')
 17: SETTINGS_PATH = SCR_PATH / 'settings.json'
 18: 
 19: UI = js.read(SETTINGS_PATH, 'WEBUI.current')
 20: 
 21: CSS = SCR_PATH / 'CSS'
 22: widgets_css = CSS / 'download-result.css'
 23: 
 24: 
 25: ## ================= loading settings V5 =================
 26: 
 27: def load_settings(path):
 28:     """Load settings from a JSON file."""
 29:     try:
 30:         return {
 31:             **js.read(path, 'ENVIRONMENT'),
 32:             **js.read(path, 'WIDGETS'),
 33:             **js.read(path, 'WEBUI')
 34:         }
 35:     except (json.JSONDecodeError, IOError) as e:
 36:         print(f"Error loading settings: {e}")
 37:         return {}
 38: 
 39: # Load settings
 40: settings = load_settings(SETTINGS_PATH)
 41: locals().update(settings)
 42: 
 43: ## ======================= WIDGETS =======================
 44: 
 45: HR = widgets.HTML('<hr class="divider-line">')
 46: HEADER_DL = 'DOWNLOAD RESULTS'
 47: VERSION = 'v0.58'
 48: 
 49: factory = WidgetFactory()
 50: 
 51: # Load CSS
 52: factory.load_css(widgets_css)
 53: 
 54: # Define extensions to filter out
 55: EXCLUDED_EXTENSIONS = {'.txt', '.yaml', '.log', '.json'}
 56: 
 57: ## Functions
 58: def output_container_generator(header, items, is_grid=False):
 59:     """Create a container widget for output items."""
 60:     header_widget = factory.create_html(f'<div class="section-title">{header} ➤</div>')
 61:     content_widgets = [factory.create_html(f'<div class="output-item">{item}</div>') for item in items]
 62: 
 63:     container_method = factory.create_hbox if is_grid else factory.create_vbox    # hbox -> grid
 64:     content_container = container_method(content_widgets).add_class('_horizontal' if is_grid else '')
 65: 
 66:     return factory.create_vbox([header_widget, content_container]).add_class('output-section')
 67: 
 68: def get_all_files_list(directory, extensions, excluded_dirs=[]):
 69:     """Get all files in the directory and its subdirectories, excluding specified directories."""
 70:     if not os.path.isdir(directory):
 71:         return []
 72: 
 73:     files_list = []
 74:     for root, dirs, files in os.walk(directory, followlinks=True):
 75:         # Exclude specified directories
 76:         dirs[:] = [d for d in dirs if d not in excluded_dirs]
 77: 
 78:         for file in files:
 79:             if file.endswith(extensions) and not file.endswith(tuple(EXCLUDED_EXTENSIONS)):
 80:                 files_list.append(file)  # Store only the file name
 81:     return files_list
 82: 
 83: def get_folders_list(directory):
 84:     """List folders in a directory, excluding hidden folders."""
 85:     if not os.path.isdir(directory):
 86:         return []
 87:     return [
 88:         folder for folder in os.listdir(directory)
 89:         if os.path.isdir(os.path.join(directory, folder)) and not folder.startswith('__')
 90:     ]
 91: 
 92: def get_controlnets_list(directory, filter_pattern):
 93:     """List ControlNet files matching a specific pattern."""
 94:     if not os.path.isdir(directory):
 95:         return []
 96:     filter_name = re.compile(filter_pattern)
 97:     return [
 98:         filter_name.match(file).group(1) if filter_name.match(file) else file
 99:         for file in os.listdir(directory)
100:         if not file.endswith(tuple(EXCLUDED_EXTENSIONS)) and '.' in file
101:     ]
102: 
103: ## Widgets
104: header_widget = factory.create_html(f'''
105: <div><span class="header-main-title">{HEADER_DL}</span> <span style="color: grey; opacity: 0.25;">| {VERSION}</span></div>
106: ''')
107: 
108: # Models
109: models_list = get_all_files_list(model_dir, ('.safetensors', '.ckpt'))
110: models_widget = output_container_generator('Models', models_list)
111: # Vaes
112: vaes_list = get_all_files_list(vae_dir, ('.safetensors',))
113: vaes_widget = output_container_generator('VAEs', vaes_list)
114: # Embeddings
115: embed_filter = ['SD', 'XL']
116: embeddings_list = get_all_files_list(embed_dir, ('.safetensors', '.pt'), embed_filter)
117: embeddings_widget = output_container_generator('Embeddings', embeddings_list)
118: # LoRAs
119: loras_list = get_all_files_list(lora_dir, ('.safetensors',))
120: loras_widget = output_container_generator('LoRAs', loras_list)
121: # Extensions
122: extensions_list = get_folders_list(extension_dir)
123: extension_type = 'Nodes' if UI == 'ComfyUI' else 'Extensions'
124: extensions_widget = output_container_generator(extension_type, extensions_list, is_grid=True)
125: # ADetailers
126: adetailers_list = get_all_files_list(adetailer_dir, ('.safetensors', '.pt'))
127: adetailers_widget = output_container_generator('ADetailers', adetailers_list)
128: # Clips
129: clips_list = get_all_files_list(clip_dir, ('.safetensors',))
130: clips_widget = output_container_generator('Clips', clips_list)
131: # Unets
132: unets_list = get_all_files_list(unet_dir, ('.safetensors',))
133: unets_widget = output_container_generator('Unets', unets_list)
134: # (Clip) Visions
135: visions_list = get_all_files_list(vision_dir, ('.safetensors',))
136: visions_widget = output_container_generator('Visions', visions_list)
137: # (Text) Encoders
138: encoders_list = get_all_files_list(encoder_dir, ('.safetensors',))
139: encoders_widget = output_container_generator('Encoders', encoders_list)
140: # Diffusions (Models)
141: diffusions_list = get_all_files_list(diffusion_dir, ('.safetensors',))
142: diffusions_widget = output_container_generator('Diffusions', diffusions_list)
143: # ControlNet
144: controlnets_list = get_controlnets_list(control_dir, r'^[^_]*_[^_]*_[^_]*_(.*)_fp16\.safetensors')
145: controlnets_widget = output_container_generator('ControlNets', controlnets_list)
146: 
147: ## Sorting and Output
148: widgets_dict = {
149:     models_widget: models_list,
150:     vaes_widget: vaes_list,
151:     embeddings_widget: embeddings_list,
152:     loras_widget: loras_list,
153:     extensions_widget: extensions_list,
154:     adetailers_widget: adetailers_list,
155:     clips_widget: clips_list,
156:     unets_widget: unets_list,
157:     visions_widget: visions_list,
158:     encoders_widget: encoders_list,
159:     diffusions_widget: diffusions_list,
160:     controlnets_widget: controlnets_list
161: }
162: 
163: outputs_widgets_list = [widget for widget, widget_list in widgets_dict.items() if widget_list]
164: result_output_widget = factory.create_hbox(outputs_widgets_list).add_class('result-output-container')
165: 
166: container_widget = factory.create_vbox([header_widget, HR, result_output_widget, HR],
167:                                        layout={'width': '1080px'}).add_class('result-container')
168: factory.display(container_widget)
```

## File: scripts/launch.py
```python
  1: # ~ launch.py | by ANXETY ~
  2: 
  3: from TunnelHub import Tunnel    # Tunneling
  4: import json_utils as js         # JSON
  5: 
  6: from IPython.display import clear_output
  7: from IPython import get_ipython
  8: from datetime import timedelta
  9: from pathlib import Path
 10: import subprocess
 11: import requests
 12: import argparse
 13: import logging
 14: import asyncio
 15: import shlex
 16: import time
 17: import json
 18: import yaml
 19: import sys
 20: import os
 21: import re
 22: 
 23: 
 24: # Universal platform detection and optimization
 25: def detect_and_optimize_platform():
 26:     """Detect platform and apply all necessary optimizations"""
 27:     import os
 28:     from pathlib import Path
 29: 
 30:     # Get platform from environment or detect
 31:     platform = os.environ.get('DETECTED_PLATFORM', 'local')
 32: 
 33:     if not platform or platform == 'local':
 34:         # Re-detect platform
 35:         try:
 36:             import google.colab
 37:             platform = 'colab'
 38:         except ImportError:
 39:             pass
 40: 
 41:         if os.path.exists('/kaggle'):
 42:             return 'kaggle'
 43:         elif (os.environ.get('LIGHTNING_CLOUD_PROJECT_ID') or
 44:               os.environ.get('LIGHTNING_AI') or
 45:               os.path.exists('/teamspace') or
 46:               'lightning' in os.environ.get('PWD', '').lower() == True or # Ensure exact match on 'lightning' in PWD for stricter detection
 47:               'studios' in os.environ.get('PWD', '').lower() == True):   # Ensure exact match on 'studios' in PWD
 48:             platform = 'lightning'
 49:         elif 'lightning' in str(Path.home()).lower(): # Final check for home path
 50:              platform = 'lightning'
 51: 
 52: 
 53:     # Set platform environment variable
 54:     os.environ['DETECTED_PLATFORM'] = platform
 55:     print(f"🔍 Platform detected: {platform}")
 56: 
 57:     # Apply platform-specific optimizations
 58:     if platform == 'lightning':
 59:         # Lightning AI optimizations
 60:         optimizations = {
 61:             'PYTORCH_CUDA_ALLOC_CONF': 'max_split_size_mb:128',
 62:             'CUDA_LAUNCH_BLOCKING': '1',
 63:             'TMPDIR': '/tmp/sdaigen',
 64:             'TEMP': '/tmp/sdaigen',
 65:             'CUDA_VISIBLE_DEVICES': '0',  # Use first GPU only
 66:         }
 67: 
 68:         for key, value in optimizations.items():
 69:             os.environ[key] = value
 70: 
 71:         # Create temp directories
 72:         temp_dirs = ['/tmp/sdaigen', '/teamspace/studios/this_studio/temp']
 73:         for temp_dir in temp_dirs:
 74:             Path(temp_dir).mkdir(parents=True, exist_ok=True)
 75: 
 76:         print("⚡ Applied Lightning AI optimizations")
 77: 
 78:         # Define SHARED_MODEL_BASE BEFORE it's used in the return statement
 79:         SHARED_MODEL_BASE = Path('/teamspace/studios/this_studio') / 'sd_models_shared'
 80:         os.makedirs(SHARED_MODEL_BASE, exist_ok=True) # Ensure shared base exists
 81: 
 82:         # Return Lightning AI launch arguments, explicitly adding --share
 83:         return [
 84:             '--xformers',
 85:             '--no-half-vae',
 86:             '--opt-split-attention',
 87:             '--medvram',
 88:             '--disable-console-progressbars',
 89:             '--api',
 90:             # MODIFICATION: Quote argument to prevent zsh globbing error
 91:             "'--cors-allow-origins=*'",
 92:             '--listen',
 93:             '--port=8080',
 94:             '--share', # Added to enable public Gradio link
 95:             f'--ckpt-dir={SHARED_MODEL_BASE}/Stable-diffusion', # Point to shared location
 96:             f'--embeddings-dir={SHARED_MODEL_BASE}/embeddings', # Point to shared location
 97:             f'--lora-dir={SHARED_MODEL_BASE}/loras', # Point to shared location
 98:             f'--vae-dir={SHARED_MODEL_BASE}/vae', # Point to shared location
 99:             f'--controlnet-dir={SHARED_MODEL_BASE}/ControlNet', # Point to shared location
100:             '--disable-safe-unpickle',  # For Lightning AI compatibility
101:             '--skip-torch-cuda-test',   # Skip CUDA tests
102:             '--no-download-sd-model'    # Don't auto-download models
103:         ]
104: 
105:     elif platform == 'colab':
106:         # Google Colab optimizations
107:         os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
108:         return [
109:             '--share',
110:             '--xformers',
111:             '--enable-insecure-extension-access',
112:             '--opt-split-attention'
113:         ]
114: 
115:     elif platform == 'kaggle':
116:         # Kaggle optimizations
117:         os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
118:         return [
119:             '--listen',
120:             '--port=8080',
121:             '--xformers',
122:             '--medvram',
123:             '--opt-split-attention'
124:         ]
125: 
126:     else:
127:         # Local/default
128:         return ['--xformers']
129: 
130: # Apply optimizations and get launch arguments
131: PLATFORM_ARGS = detect_and_optimize_platform()
132: 
133: 
134: CD = os.chdir
135: ipySys = get_ipython().system
136: 
137: # Constants
138: HOME = Path.home()
139: VENV = HOME / 'venv'
140: SCR_PATH = HOME / 'ANXETY'
141: SETTINGS_PATH = SCR_PATH / 'settings.json'
142: 
143: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
144: UI = js.read(SETTINGS_PATH, 'WEBUI.current')
145: WEBUI = Path(js.read(SETTINGS_PATH, 'WEBUI.webui_path')) # Ensure WEBUI is a Path object
146: 
147: 
148: BIN = str(VENV / 'bin')
149: PKG = str(VENV / 'lib/python3.10/site-packages')
150: 
151: if BIN not in os.environ['PATH']:
152:     os.environ['PATH'] = BIN + ':' + os.environ['PATH']
153: # Fix: Safely get PYTHONPATH, defaulting to empty string if not set
154: if PKG not in os.environ.get('PYTHONPATH', ''):
155:     os.environ['PYTHONPATH'] = PKG + ':' + os.environ.get('PYTHONPATH', '')
156: 
157: 
158: ## ================ loading settings V5 ==================
159: 
160: def load_settings(path):
161:     """Load settings from a JSON file."""
162:     try:
163:         return {
164:             **js.read(path, 'ENVIRONMENT'),
165:             **js.read(path, 'WIDGETS'),
166:             **js.read(path, 'WEBUI')
167:         }
168:     except (json.JSONDecodeError, IOError) as e:
169:         print(f"Error loading settings: {e}")
170:         return {}
171: 
172: # Load settings upfront so all variables are defined
173: settings = load_settings(SETTINGS_PATH)
174: locals().update(settings) # This populates ngrok_token, etc.
175: 
176: 
177: ## ====================== Helpers ========================
178: 
179: def parse_arguments():
180:     parser = argparse.ArgumentParser()
181:     parser.add_argument('-l', '--log', action='store_true', help='Show failed tunnel details')
182:     return parser.parse_args()
183: 
184: def _trashing():
185:     dirs = ['A1111', 'ComfyUI', 'Forge', 'Classic', 'ReForge', 'SD-UX']
186:     paths = [Path(HOME) / name for name in dirs]
187: 
188:     for path in paths:
189:         cmd = f"find {path} -type d -name .ipynb_checkpoints -exec rm -rf {{}} +"
190:         subprocess.run(shlex.split(cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
191: 
192: def _update_config_paths():
193:     """Update configuration paths in WebUI config file."""
194:     config_mapping = {
195:         'tagger_hf_cache_dir': f"{WEBUI}/models/interrogators/",
196:         'ad_extra_models_dir': adetailer_dir,
197:         # 'sd_checkpoint_hash': '',
198:         # 'sd_model_checkpoint': '',
199:         'sd_vae': 'None'
200:     }
201: 
202:     config_file = WEBUI / 'config.json' # Ensure config_file is a Path object
203:     for key, value in config_mapping.items():
204:         if js.key_exists(config_file, key):
205:             js.update(config_file, key, str(value))
206:         else:
207:             js.save(config_file, key, str(value))
208: 
209: def get_launch_command():
210:     """Construct launch command based on configuration"""
211:     # Ensure commandline_arguments is from the loaded settings
212:     base_args = settings.get('commandline_arguments', '') # Safely get from settings
213:     password = 'ha4ez7147b5vdlu5u8f8flrllgn61kpbgbh6emil'
214: 
215:     common_args = ' --enable-insecure-extension-access --disable-console-progressbars --theme dark'
216:     if ENV_NAME == 'Kaggle':
217:         common_args += f" --encrypt-pass={password}"
218: 
219:     # Accent Color For Anxety-Theme
220:     # Ensure theme_accent is from the loaded settings
221:     theme_accent_val = settings.get('theme_accent', 'anxety') # Safely get from settings
222:     if theme_accent_val != 'anxety':
223:         common_args += f" --anxety {theme_accent_val}"
224: 
225:     if UI == 'ComfyUI':
226:         return f"python3 main.py {base_args}"
227:     elif UI == 'ReForge': # Specific handling for ReForge, assuming 'webui.py' is its main entry point
228:         final_args = " ".join(PLATFORM_ARGS)
229:         return f"python3 webui.py {final_args}{common_args}"
230:     else: # Default case for other UIs like A1111, Forge, Classic, SD-UX
231:         final_args = " ".join(PLATFORM_ARGS)
232:         return f"python3 launch.py {final_args}{common_args}"
233: 
234: ## ===================== Tunneling =======================
235: 
236: class TunnelManager:
237:     """Class for managing tunnel services"""
238: 
239:     def __init__(
240:         self,
241:         tunnel_port,
242:         ngrok_token_param=None
243:     ):
244:         self.tunnel_port = tunnel_port
245:         self.ngrok_token = ngrok_token_param
246:         self.tunnels = []
247:         self.error_reasons = []
248:         self.public_ip = self._get_public_ip()
249:         self.checking_queue = asyncio.Queue()
250:         self.timeout = 10
251: 
252:     def _get_public_ip(self) -> str:
253:         """Retrieve and cache public IPv4 address"""
254:         cached_ip = js.read(SETTINGS_PATH, 'ENVIRONMENT.public_ip')
255:         if cached_ip:
256:             return cached_ip
257: 
258:         try:
259:             response = requests.get('https://api64.ipify.org?format=json&ipv4=true', timeout=5)
260:             public_ip = response.json().get('ip', 'N/A')
261:             js.update(SETTINGS_PATH, 'ENVIRONMENT.public_ip', public_ip)
262:             return public_ip
263:         except Exception as e:
264:             print(f"Error getting public IP address: {e}")
265:             return 'N/A'
266: 
267:     async def _print_status(self):
268:         """Async status printer"""
269:         print('\033[33m>> Tunnels:\033[0m')
270:         while True:
271:             service_name = await self.checking_queue.get()
272:             print(f"- 🕒 Checking \033[36m{service_name}\003[0m...")
273:             self.checking_queue.task_done()
274: 
275:     async def _test_tunnel(self, name, config):
276:         """Async tunnel testing"""
277:         await self.checking_queue.put(name)
278:         try:
279:             # Use the venv python to run gradio cli, more robust
280:             command_to_run = config['command']
281:             if "gradio.cli" in command_to_run:
282:                 command_to_run = f"{VENV / 'bin' / 'python'} {command_to_run}"
283: 
284:             process = await asyncio.create_subprocess_exec(
285:                 *shlex.split(command_to_run),
286:                 stdout=asyncio.subprocess.PIPE,
287:                 stderr=asyncio.subprocess.STDOUT
288:             )
289: 
290:             start_time = time.time()
291:             output = []
292:             pattern_found = False
293:             check_interval = 0.5
294: 
295:             while time.time() - start_time < self.timeout:
296:                 try:
297:                     line = await asyncio.wait_for(
298:                         process.stdout.readline(),
299:                         timeout=check_interval
300:                     )
301:                     if not line:
302:                         continue
303: 
304:                     line = line.decode().strip()
305:                     output.append(line)
306: 
307:                     if config['pattern'].search(line):
308:                         pattern_found = True
309:                         break
310: 
311:                 except asyncio.TimeoutError:
312:                     continue
313: 
314:             if process.returncode is None:
315:                 try:
316:                     process.terminate()
317:                     await asyncio.wait_for(process.wait(), timeout=2)
318:                 except:
319:                     pass
320: 
321:             if pattern_found:
322:                 return True, None
323: 
324:             error_msg = '\n'.join(output[-3:]) or 'No output received'
325:             return False, f"Process error: {error_msg[:300]}..."
326: 
327:         except Exception as e:
328:             return False, f"Process error: {str(e)}"
329: 
330:     async def setup_tunnels(self):
331:         """Async tunnel configuration"""
332:         # MODIFICATION: Use `python -m gradio.cli tunnel` for robustness and comment out failing services.
333:         services = [
334:             ('Gradio', {
335:                 'command': f"-m gradio.cli tunnel {self.tunnel_port}",
336:                 'pattern': re.compile(r'[\w-]+\.gradio\.live')
337:             }),
338:             ('Serveo', {
339:                 'command': f"ssh -o StrictHostKeyChecking=no -R 80:localhost:{self.tunnel_port} serveo.net",
340:                 'pattern': re.compile(r'[\w-]+\.serveo\.net')
341:             }),
342:             ('Pinggy', {
343:                 'command': f"ssh -o StrictHostKeyChecking=no -p 80 -R0:localhost:{self.tunnel_port} a.pinggy.io",
344:                 'pattern': re.compile(r'[\w-]+\.a\.free\.pinggy\.link')
345:             }),
346:             # ('Cloudflared', {
347:             #     'command': f"cl tunnel --url localhost:{self.tunnel_port}",
348:             #     'pattern': re.compile(r'[\w-]+\.trycloudflare\.com')
349:             # }),
350:             # ('Localtunnel', {
351:             #     'command': f"lt --port {self.tunnel_port}",
352:             #     'pattern': re.compile(r'[\w-]+\.loca\.lt'),
353:             #     'note': f"Password: \033[32m{self.public_ip}\033[0m"
354:             # })
355:         ]
356: 
357:         if self.ngrok_token: # Use self.ngrok_token from instance variable
358:             config_path = HOME / '.config/ngrok/ngrok.yml'
359:             current_token = None
360: 
361:             if config_path.exists():
362:                 with open(config_path, 'r') as f:
363:                     current_token = yaml.safe_load(f).get('agent', {}).get('authtoken')
364: 
365:             if current_token != self.ngrok_token: # Use self.ngrok_token
366:                 ipySys(f"ngrok config add-authtoken {self.ngrok_token}")
367: 
368:             # NOTE: Commenting out Ngrok as the executable is likely missing or has permission issues.
369:             # services.append(('Ngrok', {
370:             #     'command': f"ngrok http http://localhost:{self.tunnel_port} --log stdout",
371:             #     'pattern': re.compile(r'https://[\w-]+\.ngrok-free\.app')
372:             # }))
373: 
374:         # Create status printer task
375:         printer_task = asyncio.create_task(self._print_status())
376: 
377:         # Run all tests concurrently
378:         tasks = []
379:         for name, config in services:
380:             tasks.append(self._test_tunnel(name, config))
381: 
382:         results = await asyncio.gather(*tasks)
383: 
384:         # Cancel status printer
385:         printer_task.cancel()
386:         try:
387:             await printer_task
388:         except asyncio.CancelledError:
389:             pass
390: 
391:         # Process results
392:         for (name, config), (success, error) in zip(services, results):
393:             if success:
394:                 self.tunnels.append({**config, 'name': name})
395:             else:
396:                 self.error_reasons.append({'name': name, 'reason': error})
397: 
398:         return (
399:             self.tunnels,
400:             len(services),
401:             len(self.tunnels),
402:             len(self.error_reasons)
403:         )
404: 
405: ## ========================= Main ========================
406: 
407: import nest_asyncio
408: nest_asyncio.apply()
409: 
410: if __name__ == '__main__':
411:     """Main execution flow"""
412:     args = parse_arguments()
413:     print('Please Wait...\n')
414: 
415:     os.environ['PYTHONWARNINGS'] = 'ignore'
416: 
417:     # Initialize tunnel manager and services
418:     tunnel_port = 8188 if UI == 'ComfyUI' else 7860
419:     # Pass tokens from loaded settings to TunnelManager instance
420:     tunnel_mgr = TunnelManager(
421:         tunnel_port,
422:         ngrok_token_param=settings.get('ngrok_token')
423:     )
424: 
425:     # Run async setup
426:     loop = asyncio.new_event_loop()
427:     asyncio.set_event_loop(loop)
428:     try:
429:         tunnels, total, success, errors = loop.run_until_complete(tunnel_mgr.setup_tunnels())
430:     except Exception as e:
431:         print(f"Error during tunnel setup: {e}")
432:         tunnels, total, success, errors = [], 0, 0, 0 # Fallback if no tunnels are added
433: 
434:     # Set up tunneling service
435:     tunnelingService = Tunnel(tunnel_port)
436:     tunnelingService.logger.setLevel(logging.DEBUG)
437: 
438:     # Only add tunnels if any were successfully created
439:     if tunnels:
440:         for tunnel in tunnels:
441:             tunnelingService.add_tunnel(**tunnel)
442:     else:
443:         print("No tunnels were successfully established.") # Inform user if no tunnels are added
444: 
445:     clear_output(wait=True)
446: 
447:     # Launch sequence
448:     _trashing()
449:     _update_config_paths()
450:     LAUNCHER = get_launch_command()
451: 
452:     # Ensure the static directory exists before writing the timer file
453:     static_dir = WEBUI / 'static'
454:     static_dir.mkdir(parents=True, exist_ok=True) # Create static directory
455:     
456:     # Setup pinggy timer
457:     ipySys(f"echo -n {int(time.time())+(3600+20)} > {static_dir}/timer-pinggy.txt")
458: 
459:     # Only proceed with tunnelingService if there are tunnels to manage
460:     if tunnels:
461:         with tunnelingService:
462:             CD(WEBUI)
463: 
464:             if UI == 'ComfyUI':
465:                 COMFYUI_SETTINGS_PATH = SCR_PATH / 'ComfyUI.json'
466:                 if check_custom_nodes_deps:
467:                     ipySys('python3 install-deps.py')
468:                     clear_output(wait=True)
469: 
470:                 if not js.key_exists(COMFYUI_SETTINGS_PATH, 'install_req', True):
471:                     print('Installing ComfyUI dependencies...')
472:                     subprocess.run(['pip', 'install', '-r', 'requirements.txt'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
473:                     js.save(COMFYUI_SETTINGS_PATH, 'install_req', True)
474:                     clear_output(wait=True)
475: 
476:             print(f"\033[34m>> Total Tunnels:\033[0m {total} | \033[32mSuccess:\033[0m {success} | \033[31mErrors:\003[0m {errors}\n")
477: 
478:             # Display error details if any
479:             if args.log and errors > 0:
480:                 print('\033[31m>> Failed Tunnels:\003[0m')
481:                 for error in tunnel_mgr.error_reasons:
482:                     print(f"  - {error['name']}: {error['reason']}")
483:                 print()
484: 
485:             print(f"🔧 WebUI: \033[34m{UI}\003[0m")
486: 
487:             try:
488:                 ipySys(LAUNCHER)
489:             except KeyboardInterrupt:
490:                 pass
491:     else:
492:         # If no tunnels were successfully established, launch WebUI without a tunneling service context
493:         print("Launching WebUI without active public tunnels (check logs for tunnel errors).")
494:         CD(WEBUI)
495:         if UI == 'ComfyUI': # Still run ComfyUI specific setup if needed
496:             COMFYUI_SETTINGS_PATH = SCR_PATH / 'ComfyUI.json'
497:             if check_custom_nodes_deps:
498:                 ipySys('python3 install-deps.py')
499:                 clear_output(wait=True)
500:             if not js.key_exists(COMFYUI_SETTINGS_PATH, 'install_req', True):
501:                 print('Installing ComfyUI dependencies...')
502:                 subprocess.run(['pip', 'install', '-r', 'requirements.txt'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
503:                 js.save(COMFYUI_SETTINGS_PATH, 'install_req', True)
504:                 clear_output(wait=True)
505: 
506:         print(f"🔧 WebUI: \033[34m{UI}\003[0m") # Re-print WebUI info
507:         try:
508:             ipySys(LAUNCHER)
509:         except KeyboardInterrupt:
510:             pass
511: 
512: 
513:     # Display session duration
514:     try:
515:         with open(f"{static_dir}/timer.txt") as f: # Use static_dir here
516:             timer = float(f.read())
517:             duration = timedelta(seconds=time.time() - timer)
518:             print(f"\n⌚️ Session duration: \033[33m{str(duration).split('.')[0]}\003[0m")
519:     except FileNotFoundError:
520:         pass
```

## File: scripts/setup.py
```python
  1: # ~ setup.py | by ANXETY ~
  2: 
  3: # VERY EARLY SYS.PATH MODIFICATION FOR CRITICAL IMPORTS
  4: import sys
  5: from pathlib import Path
  6: import os
  7: 
  8: _HOME_EARLY = Path.home()
  9: _ANXETY_PATH_EARLY = _HOME_EARLY / 'ANXETY'
 10: _MODULES_PATH_EARLY = _ANXETY_PATH_EARLY / 'modules'
 11: _SCRIPTS_PATH_EARLY = _ANXETY_PATH_EARLY / 'scripts'
 12: 
 13: # Ensure the directories exist and are added to sys.path at the highest priority
 14: _MODULES_PATH_EARLY.mkdir(parents=True, exist_ok=True)
 15: _SCRIPTS_PATH_EARLY.mkdir(parents=True, exist_ok=True)
 16: 
 17: if str(_MODULES_PATH_EARLY) not in sys.path:
 18:     sys.path.insert(0, str(_MODULES_PATH_EARLY))
 19: if str(_SCRIPTS_PATH_EARLY) not in sys.path:
 20:     sys.path.insert(0, str(_SCRIPTS_PATH_EARLY))
 21: # END VERY EARLY SYS.PATH MODIFICATION
 22: 
 23: 
 24: from IPython.display import display, HTML, clear_output
 25: from urllib.parse import urljoin
 26: from tqdm import tqdm
 27: import nest_asyncio
 28: import importlib
 29: import argparse
 30: import asyncio
 31: import aiohttp
 32: import time
 33: import json
 34: 
 35: 
 36: # Platform detection added for Lightning AI compatibility
 37: # The definitions of os and Path are now imported at the very top via the early sys.path modification
 38: # So we can proceed with using them directly without re-importing.
 39: 
 40: def detect_platform():
 41:     try:
 42:         import google.colab
 43:         return 'colab'
 44:     except ImportError:
 45:         pass
 46: 
 47:     if os.path.exists('/kaggle'):
 48:         return 'kaggle'
 49: 
 50:     if (
 51:         os.environ.get('LIGHTNING_CLOUD_PROJECT_ID') or
 52:         os.environ.get('LIGHTNING_AI') or
 53:         os.path.exists('/teamspace') or
 54:         'lightning' in os.environ.get('PWD', '').lower() or
 55:         'studios' in os.environ.get('PWD', '').lower() or
 56:         'lightning' in str(Path.home()).lower()
 57:     ):
 58:         return 'lightning'
 59: 
 60:     return 'local'
 61: 
 62: CURRENT_PLATFORM = detect_platform()
 63: print(f"Setup script detected platform: {CURRENT_PLATFORM}")
 64: 
 65: # Constants
 66: platform = os.environ.get('DETECTED_PLATFORM', 'local')
 67: if platform == 'lightning':
 68:     HOME = Path('/teamspace/studios/this_studio')
 69:     if not HOME.exists():
 70:         HOME = Path.home() / 'workspace'
 71:         HOME.mkdir(parents=True, exist_ok=True)
 72: elif platform == 'colab':
 73:     HOME = Path.home()
 74: elif platform == 'kaggle':
 75:     HOME = Path('/kaggle/working')
 76: else:
 77:     HOME = Path.cwd()
 78: SCR_PATH = HOME / 'ANXETY'
 79: SETTINGS_PATH = SCR_PATH / 'settings.json'
 80: 
 81: # Removed setup_module_folder_early and global import of json_utils.js
 82: # All necessary json operations are now inlined or use built-in json module
 83: 
 84: nest_asyncio.apply()  # Async support for Jupyter
 85: 
 86: 
 87: # ===================== UTILITIES (JSON/FILE OPERATIONS) =====================
 88: 
 89: # Inlined key_exists logic (previously from json_utils)
 90: def key_exists(filepath, key=None, value=None):
 91:     """Check key/value in JSON file."""
 92:     if not filepath.exists():
 93:         return False
 94:     try:
 95:         with open(filepath, 'r') as f:
 96:             data = json.load(f)
 97:     except json.JSONDecodeError:
 98:         return False
 99: 
100:     if key:
101:         keys = key.split('.')
102:         for k in keys:
103:             if isinstance(data, dict) and k in data:
104:                 data = data[k]
105:             else:
106:                 return False
107:         return (data == value) if value else True
108:     return False
109: 
110: # This function is now the primary way to save/update settings for setup.py
111: def save_data_to_json_nested(filepath, key_path, value):
112:     """Save value to a JSON file at a nested key path, creating parent dictionaries as needed."""
113:     try:
114:         if Path(filepath).exists():
115:             with open(filepath, 'r') as f:
116:                 data = json.load(f)
117:         else:
118:             data = {}
119:     except json.JSONDecodeError:
120:         data = {} # Handle corrupted JSON
121: 
122:     keys = key_path.split('.')
123:     current_data = data
124:     for i, k in enumerate(keys):
125:         if i == len(keys) - 1: # Last key
126:             current_data[k] = value
127:         else:
128:             if k not in current_data or not isinstance(current_data[k], dict):
129:                 current_data[k] = {}
130:             current_data = current_data[k]
131:     
132:     Path(filepath).parent.mkdir(parents=True, exist_ok=True) # Ensure directory exists
133:     with open(filepath, 'w') as f:
134:         json.dump(data, f, indent=4)
135: 
136: 
137: def save_environment_to_json(SETTINGS_PATH, data):
138:     """Save environment data to a JSON file."""
139:     existing_data = {}
140: 
141:     if SETTINGS_PATH.exists():
142:         try:
143:             with open(SETTINGS_PATH, 'r') as json_file:
144:                 existing_data = json.load(json_file)
145:         except json.JSONDecodeError:
146:             existing_data = {} # Handle corrupted settings.json
147: 
148:     existing_data.update(data)
149: 
150:     with open(SETTINGS_PATH, 'w') as json_file:
151:         json.dump(existing_data, json_file, indent=4)
152: 
153: def get_start_timer():
154:     """Get the start timer from settings or default to current time minus 5 seconds."""
155:     if SETTINGS_PATH.exists():
156:         try:
157:             with open(SETTINGS_PATH, 'r') as f:
158:                 settings = json.load(f)
159:                 return settings.get('ENVIRONMENT', {}).get('start_timer', int(time.time() - 5))
160:         except json.JSONDecodeError:
161:             return int(time.time() - 5) # Default if JSON is corrupt
162:     return int(time.time() - 5)
163: 
164: 
165: ## ======================= MODULES =======================
166: 
167: def clear_module_cache(modules_folder):
168:     """Clear the module cache for modules in the specified folder."""
169:     for module_name in list(sys.modules.keys()):
170:         module = sys.modules[module_name]
171:         if hasattr(module, '__file__') and module.__file__ and module.__file__.startswith(str(modules_folder)):
172:             del sys.modules[module_name]
173:     importlib.invalidate_caches()
174: 
175: def setup_module_folder(scr_folder):
176:     """Set up the module folder by clearing the cache and adding it to sys.path.
177:     This function is kept for consistency with how modules are cleared/reloaded later.
178:     The initial path addition is now handled by `setup_module_folder_early`.
179:     """
180:     clear_module_cache(scr_folder)
181:     # The path should already be there from setup_module_folder_early, but this ensures it.
182:     modules_folder = scr_folder / 'modules'
183:     modules_folder.mkdir(parents=True, exist_ok=True)
184:     if str(modules_folder) not in sys.path:
185:         sys.path.append(str(modules_folder))
186: 
187: 
188: # ===================== ENVIRONMENT SETUP =====================
189: 
190: def detect_environment():
191:     """Detect runtime environment."""
192:     envs = {'COLAB_GPU': 'Google Colab', 'KAGGLE_URL_BASE': 'Kaggle'}
193:     for var, name in envs.items():
194:         if var in os.environ:
195:             return name
196:     # The original detect_environment function did not recognize Lightning AI.
197:     # The new environment_setup will handle the platform detection and optimization.
198:     # This original function is effectively bypassed if the new environment_setup is used.
199:     # For safety, I'll update it to include lightning detection.
200:     if (
201:         os.environ.get('LIGHTNING_CLOUD_PROJECT_ID') or
202:         os.environ.get('LIGHTNING_AI') or
203:         os.path.exists('/teamspace') or
204:         'lightning' in os.environ.get('PWD', '').lower() or
205:         'studios' in os.environ.get('PWD', '').lower() or
206:         'lightning' in str(Path.home()).lower()
207:     ):
208:         return 'Lightning AI' # Returning "Lightning AI" as a distinct environment
209: 
210:     raise EnvironmentError(f"Unsupported environment. Supported: {', '.join(envs.values())}")
211: 
212: def get_fork_info(fork_arg):
213:     """Parse fork argument into user/repo."""
214:     if not fork_arg:
215:         return 'anxety-solo', 'sdAIgen'
216:     parts = fork_arg.split('/', 1)
217:     return parts[0], (parts[1] if len(parts) > 1 else 'sdAIgen')
218: 
219: def create_environment_data(env, scr_folder, lang, fork_user, fork_repo, branch):
220:     """Create a dictionary with environment data."""
221:     install_deps = key_exists(SETTINGS_PATH, 'ENVIRONMENT.install_deps', True)
222:     start_timer = get_start_timer()
223: 
224:     return {
225:         'ENVIRONMENT': {
226:             'lang': lang,
227:             'fork': f"{fork_user}/{fork_repo}",
228:             'branch': branch,
229:             'env_name': env,
230:             'install_deps': install_deps,
231:             'home_path': str(HOME),
232:             'venv_path': str(HOME / 'venv'),
233:             'scr_path': str(scr_folder),
234:             'start_timer': start_timer,
235:             'public_ip': ''
236:         }
237:     }
238: 
239: # Replacing the environment_setup function entirely as per comprehensive_patches.md
240: def environment_setup():
241:     """Universal environment setup - works on all platforms"""
242:     import os
243:     from pathlib import Path
244: 
245:     # Universal platform detection
246:     def detect_platform_internal():
247:         """Detect current platform reliably"""
248:         try:
249:             import google.colab
250:             return 'colab'
251:         except ImportError:
252:             pass
253: 
254:         # Check for Kaggle
255:         if os.path.exists('/kaggle'):
256:             return 'kaggle'
257: 
258:         # Check for Lightning AI - comprehensive detection
259:         lightning_indicators = [
260:             os.environ.get('LIGHTNING_CLOUD_PROJECT_ID'),
261:             os.environ.get('LIGHTNING_AI'),
262:             os.path.exists('/teamspace'),
263:             'lightning' in os.environ.get('PWD', '').lower() or # Ensure exact match on 'lightning' in PWD for stricter detection
264:             'studios' in os.environ.get('PWD', '').lower() or # Ensure exact match on 'studios' in PWD
265:             'lightning' in str(Path.home()).lower()
266:         ]
267: 
268:         if any(lightning_indicators):
269:             return 'lightning'
270: 
271:         return 'local'
272: 
273:     # Set platform and export to environment
274:     platform = detect_platform_internal()
275:     os.environ['DETECTED_PLATFORM'] = platform
276:     print(f"🔍 Detected platform: {platform}")
277: 
278:     # Platform-specific base path setup
279:     if platform == 'lightning':
280:         # Lightning AI paths
281:         base_path = Path('/teamspace/studios/this_studio')
282:         if not base_path.exists():
283:             base_path = Path.home() / 'workspace'
284: 
285:         # Ensure base path exists
286:         base_path.mkdir(parents=True, exist_ok=True)
287: 
288:         # Create all required directories
289:         required_dirs = [
290:             'models', 'outputs', 'extensions', 'embeddings',
291:             'lora', 'vae', 'controlnet', 'config', 'logs',
292:             'temp', '.cache', 'ANXETY', 'ANXETY/scripts', 'sd_models_shared' # Added sd_models_shared
293:         ]
294: 
295:         for dir_name in required_dirs:
296:             dir_path = base_path / dir_name
297:             dir_path.mkdir(parents=True, exist_ok=True)
298: 
299:         # Set Lightning AI optimizations
300:         os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'
301:         os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
302:         os.environ['TMPDIR'] = str(base_path / 'temp') # Updated to use base_path
303:         os.environ['TEMP'] = str(base_path / 'temp') # Updated to use base_path
304: 
305:         # Create temp directory
306:         (base_path / 'temp').mkdir(parents=True, exist_ok=True) # Ensure it's under base_path
307: 
308:         return str(base_path)
309: 
310:     elif platform == 'colab':
311:         # Google Colab setup
312:         base_path = Path('/content')
313:         return str(base_path)
314: 
315:     elif platform == 'kaggle':
316:         # Kaggle setup
317:         base_path = Path('/kaggle/working')
318:         base_path.mkdir(parents=True, exist_ok=True)
319:         return str(base_path)
320: 
321:     else:
322:         # Local/other platforms
323:         base_path = Path.cwd()
324:         return str(base_path)
325: 
326: 
327: # Replacing the Google Drive Mount Section entirely as per comprehensive_patches.md
328: def setup_storage():
329:     """Platform-aware storage setup"""
330:     platform = os.environ.get('DETECTED_PLATFORM', 'local')
331: 
332:     if platform == 'colab':
333:         try:
334:             from google.colab import drive
335:             drive.mount('/content/drive')
336:             return Path('/content/drive/MyDrive')
337:         except Exception as e:
338:             print(f"Drive mount failed: {e}")
339:             return HOME
340: 
341:     elif platform == 'lightning':
342:         # Use persistent storage for Lightning AI
343:         persistent_path = HOME / 'persistent' # Using HOME here as it's already set to studio base_path
344:         persistent_path.mkdir(parents=True, exist_ok=True)
345:         return persistent_path
346: 
347:     elif platform == 'kaggle':
348:         # Kaggle doesn't have persistent storage
349:         return HOME
350: 
351:     else:
352:         return HOME
353: 
354: DRIVE_PATH = setup_storage() # Assigning the result of setup_storage to DRIVE_PATH
355: # Fix: Save DRIVE_PATH to settings.json so other scripts can access it
356: save_data_to_json_nested(SETTINGS_PATH, 'ENVIRONMENT.gdrive_path', str(DRIVE_PATH))
357: 
358: 
359: ## ======================= DOWNLOAD LOGIC =====================
360: 
361: def generate_file_list(structure, base_url, base_path):
362:     """Generate flat list of (url, path) from nested structure"""
363:     def walk(struct, path_parts):
364:         items = []
365:         for key, value in struct.items():
366:             current_path = [*path_parts, key] if key else path_parts
367:             if isinstance(value, dict):
368:                 items.extend(walk(value, current_path))
369:             else:
370:                 url_path = '/'.join(current_path)
371:                 for file in value:
372:                     url = f"{base_url}/{url_path}/{file}" if url_path else f"{base_url}/{file}"
373:                     file_path = base_path / '/'.join(current_path) / file
374:                     items.append((url, file_path))
375:         return items
376: 
377:     return walk(structure, [])
378: 
379: async def download_file(session, url, path):
380:     """Download and save single file with error handling"""
381:     try:
382:         async with session.get(url) as resp:
383:             resp.raise_for_status()
384:             content = await resp.read()
385:             path.parent.mkdir(parents=True, exist_ok=True)
386:             path.write_bytes(content)
387:             return (True, url, path, None)
388:     except aiohttp.ClientResponseError as e:
389:         return (False, url, path, f"HTTP error {e.status}: {e.message}")
390:     except Exception as e:
391:         return (False, url, path, f"Error: {str(e)}")
392: 
393: async def download_files_async(scr_path, lang, fork_user, fork_repo, branch, log_errors):
394:     """Main download executor with error logging"""
395:     files_structure = {
396:         'CSS': ['main-widgets.css', 'download-result.css', 'auto-cleaner.css'],
397:         'JS': ['main-widgets.js'],
398:         'modules': ['json_utils.py', 'webui_utils.py', 'widget_factory.py',
399:                    'TunnelHub.py', 'CivitaiAPI.py', 'Manager.py', '__season.py'],
400:         'scripts': {
401:             'UIs': ['A1111.py', 'ComfyUI.py', 'Forge.py', 'Classic.py', 'ReForge.py', 'SD-UX.py'],
402:             lang: [f"widgets-{lang}.py", f"downloading-{lang}.py"],
403:             '': ['launch.py', 'auto-cleaner.py', 'download-result.py',
404:                 '_models-data.py', '_xl-models-data.py', '_loras-data.py'] # Added _loras-data.py
405:         }
406:     }
407: 
408:     base_url = f"https://raw.githubusercontent.com/{fork_user}/{fork_repo}/{branch}"
409:     file_list = generate_file_list(files_structure, base_url, scr_path)
410: 
411:     async with aiohttp.ClientSession() as session:
412:         tasks = [download_file(session, url, path) for url, path in file_list]
413: 
414:         errors = []
415:         futures = asyncio.as_completed(tasks)
416:         for future in tqdm(futures, total=len(tasks), desc="Downloading files", unit="file"):
417:             result = await future
418:             success, url, path, error = result
419:             if not success:
420:                 errors.append((url, path, error))
421: 
422:         clear_output()
423: 
424:         if log_errors and errors:
425:             print("\nErrors occurred during download:")
426:             for url, path, error in errors:
427:                 print(f"URL: {url}")
428:                 print(f"Path: {path}")
429:                 print(f"Error: {error}\n")
430: 
431: 
432: # ===================== MAIN EXECUTION =====================
433: 
434: async def main_async(args=None):
435:     """Entry point."""
436:     parser = argparse.ArgumentParser(description='ANXETY Download Manager')
437:     parser.add_argument('-l', '--lang', type=str, default='en', help='Language to be used (default: en)')
438:     parser.add_argument('-b', '--branch', type=str, default='main', help='Branch to download files from (default: main)')
439:     parser.add_argument('-f', '--fork', type=str, default=None, help='Specify project fork (user or user/repo)')
440:     parser.add_argument('-s', '--skip-download', action='store_true', help='Skip downloading files and just update the directory and modules')
441:     parser.add_argument('-L', '--log', action='store_true', help='Enable logging of download errors')
442: 
443:     args, _ = parser.parse_known_args(args)
444: 
445:     env = detect_environment() # Keep this call as is, as it's used for display_info
446:     user, repo = get_fork_info(args.fork)   # gitLogin , gitRepoName
447: 
448:     if not args.skip_download:
449:         await download_files_async(SCR_PATH, args.lang, user, repo, args.branch, args.log)    # download scripts files
450: 
451:     setup_module_folder(SCR_PATH)   # setup main dir -> modules
452: 
453:     env_data = create_environment_data(env, SCR_PATH, args.lang, user, repo, args.branch)
454:     save_environment_to_json(SETTINGS_PATH, env_data)
455: 
456:     # display info text | MODULES
457:     from __season import display_info
458: 
459:     display_info(
460:         env=env,
461:         scr_folder=str(SCR_PATH),
462:         branch=args.branch,
463:         lang=args.lang,
464:         fork=args.fork
465:     )
466: 
467: if __name__ == '__main__':
468:     asyncio.run(main_async())
```

## File: LICENSE
```
  1: GNU GENERAL PUBLIC LICENSE
  2:                        Version 3, 29 June 2007
  3: 
  4:  Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
  5:  Everyone is permitted to copy and distribute verbatim copies
  6:  of this license document, but changing it is not allowed.
  7: 
  8:                             Preamble
  9: 
 10:   The GNU General Public License is a free, copyleft license for
 11: software and other kinds of works.
 12: 
 13:   The licenses for most software and other practical works are designed
 14: to take away your freedom to share and change the works.  By contrast,
 15: the GNU General Public License is intended to guarantee your freedom to
 16: share and change all versions of a program--to make sure it remains free
 17: software for all its users.  We, the Free Software Foundation, use the
 18: GNU General Public License for most of our software; it applies also to
 19: any other work released this way by its authors.  You can apply it to
 20: your programs, too.
 21: 
 22:   When we speak of free software, we are referring to freedom, not
 23: price.  Our General Public Licenses are designed to make sure that you
 24: have the freedom to distribute copies of free software (and charge for
 25: them if you wish), that you receive source code or can get it if you
 26: want it, that you can change the software or use pieces of it in new
 27: free programs, and that you know you can do these things.
 28: 
 29:   To protect your rights, we need to prevent others from denying you
 30: these rights or asking you to surrender the rights.  Therefore, you have
 31: certain responsibilities if you distribute copies of the software, or if
 32: you modify it: responsibilities to respect the freedom of others.
 33: 
 34:   For example, if you distribute copies of such a program, whether
 35: gratis or for a fee, you must pass on to the recipients the same
 36: freedoms that you received.  You must make sure that they, too, receive
 37: or can get the source code.  And you must show them these terms so they
 38: know their rights.
 39: 
 40:   Developers that use the GNU GPL protect your rights with two steps:
 41: (1) assert copyright on the software, and (2) offer you this License
 42: giving you legal permission to copy, distribute and/or modify it.
 43: 
 44:   For the developers' and authors' protection, the GPL clearly explains
 45: that there is no warranty for this free software.  For both users' and
 46: authors' sake, the GPL requires that modified versions be marked as
 47: changed, so that their problems will not be attributed erroneously to
 48: authors of previous versions.
 49: 
 50:   Some devices are designed to deny users access to install or run
 51: modified versions of the software inside them, although the manufacturer
 52: can do so.  This is fundamentally incompatible with the aim of
 53: protecting users' freedom to change the software.  The systematic
 54: pattern of such abuse occurs in the area of products for individuals to
 55: use, which is precisely where it is most unacceptable.  Therefore, we
 56: have designed this version of the GPL to prohibit the practice for those
 57: products.  If such problems arise substantially in other domains, we
 58: stand ready to extend this provision to those domains in future versions
 59: of the GPL, as needed to protect the freedom of users.
 60: 
 61:   Finally, every program is threatened constantly by software patents.
 62: States should not allow patents to restrict development and use of
 63: software on general-purpose computers, but in those that do, we wish to
 64: avoid the special danger that patents applied to a free program could
 65: make it effectively proprietary.  To prevent this, the GPL assures that
 66: patents cannot be used to render the program non-free.
 67: 
 68:   The precise terms and conditions for copying, distribution and
 69: modification follow.
 70: 
 71:                        TERMS AND CONDITIONS
 72: 
 73:   0. Definitions.
 74: 
 75:   "This License" refers to version 3 of the GNU General Public License.
 76: 
 77:   "Copyright" also means copyright-like laws that apply to other kinds of
 78: works, such as semiconductor masks.
 79: 
 80:   "The Program" refers to any copyrightable work licensed under this
 81: License.  Each licensee is addressed as "you".  "Licensees" and
 82: "recipients" may be individuals or organizations.
 83: 
 84:   To "modify" a work means to copy from or adapt all or part of the work
 85: in a fashion requiring copyright permission, other than the making of an
 86: exact copy.  The resulting work is called a "modified version" of the
 87: earlier work or a work "based on" the earlier work.
 88: 
 89:   A "covered work" means either the unmodified Program or a work based
 90: on the Program.
 91: 
 92:   To "propagate" a work means to do anything with it that, without
 93: permission, would make you directly or secondarily liable for
 94: infringement under applicable copyright law, except executing it on a
 95: computer or modifying a private copy.  Propagation includes copying,
 96: distribution (with or without modification), making available to the
 97: public, and in some countries other activities as well.
 98: 
 99:   To "convey" a work means any kind of propagation that enables other
100: parties to make or receive copies.  Mere interaction with a user through
101: a computer network, with no transfer of a copy, is not conveying.
102: 
103:   An interactive user interface displays "Appropriate Legal Notices"
104: to the extent that it includes a convenient and prominently visible
105: feature that (1) displays an appropriate copyright notice, and (2)
106: tells the user that there is no warranty for the work (except to the
107: extent that warranties are provided), that licensees may convey the
108: work under this License, and how to view a copy of this License.  If
109: the interface presents a list of user commands or options, such as a
110: menu, a prominent item in the list meets this criterion.
111: 
112:   1. Source Code.
113: 
114:   The "source code" for a work means the preferred form of the work
115: for making modifications to it.  "Object code" means any non-source
116: form of a work.
117: 
118:   A "Standard Interface" means an interface that either is an official
119: standard defined by a recognized standards body, or, in the case of
120: interfaces specified for a particular programming language, one that
121: is widely used among developers working in that language.
122: 
123:   The "System Libraries" of an executable work include anything, other
124: than the work as a whole, that (a) is included in the normal form of
125: packaging a Major Component, but which is not part of that Major
126: Component, and (b) serves only to enable use of the work with that
127: Major Component, or to implement a Standard Interface for which an
128: implementation is available to the public in source code form.  A
129: "Major Component", in this context, means a major essential component
130: (kernel, window system, and so on) of the specific operating system
131: (if any) on which the executable work runs, or a compiler used to
132: produce the work, or an object code interpreter used to run it.
133: 
134:   The "Corresponding Source" for a work in object code form means all
135: the source code needed to generate, install, and (for an executable
136: work) run the object code and to modify the work, including scripts to
137: control those activities.  However, it does not include the work's
138: System Libraries, or general-purpose tools or generally available free
139: programs which are used unmodified in performing those activities but
140: which are not part of the work.  For example, Corresponding Source
141: includes interface definition files associated with source files for
142: the work, and the source code for shared libraries and dynamically
143: linked subprograms that the work is specifically designed to require,
144: such as by intimate data communication or control flow between those
145: subprograms and other parts of the work.
146: 
147:   The Corresponding Source need not include anything that users
148: can regenerate automatically from other parts of the Corresponding
149: Source.
150: 
151:   The Corresponding Source for a work in source code form is that
152: same work.
153: 
154:   2. Basic Permissions.
155: 
156:   All rights granted under this License are granted for the term of
157: copyright on the Program, and are irrevocable provided the stated
158: conditions are met.  This License explicitly affirms your unlimited
159: permission to run the unmodified Program.  The output from running a
160: covered work is covered by this License only if the output, given its
161: content, constitutes a covered work.  This License acknowledges your
162: rights of fair use or other equivalent, as provided by copyright law.
163: 
164:   You may make, run and propagate covered works that you do not
165: convey, without conditions so long as your license otherwise remains
166: in force.  You may convey covered works to others for the sole purpose
167: of having them make modifications exclusively for you, or provide you
168: with facilities for running those works, provided that you comply with
169: the terms of this License in conveying all material for which you do
170: not control copyright.  Those thus making or running the covered works
171: for you must do so exclusively on your behalf, under your direction
172: and control, on terms that prohibit them from making any copies of
173: your copyrighted material outside their relationship with you.
174: 
175:   Conveying under any other circumstances is permitted solely under
176: the conditions stated below.  Sublicensing is not allowed; section 10
177: makes it unnecessary.
178: 
179:   3. Protecting Users' Legal Rights From Anti-Circumvention Law.
180: 
181:   No covered work shall be deemed part of an effective technological
182: measure under any applicable law fulfilling obligations under article
183: 11 of the WIPO copyright treaty adopted on 20 December 1996, or
184: similar laws prohibiting or restricting circumvention of such
185: measures.
186: 
187:   When you convey a covered work, you waive any legal power to forbid
188: circumvention of technological measures to the extent such circumvention
189: is effected by exercising rights under this License with respect to
190: the covered work, and you disclaim any intention to limit operation or
191: modification of the work as a means of enforcing, against the work's
192: users, your or third parties' legal rights to forbid circumvention of
193: technological measures.
194: 
195:   4. Conveying Verbatim Copies.
196: 
197:   You may convey verbatim copies of the Program's source code as you
198: receive it, in any medium, provided that you conspicuously and
199: appropriately publish on each copy an appropriate copyright notice;
200: keep intact all notices stating that this License and any
201: non-permissive terms added in accord with section 7 apply to the code;
202: keep intact all notices of the absence of any warranty; and give all
203: recipients a copy of this License along with the Program.
204: 
205:   You may charge any price or no price for each copy that you convey,
206: and you may offer support or warranty protection for a fee.
207: 
208:   5. Conveying Modified Source Versions.
209: 
210:   You may convey a work based on the Program, or the modifications to
211: produce it from the Program, in the form of source code under the
212: terms of section 4, provided that you also meet all of these conditions:
213: 
214:     a) The work must carry prominent notices stating that you modified
215:     it, and giving a relevant date.
216: 
217:     b) The work must carry prominent notices stating that it is
218:     released under this License and any conditions added under section
219:     7.  This requirement modifies the requirement in section 4 to
220:     "keep intact all notices".
221: 
222:     c) You must license the entire work, as a whole, under this
223:     License to anyone who comes into possession of a copy.  This
224:     License will therefore apply, along with any applicable section 7
225:     additional terms, to the whole of the work, and all its parts,
226:     regardless of how they are packaged.  This License gives no
227:     permission to license the work in any other way, but it does not
228:     invalidate such permission if you have separately received it.
229: 
230:     d) If the work has interactive user interfaces, each must display
231:     Appropriate Legal Notices; however, if the Program has interactive
232:     interfaces that do not display Appropriate Legal Notices, your
233:     work need not make them do so.
234: 
235:   A compilation of a covered work with other separate and independent
236: works, which are not by their nature extensions of the covered work,
237: and which are not combined with it such as to form a larger program,
238: in or on a volume of a storage or distribution medium, is called an
239: "aggregate" if the compilation and its resulting copyright are not
240: used to limit the access or legal rights of the compilation's users
241: beyond what the individual works permit.  Inclusion of a covered work
242: in an aggregate does not cause this License to apply to the other
243: parts of the aggregate.
244: 
245:   6. Conveying Non-Source Forms.
246: 
247:   You may convey a covered work in object code form under the terms
248: of sections 4 and 5, provided that you also convey the
249: machine-readable Corresponding Source under the terms of this License,
250: in one of these ways:
251: 
252:     a) Convey the object code in, or embodied in, a physical product
253:     (including a physical distribution medium), accompanied by the
254:     Corresponding Source fixed on a durable physical medium
255:     customarily used for software interchange.
256: 
257:     b) Convey the object code in, or embodied in, a physical product
258:     (including a physical distribution medium), accompanied by a
259:     written offer, valid for at least three years and valid for as
260:     long as you offer spare parts or customer support for that product
261:     model, to give anyone who possesses the object code either (1) a
262:     copy of the Corresponding Source for all the software in the
263:     product that is covered by this License, on a durable physical
264:     medium customarily used for software interchange, for a price no
265:     more than your reasonable cost of physically performing this
266:     conveying of source, or (2) access to copy the
267:     Corresponding Source from a network server at no charge.
268: 
269:     c) Convey individual copies of the object code with a copy of the
270:     written offer to provide the Corresponding Source.  This
271:     alternative is allowed only occasionally and noncommercially, and
272:     only if you received the object code with such an offer, in accord
273:     with subsection 6b.
274: 
275:     d) Convey the object code by offering access from a designated
276:     place (gratis or for a charge), and offer equivalent access to the
277:     Corresponding Source in the same way through the same place at no
278:     further charge.  You need not require recipients to copy the
279:     Corresponding Source along with the object code.  If the place to
280:     copy the object code is a network server, the Corresponding Source
281:     may be on a different server (operated by you or a third party)
282:     that supports equivalent copying facilities, provided you maintain
283:     clear directions next to the object code saying where to find the
284:     Corresponding Source.  Regardless of what server hosts the
285:     Corresponding Source, you remain obligated to ensure that it is
286:     available for as long as needed to satisfy these requirements.
287: 
288:     e) Convey the object code using peer-to-peer transmission, provided
289:     you inform other peers where the object code and Corresponding
290:     Source of the work are being offered to the general public at no
291:     charge under subsection 6d.
292: 
293:   A separable portion of the object code, whose source code is excluded
294: from the Corresponding Source as a System Library, need not be
295: included in conveying the object code work.
296: 
297:   A "User Product" is either (1) a "consumer product", which means any
298: tangible personal property which is normally used for personal, family,
299: or household purposes, or (2) anything designed or sold for incorporation
300: into a dwelling.  In determining whether a product is a consumer product,
301: doubtful cases shall be resolved in favor of coverage.  For a particular
302: product received by a particular user, "normally used" refers to a
303: typical or common use of that class of product, regardless of the status
304: of the particular user or of the way in which the particular user
305: actually uses, or expects or is expected to use, the product.  A product
306: is a consumer product regardless of whether the product has substantial
307: commercial, industrial or non-consumer uses, unless such uses represent
308: the only significant mode of use of the product.
309: 
310:   "Installation Information" for a User Product means any methods,
311: procedures, authorization keys, or other information required to install
312: and execute modified versions of a covered work in that User Product from
313: a modified version of its Corresponding Source.  The information must
314: suffice to ensure that the continued functioning of the modified object
315: code is in no case prevented or interfered with solely because
316: modification has been made.
317: 
318:   If you convey an object code work under this section in, or with, or
319: specifically for use in, a User Product, and the conveying occurs as
320: part of a transaction in which the right of possession and use of the
321: User Product is transferred to the recipient in perpetuity or for a
322: fixed term (regardless of how the transaction is characterized), the
323: Corresponding Source conveyed under this section must be accompanied
324: by the Installation Information.  But this requirement does not apply
325: if neither you nor any third party retains the ability to install
326: modified object code on the User Product (for example, the work has
327: been installed in ROM).
328: 
329:   The requirement to provide Installation Information does not include a
330: requirement to continue to provide support service, warranty, or updates
331: for a work that has been modified or installed by the recipient, or for
332: the User Product in which it has been modified or installed.  Access to a
333: network may be denied when the modification itself materially and
334: adversely affects the operation of the network or violates the rules and
335: protocols for communication across the network.
336: 
337:   Corresponding Source conveyed, and Installation Information provided,
338: in accord with this section must be in a format that is publicly
339: documented (and with an implementation available to the public in
340: source code form), and must require no special password or key for
341: unpacking, reading or copying.
342: 
343:   7. Additional Terms.
344: 
345:   "Additional permissions" are terms that supplement the terms of this
346: License by making exceptions from one or more of its conditions.
347: Additional permissions that are applicable to the entire Program shall
348: be treated as though they were included in this License, to the extent
349: that they are valid under applicable law.  If additional permissions
350: apply only to part of the Program, that part may be used separately
351: under those permissions, but the entire Program remains governed by
352: this License without regard to the additional permissions.
353: 
354:   When you convey a copy of a covered work, you may at your option
355: remove any additional permissions from that copy, or from any part of
356: it.  (Additional permissions may be written to require their own
357: removal in certain cases when you modify the work.)  You may place
358: additional permissions on material, added by you to a covered work,
359: for which you have or can give appropriate copyright permission.
360: 
361:   Notwithstanding any other provision of this License, for material you
362: add to a covered work, you may (if authorized by the copyright holders of
363: that material) supplement the terms of this License with terms:
364: 
365:     a) Disclaiming warranty or limiting liability differently from the
366:     terms of sections 15 and 16 of this License; or
367: 
368:     b) Requiring preservation of specified reasonable legal notices or
369:     author attributions in that material or in the Appropriate Legal
370:     Notices displayed by works containing it; or
371: 
372:     c) Prohibiting misrepresentation of the origin of that material, or
373:     requiring that modified versions of such material be marked in
374:     reasonable ways as different from the original version; or
375: 
376:     d) Limiting the use for publicity purposes of names of licensors or
377:     authors of the material; or
378: 
379:     e) Declining to grant rights under trademark law for use of some
380:     trade names, trademarks, or service marks; or
381: 
382:     f) Requiring indemnification of licensors and authors of that
383:     material by anyone who conveys the material (or modified versions of
384:     it) with contractual assumptions of liability to the recipient, for
385:     any liability that these contractual assumptions directly impose on
386:     those licensors and authors.
387: 
388:   All other non-permissive additional terms are considered "further
389: restrictions" within the meaning of section 10.  If the Program as you
390: received it, or any part of it, contains a notice stating that it is
391: governed by this License along with a term that is a further
392: restriction, you may remove that term.  If a license document contains
393: a further restriction but permits relicensing or conveying under this
394: License, you may add to a covered work material governed by the terms
395: of that license document, provided that the further restriction does
396: not survive such relicensing or conveying.
397: 
398:   If you add terms to a covered work in accord with this section, you
399: must place, in the relevant source files, a statement of the
400: additional terms that apply to those files, or a notice indicating
401: where to find the applicable terms.
402: 
403:   Additional terms, permissive or non-permissive, may be stated in the
404: form of a separately written license, or stated as exceptions;
405: the above requirements apply either way.
406: 
407:   8. Termination.
408: 
409:   You may not propagate or modify a covered work except as expressly
410: provided under this License.  Any attempt otherwise to propagate or
411: modify it is void, and will automatically terminate your rights under
412: this License (including any patent licenses granted under the third
413: paragraph of section 11).
414: 
415:   However, if you cease all violation of this License, then your
416: license from a particular copyright holder is reinstated (a)
417: provisionally, unless and until the copyright holder explicitly and
418: finally terminates your license, and (b) permanently, if the copyright
419: holder fails to notify you of the violation by some reasonable means
420: prior to 60 days after the cessation.
421: 
422:   Moreover, your license from a particular copyright holder is
423: reinstated permanently if the copyright holder notifies you of the
424: violation by some reasonable means, this is the first time you have
425: received notice of violation of this License (for any work) from that
426: copyright holder, and you cure the violation prior to 30 days after
427: your receipt of the notice.
428: 
429:   Termination of your rights under this section does not terminate the
430: licenses of parties who have received copies or rights from you under
431: this License.  If your rights have been terminated and not permanently
432: reinstated, you do not qualify to receive new licenses for the same
433: material under section 10.
434: 
435:   9. Acceptance Not Required for Having Copies.
436: 
437:   You are not required to accept this License in order to receive or
438: run a copy of the Program.  Ancillary propagation of a covered work
439: occurring solely as a consequence of using peer-to-peer transmission
440: to receive a copy likewise does not require acceptance.  However,
441: nothing other than this License grants you permission to propagate or
442: modify any covered work.  These actions infringe copyright if you do
443: not accept this License.  Therefore, by modifying or propagating a
444: covered work, you indicate your acceptance of this License to do so.
445: 
446:   10. Automatic Licensing of Downstream Recipients.
447: 
448:   Each time you convey a covered work, the recipient automatically
449: receives a license from the original licensors, to run, modify and
450: propagate that work, subject to this License.  You are not responsible
451: for enforcing compliance by third parties with this License.
452: 
453:   An "entity transaction" is a transaction transferring control of an
454: organization, or substantially all assets of one, or subdividing an
455: organization, or merging organizations.  If propagation of a covered
456: work results from an entity transaction, each party to that
457: transaction who receives a copy of the work also receives whatever
458: licenses to the work the party's predecessor in interest had or could
459: give under the previous paragraph, plus a right to possession of the
460: Corresponding Source of the work from the predecessor in interest, if
461: the predecessor has it or can get it with reasonable efforts.
462: 
463:   You may not impose any further restrictions on the exercise of the
464: rights granted or affirmed under this License.  For example, you may
465: not impose a license fee, royalty, or other charge for exercise of
466: rights granted under this License, and you may not initiate litigation
467: (including a cross-claim or counterclaim in a lawsuit) alleging that
468: any patent claim is infringed by making, using, selling, offering for
469: sale, or importing the Program or any portion of it.
470: 
471:   11. Patents.
472: 
473:   A "contributor" is a copyright holder who authorizes use under this
474: License of the Program or a work on which the Program is based.  The
475: work thus licensed is called the contributor's "contributor version".
476: 
477:   A contributor's "essential patent claims" are all patent claims
478: owned or controlled by the contributor, whether already acquired or
479: hereafter acquired, that would be infringed by some manner, permitted
480: by this License, of making, using, or selling its contributor version,
481: but do not include claims that would be infringed only as a
482: consequence of further modification of the contributor version.  For
483: purposes of this definition, "control" includes the right to grant
484: patent sublicenses in a manner consistent with the requirements of
485: this License.
486: 
487:   Each contributor grants you a non-exclusive, worldwide, royalty-free
488: patent license under the contributor's essential patent claims, to
489: make, use, sell, offer for sale, import and otherwise run, modify and
490: propagate the contents of its contributor version.
491: 
492:   In the following three paragraphs, a "patent license" is any express
493: agreement or commitment, however denominated, not to enforce a patent
494: (such as an express permission to practice a patent or covenant not to
495: sue for patent infringement).  To "grant" such a patent license to a
496: party means to make such an agreement or commitment not to enforce a
497: patent against the party.
498: 
499:   If you convey a covered work, knowingly relying on a patent license,
500: and the Corresponding Source of the work is not available for anyone
501: to copy, free of charge and under the terms of this License, through a
502: publicly available network server or other readily accessible means,
503: then you must either (1) cause the Corresponding Source to be so
504: available, or (2) arrange to deprive yourself of the benefit of the
505: patent license for this particular work, or (3) arrange, in a manner
506: consistent with the requirements of this License, to extend the patent
507: license to downstream recipients.  "Knowingly relying" means you have
508: actual knowledge that, but for the patent license, your conveying the
509: covered work in a country, or your recipient's use of the covered work
510: in a country, would infringe one or more identifiable patents in that
511: country that you have reason to believe are valid.
512: 
513:   If, pursuant to or in connection with a single transaction or
514: arrangement, you convey, or propagate by procuring conveyance of, a
515: covered work, and grant a patent license to some of the parties
516: receiving the covered work authorizing them to use, propagate, modify
517: or convey a specific copy of the covered work, then the patent license
518: you grant is automatically extended to all recipients of the covered
519: work and works based on it.
520: 
521:   A patent license is "discriminatory" if it does not include within
522: the scope of its coverage, prohibits the exercise of, or is
523: conditioned on the non-exercise of one or more of the rights that are
524: specifically granted under this License.  You may not convey a covered
525: work if you are a party to an arrangement with a third party that is
526: in the business of distributing software, under which you make payment
527: to the third party based on the extent of your activity of conveying
528: the work, and under which the third party grants, to any of the
529: parties who would receive the covered work from you, a discriminatory
530: patent license (a) in connection with copies of the covered work
531: conveyed by you (or copies made from those copies), or (b) primarily
532: for and in connection with specific products or compilations that
533: contain the covered work, unless you entered into that arrangement,
534: or that patent license was granted, prior to 28 March 2007.
535: 
536:   Nothing in this License shall be construed as excluding or limiting
537: any implied license or other defenses to infringement that may
538: otherwise be available to you under applicable patent law.
539: 
540:   12. No Surrender of Others' Freedom.
541: 
542:   If conditions are imposed on you (whether by court order, agreement or
543: otherwise) that contradict the conditions of this License, they do not
544: excuse you from the conditions of this License.  If you cannot convey a
545: covered work so as to satisfy simultaneously your obligations under this
546: License and any other pertinent obligations, then as a consequence you may
547: not convey it at all.  For example, if you agree to terms that obligate you
548: to collect a royalty for further conveying from those to whom you convey
549: the Program, the only way you could satisfy both those terms and this
550: License would be to refrain entirely from conveying the Program.
551: 
552:   13. Use with the GNU Affero General Public License.
553: 
554:   Notwithstanding any other provision of this License, you have
555: permission to link or combine any covered work with a work licensed
556: under version 3 of the GNU Affero General Public License into a single
557: combined work, and to convey the resulting work.  The terms of this
558: License will continue to apply to the part which is the covered work,
559: but the special requirements of the GNU Affero General Public License,
560: section 13, concerning interaction through a network will apply to the
561: combination as such.
562: 
563:   14. Revised Versions of this License.
564: 
565:   The Free Software Foundation may publish revised and/or new versions of
566: the GNU General Public License from time to time.  Such new versions will
567: be similar in spirit to the present version, but may differ in detail to
568: address new problems or concerns.
569: 
570:   Each version is given a distinguishing version number.  If the
571: Program specifies that a certain numbered version of the GNU General
572: Public License "or any later version" applies to it, you have the
573: option of following the terms and conditions either of that numbered
574: version or of any later version published by the Free Software
575: Foundation.  If the Program does not specify a version number of the
576: GNU General Public License, you may choose any version ever published
577: by the Free Software Foundation.
578: 
579:   If the Program specifies that a proxy can decide which future
580: versions of the GNU General Public License can be used, that proxy's
581: public statement of acceptance of a version permanently authorizes you
582: to choose that version for the Program.
583: 
584:   Later license versions may give you additional or different
585: permissions.  However, no additional obligations are imposed on any
586: author or copyright holder as a result of your choosing to follow a
587: later version.
588: 
589:   15. Disclaimer of Warranty.
590: 
591:   THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
592: APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
593: HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
594: OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
595: THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
596: PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
597: IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
598: ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
599: 
600:   16. Limitation of Liability.
601: 
602:   IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
603: WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
604: THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
605: GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
606: USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
607: DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
608: PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
609: EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
610: SUCH DAMAGES.
611: 
612:   17. Interpretation of Sections 15 and 16.
613: 
614:   If the disclaimer of warranty and limitation of liability provided
615: above cannot be given local legal effect according to their terms,
616: reviewing courts shall apply local law that most closely approximates
617: an absolute waiver of all civil liability in connection with the
618: Program, unless a warranty or assumption of liability accompanies a
619: copy of the Program in return for a fee.
620: 
621:                      END OF TERMS AND CONDITIONS
622: 
623:             How to Apply These Terms to Your New Programs
624: 
625:   If you develop a new program, and you want it to be of the greatest
626: possible use to the public, the best way to achieve this is to make it
627: free software which everyone can redistribute and change under these terms.
628: 
629:   To do so, attach the following notices to the program.  It is safest
630: to attach them to the start of each source file to most effectively
631: state the exclusion of warranty; and each file should have at least
632: the "copyright" line and a pointer to where the full notice is found.
633: 
634:     <one line to give the program's name and a brief idea of what it does.>
635:     Copyright (C) <year>  <name of author>
636: 
637:     This program is free software: you can redistribute it and/or modify
638:     it under the terms of the GNU General Public License as published by
639:     the Free Software Foundation, either version 3 of the License, or
640:     (at your option) any later version.
641: 
642:     This program is distributed in the hope that it will be useful,
643:     but WITHOUT ANY WARRANTY; without even the implied warranty of
644:     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
645:     GNU General Public License for more details.
646: 
647:     You should have received a copy of the GNU General Public License
648:     along with this program.  If not, see <https://www.gnu.org/licenses/>.
649: 
650: Also add information on how to contact you by electronic and paper mail.
651: 
652:   If the program does terminal interaction, make it output a short
653: notice like this when it starts in an interactive mode:
654: 
655:     <program>  Copyright (C) <year>  <name of author>
656:     This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
657:     This is free software, and you are welcome to redistribute it
658:     under certain conditions; type `show c' for details.
659: 
660: The hypothetical commands `show w' and `show c' should show the appropriate
661: parts of the General Public License.  Of course, your program's commands
662: might be different; for a GUI interface, you would use an "about box".
663: 
664:   You should also get your employer (if you work as a programmer) or school,
665: if any, to sign a "copyright disclaimer" for the program, if necessary.
666: For more information on this, and how to apply and follow the GNU GPL, see
667: <https://www.gnu.org/licenses/>.
668: 
669:   The GNU General Public License does not permit incorporating your program
670: into proprietary programs.  If your program is a subroutine library, you
671: may consider it more useful to permit linking proprietary applications with
672: the library.  If this is what you want to do, use the GNU Lesser General
673: Public License instead of this License.  But first, please read
674: <https://www.gnu.org/licenses/why-not-lgpl.html>.
```

## File: lightning_installer_complete.py
```python
  1: #!/usr/bin/env python3
  2: """
  3: Comprehensive Lightning AI Installation Script for sdAIgen
  4: This script completely patches ALL platform-specific errors in the original sdAIgen repository.
  5: This corrected version fixes bugs in the original patching logic to ensure valid Python code is generated.
  6: """
  7: 
  8: import os
  9: import sys
 10: import json
 11: import shutil
 12: import subprocess
 13: from pathlib import Path
 14: import urllib.request
 15: import re
 16: 
 17: def detect_lightning_ai():
 18:     """Detect if running on Lightning AI"""
 19:     indicators = [
 20:         os.environ.get('LIGHTNING_CLOUD_PROJECT_ID'),
 21:         os.environ.get('LIGHTNING_AI'),
 22:         os.path.exists('/teamspace'),
 23:         'lightning' in os.environ.get('PWD', '').lower(),
 24:         'lightning' in str(Path.home()).lower(),
 25:         'studios' in os.environ.get('PWD', '').lower()
 26:     ]
 27:     return any(indicators)
 28: 
 29: def setup_lightning_directories():
 30:     """Set up Lightning AI directory structure"""
 31:     base_path = Path.cwd() / 'sdAIgen_workspace'
 32:     
 33:     directories = {
 34:         'base': base_path,
 35:         'scripts': base_path / 'ANXETY' / 'scripts',
 36:         'models': base_path / 'models',
 37:         'outputs': base_path / 'outputs',
 38:         'extensions': base_path / 'extensions',
 39:         'embeddings': base_path / 'embeddings',
 40:         'lora': base_path / 'lora',
 41:         'vae': base_path / 'vae',
 42:         'controlnet': base_path / 'controlnet',
 43:         'config': base_path / 'config',
 44:         'logs': base_path / 'logs',
 45:         'temp': base_path / 'temp',
 46:         'cache': base_path / '.cache'
 47:     }
 48:     
 49:     # Clean slate: remove old directory if it exists
 50:     if base_path.exists():
 51:         print(f"🧹 Removing old directory to ensure a clean installation: {base_path}")
 52:         shutil.rmtree(base_path)
 53: 
 54:     for name, path in directories.items():
 55:         path.mkdir(parents=True, exist_ok=True)
 56:     print(f"✅ Created all directories in: {base_path}")
 57:     
 58:     return directories
 59: 
 60: def create_comprehensive_setup_patches(base_path_str):
 61:     """Create comprehensive patches for setup.py"""
 62:     return [
 63:         {
 64:             'type': 'replace_function',
 65:             'function_name': 'environment_setup',
 66:             'old_pattern': r'def environment_setup\(\):.*?(?=def|\Z)',
 67:             'new_content': f'''def environment_setup():
 68:     """Universal environment setup for all platforms"""
 69:     import os
 70:     from pathlib import Path
 71:     
 72:     # This setup is now hardcoded for the patched Lightning environment
 73:     platform = 'lightning'
 74:     os.environ['DETECTED_PLATFORM'] = platform
 75:     print(f"🔍 Detected platform: {{platform}}")
 76:     
 77:     base_path = Path('{base_path_str}')
 78:     
 79:     dirs_to_create = [
 80:         base_path / 'models', base_path / 'outputs', base_path / 'extensions',
 81:         base_path / 'embeddings', base_path / 'lora', base_path / 'vae',
 82:         base_path / 'controlnet', base_path / 'config', base_path / 'logs',
 83:         base_path / 'temp', base_path / '.cache'
 84:     ]
 85:     for directory in dirs_to_create:
 86:         directory.mkdir(parents=True, exist_ok=True)
 87:     
 88:     os.environ['HOME'] = str(base_path)
 89:     os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'
 90:     os.environ['TMPDIR'] = str(base_path / 'temp')
 91:     
 92:     return str(base_path)
 93: '''
 94:         },
 95:         {
 96:             'type': 'replace',
 97:             'old': 'HOME = Path.home()',
 98:             'new': f"HOME = Path('{base_path_str}')"
 99:         },
100:         { 'type': 'replace', 'old': "'/content/", 'new': "str(HOME) + '/" },
101:         { 'type': 'replace', 'old': '"/content/', 'new': 'str(HOME) + "/' },
102:     ]
103: 
104: def create_comprehensive_launch_patches(dirs):
105:     """Create comprehensive patches for launch.py"""
106:     return [
107:         {
108:             'type': 'insert_after',
109:             'search': 'import os',
110:             'insert': f'''
111: # Universal platform detection and optimization
112: os.environ['DETECTED_PLATFORM'] = 'lightning'
113: os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'
114: print("⚡ Applied Lightning AI optimizations")
115: 
116: PLATFORM_ARGS = [
117:     '--xformers', '--no-half-vae', '--opt-split-attention', '--medvram',
118:     '--disable-console-progressbars', '--api', '--cors-allow-origins=*',
119:     '--listen', '--port=8080', '--ckpt-dir={dirs["models"]}',
120:     '--embeddings-dir={dirs["embeddings"]}', '--lora-dir={dirs["lora"]}',
121:     '--vae-dir={dirs["vae"]}'
122: ]
123: '''
124:         },
125:         {
126:             'type': 'replace',
127:             'old': "args = ['--share']",
128:             'new': "args = PLATFORM_ARGS"
129:         }
130:     ]
131: 
132: def apply_patches(file_path, patches):
133:     if not file_path.exists():
134:         print(f"⚠️ File not found, cannot patch: {file_path}")
135:         return False
136:     try:
137:         content = file_path.read_text(encoding='utf-8')
138:         original_content = content
139:         for patch in patches:
140:             if patch['type'] == 'replace':
141:                 content = content.replace(patch['old'], patch['new'])
142:             elif patch['type'] == 'insert_after':
143:                 content = content.replace(patch['search'], patch['search'] + '\\n' + patch['insert'], 1)
144:             elif patch['type'] == 'replace_function':
145:                 content = re.sub(patch['old_pattern'], patch['new_content'], content, flags=re.DOTALL)
146:         if content != original_content:
147:             file_path.write_text(content, encoding='utf-8')
148:             print(f"🔧 Successfully patched: {file_path.name}")
149:         else:
150:             print(f"ℹ️ No changes needed for: {file_path.name}")
151:         return True
152:     except Exception as e:
153:         print(f"❌ Failed to patch {file_path}: {e}")
154:         return False
155: 
156: def download_and_patch_script(url, local_path, patches):
157:     try:
158:         print(f"📥 Downloading: {local_path.name}")
159:         urllib.request.urlretrieve(url, local_path)
160:         print(f"  ✅ Downloaded to: {local_path}")
161:         if patches:
162:             apply_patches(local_path, patches)
163:         return True
164:     except Exception as e:
165:         print(f"❌ Failed to download/patch {url}: {e}")
166:         return False
167: 
168: def main():
169:     print("🚀 Starting sdAIgen Installation and Patching Process...")
170:     if not detect_lightning_ai():
171:         print("⚠️ WARNING: This script is optimized for a Lightning AI environment.")
172:     
173:     directories = setup_lightning_directories()
174:     base_path_str = str(directories['base'])
175: 
176:     print("\\n📦 Installing requirements...")
177:     try:
178:         subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', 
179:                         'torch', 'torchvision', 'xformers', 'diffusers', 'transformers', 
180:                         'accelerate', 'safetensors', 'opencv-python-headless', 'pillow'], check=True)
181:         print("✅ Core requirements installed successfully.")
182:     except subprocess.CalledProcessError as e:
183:         print(f"❌ Failed to install Python packages: {e}")
184:         return
185: 
186:     print("\\n📥 Downloading and patching scripts...")
187:     base_url = "https://raw.githubusercontent.com/anxety-solo/sdAIgen/main/scripts"
188:     scripts_dir = directories['scripts']
189:     
190:     scripts_to_process = [
191:         {'url': f"{base_url}/setup.py", 'local_path': scripts_dir / 'setup.py', 'patches': create_comprehensive_setup_patches(base_path_str)},
192:         {'url': f"{base_url}/launch.py", 'local_path': scripts_dir / 'launch.py', 'patches': create_comprehensive_launch_patches(directories)}
193:     ]
194:     
195:     success_count = sum(1 for script in scripts_to_process if download_and_patch_script(**script))
196:     
197:     if success_count != len(scripts_to_process):
198:         print("\\n❌ Not all scripts could be downloaded or patched. Aborting.")
199:         return
200: 
201:     print("\\n🚀 Creating launcher script...")
202:     launcher_script_path = directories['base'] / 'start_sdaigen.py'
203:     
204:     # *** THIS IS THE CORRECTED LAUNCHER CONTENT ***
205:     launcher_content = f'''#!/usr/bin/env python3
206: import sys
207: import os
208: import asyncio
209: from pathlib import Path
210: 
211: print("🚀 Launching sdAIgen...")
212: 
213: scripts_dir = Path("{scripts_dir}")
214: sys.path.insert(0, str(scripts_dir))
215: 
216: setup_script = scripts_dir / 'setup.py'
217: 
218: if not setup_script.exists():
219:     print(f"❌ Critical error: Cannot find setup.py at {{setup_script}}")
220:     sys.exit(1)
221: 
222: # Execute the patched setup script which will then handle the launch
223: try:
224:     # Import the setup module
225:     import setup
226:     
227:     # The original script uses an async main function. We must find and run it.
228:     if hasattr(setup, 'main_async'):
229:         # Explicitly run its main asynchronous function
230:         # This bypasses the '__name__ == "__main__"' guard in setup.py
231:         print("   Found main_async function. Starting application...")
232:         asyncio.run(setup.main_async())
233:     else:
234:         print("❌ Critical error: Could not find the 'main_async' function in the setup script.")
235:         sys.exit(1)
236:         
237: except Exception as e:
238:     import traceback
239:     print(f"❌ An error occurred while launching sdAIgen: {{e}}")
240:     traceback.print_exc()
241:     print("   Please check the logs and ensure all files are correctly patched.")
242:     sys.exit(1)
243: '''
244:     launcher_script_path.write_text(launcher_content)
245:     launcher_script_path.chmod(0o755)
246: 
247:     print("\\n" + "="*60)
248:     print("🎉 INSTALLATION COMPLETE!")
249:     print("="*60)
250:     print(f"📁 All files installed in: {directories['base']}")
251:     print(f"\\nTo start the application, run the following command in a new cell:")
252:     print(f"\\033[1m%run {launcher_script_path}\\033[0m")
253:     print("\\n✨ The script has been corrected and patched to run in this environment.")
254: 
255: if __name__ == "__main__":
256:     main()
```

## File: README-ru-RU.md
```markdown
 1: <div align="center">
 2: <img width="1080px" height="auto" src="https://raw.githubusercontent.com/anxety-solo/sdAIgen/main/.Docs/Imgs/sample.png"/></br>
 3: <h1>~ ANXETY | Stable Diffusion WebUI | NoteBook V2 ~</h1>
 4: 
 5: [English](README.md) | Русский
 6: 
 7: </div>
 8: 
 9: <div align="center">
10:     <a href="https://discord.gg/eemJdDusvH">
11:         <img src=".Docs/SVG/ru/discord-ru.svg" width="800" height="130" alt="discord">
12:     </a>
13:     <a href="https://colab.research.google.com/github/anxety-solo/sdAIgen/blob/main/notebook/ANXETY_sdAIgen_RU.ipynb">
14:         <img src=".Docs/SVG/ru/colab-ru.svg" width="800" height="160" alt="colab">
15:     </a>
16:     <a href="https://www.kaggle.com/code/anxetysolo/sdaigen-ru-ipynb">
17:         <img src=".Docs/SVG/ru/kaggle-ru.svg" width="800" height="160" alt="kaggle">
18:     </a>
19:     <h6>Дополнительные сведения о виджетах см. в разделе <a href="https://github.com/anxety-solo/sdAIgen/wiki/Widgets-ru-RU">WiKi</a>.</h6>
20: </div>
21: 
22: ## 🌟 Особенности:
23:   - Мультиплатформенный блокнот: **Google Colab, Kaggle.**
24:   - *Виджеты* для простого взаимодействия.
25:   - Предустановленные пользовательские: *Настройки* + *Стили* + [*UI Тема*](https://github.com/anxety-solo/anxety-theme)
26:   - Скачивание превью для *моделей, LoRa и embedding* (CivitAi) | ***Для Kaggle есть ограничения.***
27:   - Выбор WebUI между *A1111*, *ComfyUI*, *Forge*, *Classic (Forge)*, *ReForge*, *SD-UX.*
28: 
29: <details>
30: <summary>📚 Установленные Расширения</summary>
31: 
32: | ✔️ — Установленно | ❌ — Не установлено | 🔄 — Интегрированная версия | <sup>`†`</sup> — Только в *Kaggle* |
33: |----------------|---------------------|-------------------------|----------------------------------|
34: 
35: | Extension | A1111 | Forge | Classic | ReForge | SD-UX |
36: |-----------|-------|-------|---------|---------|-------|
37: | [adetailer](https://github.com/Bing-su/adetailer) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
38: | [anxety-theme](https://github.com/anxety-solo/anxety-theme) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
39: | [Aspect-Ratio-Helper](https://github.com/thomasasfk/sd-webui-aspect-ratio-helper) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
40: | [CivitAi-Browser-plus](https://github.com/anxety-solo/sd-civitai-browser-plus) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
41: | [ControlNet](https://github.com/Mikubill/sd-webui-controlnet) | ✔️ | 🔄 | 🔄 | 🔄 | ✔️ |
42: | [Encrypt-Image](https://github.com/gutris1/sd-encrypt-image) | ✔️<sup>†</sup> | ✔️<sup>†</sup> | ✔️<sup>†</sup> | ✔️<sup>†</sup> | ✔️<sup>†</sup> |
43: | [Image-Info](https://github.com/gutris1/sd-image-info) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
44: | [Image-Viewer](https://github.com/gutris1/sd-image-viewer) | ✔️ | ✔️ | ❌ | ✔️ | ✔️ |
45: | [Infinite-Image-Browsing](https://github.com/zanllp/sd-webui-infinite-image-browsing) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
46: | [Regional-Prompter](https://github.com/hako-mikan/sd-webui-regional-prompter) | ✔️ | ❌ | ❌ | ✔️ | ✔️ |
47: | [SD-Couple](https://github.com/Haoming02/sd-forge-couple) | ❌ | ✔️ | ✔️ | ❌ | ❌ |
48: | [SD-Hub](https://github.com/gutris1/sd-hub) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
49: | [State](https://github.com/ilian6806/stable-diffusion-webui-state) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
50: | [SuperMerger](https://github.com/hako-mikan/sd-webui-supermerger) | ✔️ | ✔️ | ❌ | ✔️ | ✔️ |
51: | [Tag-Complete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
52: | [Umi-AI-Wildcards](https://github.com/Tsukreya/Umi-AI-Wildcards) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
53: | [WD14-Tagger](https://github.com/picobyte/stable-diffusion-webui-wd14-tagger) | ✔️ | ✔️ | ❌ | ✔️ | ✔️ |
54: | [webui_timer](https://github.com/anxety-solo/webui_timer) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
55: 
56: </details>
57: 
58: <details>
59: <summary>🧩 Установленные Кастомные-Ноды | ComfyUI</summary>
60: 
61: - [Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
62: - [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
63: - [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
64: - [ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)
65: - [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
66: - [ComfyUI-Model-Manager](https://github.com/hayden-fr/ComfyUI-Model-Manager)
67: - [ControlNet-AUX](https://github.com/Fannovel16/comfyui_controlnet_aux)
68: - [Efficiency-Nodes](https://github.com/jags111/efficiency-nodes-comfyui)
69: - [UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)
70: - [WAS-Nodes](https://github.com/WASasquatch/was-node-suite-comfyui)
71: - [WD14-Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger)
72: 
73: </details>
74: 
75: ## 💙 Поддержать:
76: 
77: <div align="center">
78:     <a href="https://www.donationalerts.com/r/anxety">
79:         <img src=".Docs/SVG/DA_Logo_Color.svg" width="250" height="100" alt="DonationAlerts">
80:     </a>
81:     <a href="https://boosty.to/anxety/single-payment/donation/707920">
82:         <img src=".Docs/SVG/Boosty_Logo_Color.svg" width="250" height="100" alt="Boosty">
83:     </a>
84: </div>
85: 
86: <div align="center">
87: 	<h6>Некоторые скрипты взяты у <a href="https://github.com/gutris1">gutris1</a>.</h6>
88: </div>
```

## File: Readme.md
```markdown
 1: # **\~ ANXETY | Stable Diffusion WebUI | NoteBook V2 \~**
 2: 
 3: English | [Русский](http://docs.google.com/README-ru-RU.md)
 4: 
 5: ## **🌟 Features:**
 6: 
 7: * Multiplatform notebook: *Google Colab, Kaggle.*  
 8: * *Widgets* for easy interaction.  
 9: * Preset custom: *Settings* \+ *Styles* \+ [*UI Theme*](https://github.com/anxety-solo/anxety-theme)  
10: * Download previews for *models, LoRa and embedding* (CivitAi) | ***There are limitations for Kaggle.***  
11: * Choosing WebUI between *A1111*, *ComfyUI*, *Forge*, *Classic (Forge)*, *ReForge*, *SD-UX.*
12: 
13: | ✔️ — Installed | ❌ — Not Installed | 🔄 — Integrated Version | † — Only in Kaggle |
14: | :---- | :---- | :---- | :---- |
15: 
16: | Extension | A1111 | Forge | Classic | ReForge | SD-UX |
17: | :---- | :---- | :---- | :---- | :---- | :---- |
18: | [adetailer](https://github.com/Bing-su/adetailer) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
19: | [anxety-theme](https://github.com/anxety-solo/anxety-theme) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
20: | [Aspect-Ratio-Helper](https://github.com/thomasasfk/sd-webui-aspect-ratio-helper) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
21: | [CivitAi-Browser-plus](https://github.com/anxety-solo/sd-civitai-browser-plus) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
22: | [ControlNet](https://github.com/Mikubill/sd-webui-controlnet) | ✔️ | 🔄 | 🔄 | 🔄 | ✔️ |
23: | [Encrypt-Image](https://github.com/gutris1/sd-encrypt-image) | ✔️† | ✔️† | ✔️† | ✔️† | ✔️† |
24: | [Image-Info](https://github.com/gutris1/sd-image-info) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
25: | [Image-Viewer](https://github.com/gutris1/sd-image-viewer) | ✔️ | ❌ | ❌ | ✔️ | ✔️ |
26: | [Infinite-Image-Browsing](https://github.com/zanllp/sd-webui-infinite-image-browsing) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
27: | [Regional-Prompter](https://github.com/hako-mikan/sd-webui-regional-prompter) | ✔️ | ❌ | ❌ | ✔️ | ✔️ |
28: | [SD-Couple](https://github.com/Haoming02/sd-forge-couple) | ❌ | ✔️ | ✔️ | ❌ | ❌ |
29: | [SD-Hub](https://github.com/gutris1/sd-hub) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
30: | [State](https://github.com/ilian6806/stable-diffusion-webui-state) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
31: | [SuperMerger](https://github.com/hako-mikan/sd-webui-supermerger) | ✔️ | ✔️ | ❌ | ✔️ | ✔️ |
32: | [Tag-Complete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
33: | [Umi-AI-Wildcards](https://github.com/Tsukreya/Umi-AI-Wildcards) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
34: | [WD14-Tagger](https://github.com/picobyte/stable-diffusion-webui-wd14-tagger) | ✔️ | ✔️ | ❌ | ✔️ | ✔️ |
35: | [webui\_timer](https://github.com/anxety-solo/webui_timer) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
36: 
37: * [Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)  
38: * [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)  
39: * [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)  
40: * [ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)  
41: * [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)  
42: * [ComfyUI-Model-Manager](https://github.com/hayden-fr/ComfyUI-Model-Manager)  
43: * [ControlNet-AUX](https://github.com/Fannovel16/comfyui_controlnet_aux)  
44: * [Efficiency-Nodes](https://github.com/jags111/efficiency-nodes-comfyui)  
45: * [UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)  
46: * [WAS-Nodes](https://github.com/WASasquatch/was-node-suite-comfyui)  
47: * [WD14-Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger)
48: 
49: ## **💙 Support:**
```

## File: README.md
```markdown
 1: <div align="center">
 2: <img width="1080px" height="auto" src="https://raw.githubusercontent.com/anxety-solo/sdAIgen/main/.Docs/Imgs/sample.png"/></br>
 3: <h1>~ ANXETY | Stable Diffusion WebUI | NoteBook V2 ~</h1>
 4: 
 5: English | [Русский](README-ru-RU.md)
 6: 
 7: </div>
 8: 
 9: <div align="center">
10:     <a href="https://discord.gg/eemJdDusvH">
11:         <img src=".Docs/SVG/en/discord-en.svg" width="800" height="130" alt="discord">
12:     </a>
13:     <a href="https://colab.research.google.com/github/anxety-solo/sdAIgen/blob/main/notebook/ANXETY_sdAIgen_EN.ipynb">
14:         <img src=".Docs/SVG/en/colab-en.svg" width="800" height="160" alt="colab">
15:     </a>
16:     <a href="https://www.kaggle.com/code/anxetysolo/sdaigen-en-ipynb">
17:         <img src=".Docs/SVG/en/kaggle-en.svg" width="800" height="160" alt="kaggle">
18:     </a>
19:     <h6>For more information about widgets, see <a href="https://github.com/anxety-solo/sdAIgen/wiki/Widgets">WiKi</a>.</h6>
20: </div>
21: 
22: ## 🌟 Features:
23:   - Multiplatform notebook: *Google Colab, Kaggle.*
24:   - *Widgets* for easy interaction.
25:   - Preset custom: *Settings* + *Styles* + [*UI Theme*](https://github.com/anxety-solo/anxety-theme)
26:   - Download previews for *models, LoRa and embedding* (CivitAi) | ***There are limitations for Kaggle.***
27:   - Choosing WebUI between *A1111*, *ComfyUI*, *Forge*, *Classic (Forge)*, *ReForge*, *SD-UX.*
28: 
29: <details>
30: <summary>📚 Installed Extensions</summary>
31: 
32: | ✔️ — Installed | ❌ — Not Installed | 🔄 — Integrated Version | <sup>`†`</sup> — Only in *Kaggle* |
33: |----------------|---------------------|-------------------------|----------------------------------|
34: 
35: | Extension | A1111 | Forge | Classic | ReForge | SD-UX |
36: |-----------|-------|-------|---------|---------|-------|
37: | [adetailer](https://github.com/Bing-su/adetailer) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
38: | [anxety-theme](https://github.com/anxety-solo/anxety-theme) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
39: | [Aspect-Ratio-Helper](https://github.com/thomasasfk/sd-webui-aspect-ratio-helper) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
40: | [CivitAi-Browser-plus](https://github.com/anxety-solo/sd-civitai-browser-plus) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
41: | [ControlNet](https://github.com/Mikubill/sd-webui-controlnet) | ✔️ | 🔄 | 🔄 | 🔄 | ✔️ |
42: | [Encrypt-Image](https://github.com/gutris1/sd-encrypt-image) | ✔️<sup>†</sup> | ✔️<sup>†</sup> | ✔️<sup>†</sup> | ✔️<sup>†</sup> | ✔️<sup>†</sup> |
43: | [Image-Info](https://github.com/gutris1/sd-image-info) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
44: | [Image-Viewer](https://github.com/gutris1/sd-image-viewer) | ✔️ | ✔️ | ❌ | ✔️ | ✔️ |
45: | [Infinite-Image-Browsing](https://github.com/zanllp/sd-webui-infinite-image-browsing) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
46: | [Regional-Prompter](https://github.com/hako-mikan/sd-webui-regional-prompter) | ✔️ | ❌ | ❌ | ✔️ | ✔️ |
47: | [SD-Couple](https://github.com/Haoming02/sd-forge-couple) | ❌ | ✔️ | ✔️ | ❌ | ❌ |
48: | [SD-Hub](https://github.com/gutris1/sd-hub) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
49: | [State](https://github.com/ilian6806/stable-diffusion-webui-state) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
50: | [SuperMerger](https://github.com/hako-mikan/sd-webui-supermerger) | ✔️ | ✔️ | ❌ | ✔️ | ✔️ |
51: | [Tag-Complete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
52: | [Umi-AI-Wildcards](https://github.com/Tsukreya/Umi-AI-Wildcards) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
53: | [WD14-Tagger](https://github.com/picobyte/stable-diffusion-webui-wd14-tagger) | ✔️ | ✔️ | ❌ | ✔️ | ✔️ |
54: | [webui_timer](https://github.com/anxety-solo/webui_timer) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
55: 
56: </details>
57: 
58: <details>
59: <summary>🧩 Installed Custom-Nodes | ComfyUI</summary>
60: 
61: - [Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
62: - [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
63: - [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
64: - [ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)
65: - [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
66: - [ComfyUI-Model-Manager](https://github.com/hayden-fr/ComfyUI-Model-Manager)
67: - [ControlNet-AUX](https://github.com/Fannovel16/comfyui_controlnet_aux)
68: - [Efficiency-Nodes](https://github.com/jags111/efficiency-nodes-comfyui)
69: - [UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)
70: - [WAS-Nodes](https://github.com/WASasquatch/was-node-suite-comfyui)
71: - [WD14-Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger)
72: 
73: </details>
74: 
75: ## 💙 Support:
76: 
77: <div align="center">
78:     <a href="https://www.donationalerts.com/r/anxety">
79:         <img src=".Docs/SVG/DA_Logo_Color.svg" width="250" height="100" alt="DonationAlerts">
80:     </a>
81:     <a href="https://boosty.to/anxety/single-payment/donation/707920">
82:         <img src=".Docs/SVG/Boosty_Logo_Color.svg" width="250" height="100" alt="Boosty">
83:     </a>
84: </div>
85: 
86: <div align="center">
87: 	<h6>Some scripts are taken from <a href="https://github.com/gutris1">gutris1</a>.</h6>
88: </div>
```
