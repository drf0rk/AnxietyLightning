This file is a merged representation of the entire codebase, combined into a single document by Repomix.
The content has been processed where line numbers have been added, content has been formatted for parsing in markdown style, security check has been disabled.

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
- Content has been formatted for parsing in markdown style
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
  Comprehensive Project Guide_.md
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
  1: # ~ WebUI Utils Module | by ANXETY ~ (Final Correction for TypeError)
  2: 
  3: import json_utils as js
  4: from pathlib import Path
  5: import os
  6: import sys
  7: import json
  8: 
  9: def _get_project_home():
 10:     """Determines the correct project HOME based on the runtime environment."""
 11:     if 'google.colab' in sys.modules:
 12:         return Path('/content')
 13:     if os.path.exists('/kaggle'):
 14:         return Path('/kaggle/working')
 15:     if os.environ.get('LIGHTNING_AI') or os.path.exists('/teamspace'):
 16:         base_path = Path('/teamspace/studios/this_studio')
 17:         if not base_path.exists():
 18:             base_path = Path.home() / 'workspace'
 19:         return base_path
 20:     return Path.cwd()
 21: 
 22: # Define paths dynamically and correctly when the module is loaded
 23: HOME = _get_project_home()
 24: SCR_PATH = HOME / 'ANXETY'
 25: SETTINGS_PATH = SCR_PATH / 'settings.json'
 26: SHARED_MODEL_BASE = HOME / 'sd_models_shared'
 27: 
 28: 
 29: WEBUI_PATHS = {
 30:     'A1111': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs'),
 31:     'ComfyUI': ('checkpoints', 'vae', 'loras', 'embeddings', 'custom_nodes', 'upscale_models', 'output'),
 32:     'Classic': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'output'),
 33:     'Forge': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs'),
 34:     'ReForge': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs'),
 35:     'SD-UX': ('Stable-diffusion', 'VAE', 'Lora', 'embeddings', 'extensions', 'ESRGAN', 'outputs')
 36: }
 37: DEFAULT_UI = 'Forge'
 38: 
 39: def update_current_webui(current_value):
 40:     """Update the current WebUI value and save settings."""
 41:     _set_webui_paths(current_value)
 42: 
 43: def _set_webui_paths(ui):
 44:     """Configure paths for specified UI, pointing to the shared model base."""
 45:     selected_ui = ui if ui in WEBUI_PATHS else DEFAULT_UI
 46:     webui_root = HOME / selected_ui
 47:     
 48:     models_root = SHARED_MODEL_BASE 
 49:     models_root.mkdir(parents=True, exist_ok=True)
 50: 
 51:     is_comfy = selected_ui == 'ComfyUI'
 52:     
 53:     paths = WEBUI_PATHS.get(selected_ui, WEBUI_PATHS[DEFAULT_UI])
 54:     checkpoint_subdir, vae_subdir, lora_subdir, embed_subdir, extension_subdir, upscale_subdir, output_subdir = paths
 55: 
 56:     path_config = {
 57:         'current': ui,
 58:         'webui_path': str(webui_root),
 59:         'model_dir': str(models_root / ('checkpoints' if is_comfy else 'Stable-diffusion')),
 60:         'vae_dir': str(models_root / 'vae'),
 61:         'lora_dir': str(models_root / ('loras' if is_comfy else 'Lora')),
 62:         'embed_dir': str(models_root / 'embeddings'),
 63:         'control_dir': str(models_root / ('controlnet' if is_comfy else 'ControlNet')),
 64:         'upscale_dir': str(models_root / ('upscale_models' if is_comfy else 'ESRGAN')),
 65:         'adetailer_dir': str(models_root / 'adetailer'),
 66:         'clip_dir': str(models_root / 'clip'),
 67:         'unet_dir': str(models_root / 'unet'),
 68:         'vision_dir': str(models_root / 'clip_vision'),
 69:         'encoder_dir': str(models_root / ('text_encoders' if is_comfy else 'text_encoder')),
 70:         'diffusion_dir': str(models_root / 'diffusion_models'),
 71:         'extension_dir': str(webui_root / extension_subdir),
 72:         'output_dir': str(webui_root / output_subdir),
 73:         'config_dir': str(webui_root / ('user/default' if is_comfy else ''))
 74:     }
 75: 
 76:     # Ensure all shared directories exist
 77:     for key, path_str in path_config.items():
 78:         if '_dir' in key and not any(x in key for x in ['extension', 'output', 'config']):
 79:             Path(path_str).mkdir(parents=True, exist_ok=True)
 80:             
 81:     # --- THIS IS THE FIX ---
 82:     # The js.read function is called with only one argument, as it doesn't accept keyword arguments.
 83:     # It already returns an empty dict {} by default if the file is missing or empty.
 84:     all_settings = js.read(SETTINGS_PATH)
 85:     if not isinstance(all_settings, dict): # Safety check
 86:         all_settings = {}
 87:         
 88:     all_settings['WEBUI'] = path_config
 89:     with open(SETTINGS_PATH, 'w') as f:
 90:         json.dump(all_settings, f, indent=4)
 91: 
 92: 
 93: def handle_setup_timer(webui_path, timer_webui):
 94:     """Manage timer persistence for WebUI instances."""
 95:     timer_file = Path(webui_path) / 'static' / 'timer.txt'
 96:     timer_file.parent.mkdir(parents=True, exist_ok=True)
 97:     try:
 98:         with timer_file.open('r') as f:
 99:             timer_webui = float(f.read())
100:     except (FileNotFoundError, ValueError):
101:         pass
102:     with timer_file.open('w') as f:
103:         f.write(str(timer_webui))
104:     return timer_webui
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

## File: Notebook/Comprehensive Project Guide_.md
```markdown
   1: **AnxietyLightning: A Technical Guide for** **AI Agent Integration **
   2: 
   3: **1. Introduction **
   4: 
   5: **1.1. Purpose of this Guide **
   6: 
   7: This document provides an exhaustive technical blueprint of the drf0rk/AnxietyLightning project, specifical y tailored for consumption by Artificial Intel igence \(AI\) agents. The primary objective is to equip AI agents with the necessary knowledge to understand the system's architecture, file structures, script interactions, data formats, and operational workflows. This understanding is intended to enable them to perform automated tasks such as asset population, management, and verification within the drf0rk/AnxietyLightning ecosystem. The level of detail provided, particularly concerning file formats and script interactions, supports a paradigm where AI agents can transition from being mere users to active maintainers or configurators of such complex software environments. 
   8: 
   9: **1.2. Project Overview: drf0rk/AnxietyLightning** drf0rk/AnxietyLightning is an advanced Jupyter notebook-based solution engineered for the management of Stable Diffusion Web User Interfaces \(UIs\) and their associated digital assets. 
  10: 
  11: It is particularly optimized for deployment within cloud computing environments such as lightning.ai.1 The project is an adaptation of the anxety-solo/sdAlgen project, inheriting its foundational functionalities while extending them with specific integrations tailored for cloud platforms and enhancing operations through a graphical user interface \(GUI\).1 
  12: 
  13: The system is designed to streamline and automate the download and management of a diverse range of assets essential for Stable Diffusion workflows. These assets include various model types \(e.g., SD 1.5, SDXL, FLUX\), Low-Rank Adaptations \(LoRAs\), Variational Autoencoders \(VAEs\), ControlNets, WebUI extensions, and other supplementary resources.1 
  14: 
  15: The project's design heavily considers the operational characteristics of cloud environments, emphasizing efficiency and automation to manage resources effectively, especial y in contexts where compute instances may be ephemeral. 
  16: 
  17: **1.3. Core Capabilities for AI-Driven Automation** The drf0rk/AnxietyLightning system presents several core capabilities that make it amenable to AI-driven automation: 
  18: 
  19: ● **Programmatic Asset Management**: The system al ows for the programmatic addition and management of models, VAEs, LoRAs, ControlNets, and other assets. This can be achieved either through the direct modification of structured data definition files or by generating specific commands to invoke the download machinery.1 
  20: 
  21: ● **Automated Download Orchestration**: It features an automated download orchestration mechanism capable of retrieving assets from various public and private repositories, including Hugging Face, Civitai, and GitHub.1 
  22: 
  23: ● **Structured File System Interaction**: The project operates with a wel -defined file system structure for asset storage and retrieval. A key aspect of this is the utilization of a shared model base, which centralizes assets for efficient access and management.1 
  24: 
  25: These capabilities are facilitated by clear entry points within the system's architecture for programmatic interaction, rendering it wel -suited for control and automation by AI agents. 
  26: 
  27: The design explicitly caters to AI interaction by outlining specific files and command formats for programmatic asset population.1 
  28: 
  29: **1.4. Acknowledgment of Original Repository: **
  30: 
  31: **https://github.com/anxety-solo/sdAIgen **
  32: 
  33: This guide acknowledges that the drf0rk/AnxietyLightning project is derived from and builds upon the foundational work established by the anxety-solo/sdAIgen repository.1 AI agents referencing this document should be cognizant that certain core concepts, architectural patterns, or behavioral nuances within drf0rk/AnxietyLightning may have originated from anxety-solo/sdAIgen. This lineage is particularly relevant when troubleshooting complex issues or seeking a deeper understanding of fundamental system behaviors, as the original repository may offer additional context or clarification. This acknowledgment serves to ensure traceability and provide a broader contextual understanding, which can be invaluable if the documentation for drf0rk/AnxietyLightning is incomplete for a specific edge case or if an observed issue appears to be rooted in the system's fundamental design. 
  34: 
  35: **2. System Architecture and Data Flow **
  36: 
  37: **2.1. High-Level Architectural Blueprint **
  38: 
  39: The drf0rk/AnxietyLightning system operates primarily within a Jupyter Notebook environment. This environment serves as the orchestrator for a suite of Python scripts designed to manage Stable Diffusion WebUI environments and their associated assets.1 The architecture is modular, with distinct components responsible for data definition, user interface widget generation, download orchestration, core download and file management, external API interactions \(e.g., Civitai\), and file system path management.1 
  40: 
  41: A critical architectural feature is the utilization of a centralized shared storage system. This system is employed for storing models, LoRAs, VAEs, and other large resources. Such centralization is paramount for ensuring data persistence and operational efficiency, particularly in cloud environments where compute sessions can be transient.1 This modularity, which separates concerns like data definition from download logic and UI presentation, is advantageous for AI agents, as it al ows for targeted interaction with specific, wel -defined components of the system. 
  42: 
  43: **2.2. Key Software Components and Their Interdependencies** The system comprises several key software components, each with specific roles and interdependencies. The execution order, typical y enforced by the main Jupyter notebook, dictates a predictable lifecycle that an AI agent must respect for successful interaction. 
  44: 
  45: ● **ANXETY\_sdAlgen\_EN.ipynb \(or similar language variant\)**: This Jupyter Notebook is the primary orchestrator. It executes other Python scripts in a defined sequence using the %run magic command.1 
  46: 
  47: ● **scripts/setup.py**: This script is responsible for initializing the notebook environment. Its tasks include downloading al core project files \(including other scripts and modules\) from the designated drf0rk/AnxietyLightning GitHub fork and setting up platform-aware paths, which are saved to a settings.json file.1 For an AI agent, it is crucial to understand that any modifications to other scripts or data files must be present in the GitHub fork from which setup.py pul s its sources. 
  48: 
  49: ● **scripts/\_\*-data.py files \(e.g., \_models-data.py, \_loras-data.py,** **\_xl-models-data.py\)**: These Python files contain dictionaries that define lists of models, LoRAs, VAEs, and ControlNets, specifying their download URLs and desired local filenames. They serve as the primary data source for populating interactive widgets.1 These files represent a primary interaction point for AI agents wishing to add new predefined assets to the system. 
  50: 
  51: ● **scripts/widgets-en.py \(or similar language variant\)**: This script reads the data definition files \(the \_\*-data.py files\) and dynamical y populates interactive dropdown menus and other widgets in the Jupyter Notebook interface. It notably uses exec\(\) to process the content of the \_\*-data.py files.1 
  52: 
  53: ● **scripts/downloading-en.py \(or similar language variant\)**: Based on user selections from the widgets \(or direct programmatic input\), this script orchestrates the download process. It constructs download commands, resolves URLs \(leveraging CivitaiAPI.py for Civitai links\), handles API interactions, and initiates file downloads.1 This script is a primary interaction point for AI agents seeking to trigger custom or programmatic downloads. 
  54: 
  55: ● **modules/Manager.py**: This module provides the core, underlying functions for downloading files from various sources \(Hugging Face, Civitai, Google Drive, GitHub\) using tools like aria2c, gdown, curl, and git clone. It also performs basic file operations.1 
  56: 
  57: ● **modules/CivitaiAPI.py**: This module specifical y handles interactions with the Civitai platform. Its responsibilities include resolving Civitai model page URLs to direct download links and fetching associated metadata, such as preview images.1 
  58: 
  59: ● **modules/webui\_utils.py**: This utility centralizes the definition and management of file system paths. Critical y, it defines the SHARED\_MODEL\_BASE path, which points al model-related assets to a shared storage location, and populates settings.json with these paths.1 
  60: 
  61: ● **scripts/launch.py**: This script is responsible for configuring and launching the selected Stable Diffusion WebUI, ensuring that it correctly points to the model directories 
  62: 
  63: established by webui\_utils.py.1 
  64: 
  65: The sequential execution \(setup.py → widgets-en.py → downloading-en.py → launch.py\) implies inherent dependencies. For instance, setup.py must complete successful y to ensure al other scripts are available and paths are configured. Any AI-driven modifications to data definition files \(\_\*-data.py\) or other scripts must be committed and pushed to the source GitHub fork *before* setup.py is executed in the target environment; otherwise, the AI's changes may be overwritten or ignored when setup.py pul s the project files. 
  66: 
  67: **2.3. Data Flow for Asset Population and Management** The process of populating and managing assets within drf0rk/AnxietyLightning fol ows a wel -defined data flow: 
  68: 
  69: 1. **Data Definition**: Asset metadata, including download URLs and target filenames, is initial y defined within Python dictionaries in the \_\*-data.py files \(e.g., \_models-data.py\).1 
  70: 
  71: 2. **Widget Population**: The scripts/widgets-en.py script reads these \_\*-data.py files. It executes their content \(using exec\(\)\) to load the dictionaries and then uses this data to dynamical y populate dropdown menus and other interactive widgets within the Jupyter Notebook UI.1 
  72: 
  73: 3. **User Selection or Programmatic Input**: 
  74: 
  75: ○ A human user can interact with the UI, selecting desired assets from the populated widgets. 
  76: 
  77: ○ Alternatively, an AI agent can programmatical y set the values of these widget-associated Python variables before downloading-en.py is run.1 
  78: 
  79: ○ More directly, an AI agent can construct a special y formatted input string and provide it to scripts/downloading-en.py to trigger custom downloads, bypassing direct widget interaction.1 
  80: 
  81: 4. **Download Orchestration**: The scripts/downloading-en.py script takes the selections \(from widgets or programmatic settings\) or the direct input string. It then processes these instructions, resolves URLs \(using modules/CivitaiAPI.py for Civitai links if necessary\), and constructs the appropriate download commands.1 
  82: 
  83: 5. **Core Download Execution**: The modules/Manager.py script executes the actual download operations using underlying tools such as aria2c for direct downloads, gdown for Google Drive links, or git clone for extensions.1 
  84: 
  85: 6. **Asset Storage**: Downloaded files are saved to predefined destination paths. These paths are typical y subdirectories within the SHARED\_MODEL\_BASE \(for models, LoRAs, VAEs, etc.\) or within UI-specific extension directories. The path management logic is primarily handled by modules/webui\_utils.py, which writes resolved paths into settings.json for other scripts to use.1 
  86: 
  87: This system offers two principal pathways for an AI agent to initiate downloads: by simulating UI interaction through setting widget values \(which relies on prior modification of \_\*-data.py files if the asset is not already defined\), or by directly invoking the download engine \(downloading-en.py\) with a formatted command string. The latter method is general y more 
  88: 
  89: robust, flexible, and direct for automation purposes, as it bypasses the widgets-en.py layer and the exec\(\) parsing of \_\*-data.py files for the specific download instance, offering more immediate control. 
  90: 
  91: **3. File and Directory Structure for Programmatic** **Access **
  92: 
  93: **3.1. Root Directory Organization **
  94: 
  95: The primary operational context for an AI agent interacting with this system is the drfOrk/sdAlgenLightning/ repository structure. This repository is cloned into the Jupyter environment, typical y by the scripts/setup.py script during initialization.1 An AI agent must be capable of navigating this structure to locate scripts for execution, data files for modification \(e.g., \_\*-data.py\), and configuration files. While a general inferred structure is available 1, the structure detailed in the project's file documentation 1 is more pertinent for identifying AI agent interaction points related to asset population and download management. 
  96: 
  97: **3.2. Detailed Analysis of Critical Directories and Files** A precise understanding of the file and directory layout is essential for an AI agent. The fol owing table outlines critical paths within the repository and at runtime, their descriptions, and their relevance for AI agent interaction. The distinction between files within the cloned repository \(like scripts\) and runtime-generated paths \(like SHARED\_MODEL\_BASE\) is particularly important. SHARED\_MODEL\_BASE is a destination for downloaded assets, not a source location for project logic files, and is typical y established outside the repository clone to ensure persistence across sessions.1 
  98: 
  99: **Table 1: Critical File and Directory Reference **
 100: 
 101: ****
 102: 
 103: **Path \(within repo or Type **
 104: 
 105: **Description \(Source: Primary **
 106: 
 107: **runtime\) **
 108: 
 109: **\) **
 110: 
 111: **Function/Relevance **
 112: 
 113: **for AI Agent **
 114: 
 115: scripts/\_models-data.p File 
 116: 
 117: SD 1.5 model, VAE, 
 118: 
 119: Read/Write target for 
 120: 
 121: y 
 122: 
 123: ControlNet definitions defining new 
 124: 
 125: predefined models, 
 126: 
 127: VAEs, ControlNets to 
 128: 
 129: appear in UI widgets. 
 130: 
 131: scripts/\_loras-data.py File 
 132: 
 133: LORA model 
 134: 
 135: Read/Write target for 
 136: 
 137: definitions \(SD 1.5 and defining new 
 138: 
 139: SDXL\) 
 140: 
 141: predefined LoRAs to 
 142: 
 143: appear in UI widgets. 
 144: 
 145: scripts/\_xl-models-dat File 
 146: 
 147: SDXL model, VAE, 
 148: 
 149: Read/Write target for 
 150: 
 151: a.py 
 152: 
 153: ControlNet definitions defining new 
 154: 
 155: predefined SDXL 
 156: 
 157: models, VAEs, 
 158: 
 159: ControlNets to appear 
 160: 
 161: in UI widgets. 
 162: 
 163: scripts/setup.py 
 164: 
 165: File 
 166: 
 167: Initial setup, 
 168: 
 169: Orchestrates initial 
 170: 
 171: downloads project files environment setup; AI 
 172: 
 173: from fork 
 174: 
 175: must ensure its 
 176: 
 177: changes are in the fork 
 178: 
 179: this script pul s from. 
 180: 
 181: scripts/en/widgets-en. File 
 182: 
 183: Dynamical y populates Reads \_\*-data.py files 
 184: 
 185: py 
 186: 
 187: widgets from data files \(via exec\(\)\); AI may set 
 188: 
 189: associated Python 
 190: 
 191: variables to mimic UI 
 192: 
 193: selection. 
 194: 
 195: scripts/en/downloading File 
 196: 
 197: Orchestrates 
 198: 
 199: Primary target for 
 200: 
 201: -en.py 
 202: 
 203: downloads based on programmatic custom 
 204: 
 205: selections or direct 
 206: 
 207: download commands 
 208: 
 209: input 
 210: 
 211: via formatted strings 
 212: 
 213: \(e.g., 
 214: 
 215: prefix:URL\[filename.ext
 216: 
 217: \]\). 
 218: 
 219: modules/Manager.py File 
 220: 
 221: Core download 
 222: 
 223: Provides underlying 
 224: 
 225: functions \(aria2c, 
 226: 
 227: download 
 228: 
 229: gdown, curl, git clone\) mechanisms; AI 
 230: 
 231: interacts with it 
 232: 
 233: indirectly via 
 234: 
 235: downloading-en.py. 
 236: 
 237: modules/CivitaiAPI.py File 
 238: 
 239: Handles CivitAI URL 
 240: 
 241: Enables use of Civitai 
 242: 
 243: resolution and 
 244: 
 245: page URLs in 
 246: 
 247: metadata fetching 
 248: 
 249: download commands; 
 250: 
 251: AI interacts indirectly. 
 252: 
 253: modules/webui\_utils.py File 
 254: 
 255: Manages WebUI paths, Defines 
 256: 
 257: centralizes shared 
 258: 
 259: SHARED\_MODEL\_BASE 
 260: 
 261: model base 
 262: 
 263: and other critical 
 264: 
 265: paths, writing them to 
 266: 
 267: settings.json. AI needs 
 268: 
 269: to understand these 
 270: 
 271: output paths. 
 272: 
 273: SHARED\_MODEL\_BASE Dir 
 274: 
 275: Centralized shared 
 276: 
 277: Target destination for 
 278: 
 279: \(runtime path\) 
 280: 
 281: storage for models, 
 282: 
 283: most downloaded 
 284: 
 285: LoRAs, VAEs, etc. \(e.g., assets; location for AI 
 286: 
 287: HOME / 
 288: 
 289: to verify successful 
 290: 
 291: 'sd\_models\_shared'\) downloads. 
 292: 
 293: SHARED\_MODEL\_BASEDir 
 294: 
 295: Subdirectory for 
 296: 
 297: Specific destination for 
 298: 
 299: /Stable-diffusion 
 300: 
 301: checkpoint models 
 302: 
 303: assets downloaded 
 304: 
 305: \(runtime\) 
 306: 
 307: with the model: prefix. 
 308: 
 309: SHARED\_MODEL\_BASEDir 
 310: 
 311: Subdirectory for LoRA Specific destination for 
 312: 
 313: /loras \(runtime\) 
 314: 
 315: models 
 316: 
 317: assets downloaded 
 318: 
 319: with the lora: prefix. 
 320: 
 321: SHARED\_MODEL\_BASEDir 
 322: 
 323: Subdirectory for VAE Specific destination for 
 324: 
 325: /vae \(runtime\) 
 326: 
 327: models 
 328: 
 329: assets downloaded 
 330: 
 331: with the vae: prefix. 
 332: 
 333: UI\_SPECIFIC\_PATH/ext Dir 
 334: 
 335: Subdirectory for 
 336: 
 337: Specific destination for 
 338: 
 339: ensions \(runtime\) 
 340: 
 341: WebUI extensions 
 342: 
 343: assets downloaded 
 344: 
 345: \(path varies by UI\) 
 346: 
 347: with the extension: 
 348: 
 349: prefix \(cloned Git 
 350: 
 351: repositories\). 
 352: 
 353: \_configs\_/ 
 354: 
 355: Dir 
 356: 
 357: Configuration files for Contains UI-specific 
 358: 
 359: different UIs and 
 360: 
 361: config.json, 
 362: 
 363: general settings 
 364: 
 365: ui-config.json, etc. AI 
 366: 
 367: might need to 
 368: 
 369: read/modify these for 
 370: 
 371: advanced 
 372: 
 373: configurations. 
 374: 
 375: notebook/ANXETY\_sdA File 
 376: 
 377: The main English 
 378: 
 379: Orchestrates the 
 380: 
 381: lgen\_EN.ipynb 
 382: 
 383: Jupyter Notebook 
 384: 
 385: execution of al scripts; 
 386: 
 387: AI may interact by 
 388: 
 389: triggering cel 
 390: 
 391: execution or 
 392: 
 393: replicating its logic. 
 394: 
 395: This structured reference al ows an AI agent to quickly identify the relevant files and directories for specific tasks, such as adding a new LoRA model \(by modifying scripts/\_loras-data.py for predefined options, or by commanding scripts/en/downloading-en.py for custom downloads\) and then verifying its presence in the SHARED\_MODEL\_BASE/loras directory. 
 396: 
 397: **4. Core Scripts and Module Interactions: A Deep Dive** **4.1. Environment Initialization and Project Deployment:** **scripts/setup.py **
 398: 
 399: The scripts/setup.py script serves as the foundational step in the operational workflow, executed first by the main Jupyter notebook.1 Its primary responsibilities include: 
 400: 
 401: ● Detecting the runtime platform \(e.g., Colab, Kaggle, Lightning AI, Local\) to tailor subsequent operations.1 
 402: 
 403: ● Downloading al core project files – including CSS, JavaScript, Python modules, and other scripts – from a specified GitHub fork \(e.g., drfOrk/sdAlgenLightning\) into the current runtime environment.1 This is a critical behavior: any AI-driven modifications to these project files must be committed and pushed to this source fork *prior* to the execution of setup.py to ensure the changes are deployed. Failure to do so may result in the AI's local or in-session changes being overwritten by the versions fetched from the fork, rendering the modifications ephemeral if setup.py is re-run \(e.g., after a kernel restart\). 
 404: 
 405: ● Establishing essential environment configurations, such as defining a SCR\_PATH 
 406: 
 407: variable \(pointing to the directory of the scripts\) and adding the SCR\_PATH/modules directory to the Python system path \(sys.path\), making the project's utility modules importable by other scripts.1 
 408: 
 409: ● Defining the SHARED\_MODEL\_BASE path \(the centralized directory for shared model assets\) and saving various platform-aware paths to a settings.json file. This file is subsequently read by other scripts \(like downloading-en.py\) to determine correct file locations.1 
 410: 
 411: The behavior of setup.py effectively creates a deployment mechanism. For AI agents, this implies that persistent modifications to the system's codebase or predefined asset lists require a workflow that includes updating the source GitHub repository. 
 412: 
 413: **4.2. Asset Data Definition: scripts/\_\*-data.py Files** Files such as \_models-data.py, \_loras-data.py, and \_xl-models-data.py are central to defining the predefined assets that appear in the UI's widget dropdowns.1 These files are essential y data stores formatted as Python code. 
 414: 
 415: **4.2.1. Structure and Syntax **
 416: 
 417: These files employ a standard Python dictionary structure.1 
 418: 
 419: ● **Top-Level Keys**: These are human-readable strings that serve as the display names in the UI dropdowns \(e.g., "1. Anime \(by XpucT\) \+ INP"\).1 
 420: 
 421: ● **Value \(List of Dictionaries\)**: Each top-level key maps to a Python list. Each element in this list is a dictionary, where every dictionary represents a single file to be downloaded as part of selecting the top-level option.1 
 422: 
 423: ● **Inner Dictionary Format**: Each inner dictionary must contain specific keys: 
 424: 
 425: ○ 'url' \(String\): This is the primary source URL for the asset. It can be a direct download link \(e.g., from Hugging Face ending in /resolve/main/... or a Civitai API link like https://civitai.com/api/download/models/...\), a Civitai model page URL 
 426: 
 427: \(e.g., 
 428: 
 429: https://civitai.com/models/MODEL\_ID?modelVersionId=MODEL\_VERSION\_ID\), or a Google Drive link. The system's CivitaiAPI.py module can resolve Civitai page URLs to direct download links.1 
 430: 
 431: ○ 'name' \(String, Optional but Highly Recommended\): This string specifies the exact filename \(including the correct extension like .safetensors, .ckpt, .pt, .yaml\) under 
 432: 
 433: which the asset should be saved on the local file system \(e.g., 
 434: 
 435: "Anime\_V2.safetensors"\).1 If omitted, the system attempts to derive a filename from the URL, or for Civitai page URLs, CivitaiAPI.py provides a default based on model metadata. For precise control, AI agents should always include the 'name' 
 436: 
 437: key. 
 438: 
 439: Example structure from \_models-data.py 1: 
 440: 
 441: 
 442: 
 443: Python 
 444: 
 445: 
 446: 
 447: 
 448: 
 449: \# scripts/\_models-data.py 
 450: 
 451: model\_list = \{ 
 452: 
 453: "1. Anime \(by XpucT\) \+ INP":, 
 454: 
 455: \#... more entries 
 456: 
 457: \} 
 458: 
 459: 
 460: 
 461: **4.2.2. Programmatic Modification Protocols for AI Agents** To add or modify predefined assets, an AI agent must interact with these \_\*-data.py files programmatical y: 
 462: 
 463: 1. **Read File Content**: Ingest the content of the target \_\*-data.py file. 
 464: 
 465: 2. **Parse Python Structure**: Parse the Python dictionary structure. While the system itself uses exec\(\) for loading, a safer approach for an AI modifying the file might involve ast.literal\_eval if the content can be guaranteed to be a literal structure. However, given the project's use of exec\(\), the AI must ensure the output is valid Python code. 
 466: 
 467: 3. **Add/Modify Data**: Add a new key-value pair to the main dictionary or modify an existing one, strictly adhering to the specified format. This includes ensuring URL 
 468: 
 469: validity and explicitly setting the 'name' with the correct file extension. 
 470: 
 471: 4. **Serialize and Overwrite**: Serialize the modified Python dictionary back into valid Python code \(a string representation of the dictionary\) and overwrite the original \_\*-data.py file.1 
 472: 
 473: Directly modifying Python code files carries inherent risks. An AI agent must implement robust error handling and syntax validation mechanisms to ensure it does not corrupt the \_\*-data.py files. A syntactical y incorrect file wil cause the exec\(\) cal in scripts/widgets-en.py to fail, thereby breaking the UI widget population process and potential y halting the workflow.1 
 474: 
 475: **4.3. UI Widget Population Logic: scripts/widgets-en.py** The scripts/widgets-en.py script is responsible for dynamical y generating the interactive widgets \(dropdowns, checkboxes, etc.\) that form the user interface within the Jupyter notebook.1 
 476: 
 477: **4.3.1. Data Ingestion from \_\*-data.py \(via read\_model\_data and exec\(\)\) **
 478: 
 479: The core mechanism for data ingestion is the read\_model\_data\(file\_path, data\_key\_in\_file, prefixes=\['none'\]\) function.1 
 480: 
 481: ● This function opens the specified \_\*-data.py file \(e.g., \_models-data.py\). 
 482: 
 483: ● Critical y, it then executes the entire content of this file as Python code using exec\(f.read\(\), \{\}, local\_vars\).1 This populates the local\_vars dictionary with the variables \(which are the asset dictionaries like model\_list\) defined within the data file. 
 484: 
 485: ● The data\_key\_in\_file argument al ows for specifying nested dictionary keys if the asset definitions are structured hierarchical y within the data file \(e.g., 'lora\_data.sd15\_loras' 
 486: 
 487: to access SD1.5 LoRAs within a larger lora\_data dictionary\).1 
 488: 
 489: ● The function processes local\_vars to extract the relevant dictionary and returns a list of its keys \(the human-readable names like "1. Anime \(by XpucT\) \+ INP"\), which are then used to populate the options in the UI dropdowns. 
 490: 
 491: The use of exec\(\) is a significant architectural choice. It means that the \_\*-data.py files are not merely static data configurations but are treated as executable Python scripts. While this provides flexibility, it also introduces a potential vulnerability: if an AI agent \(or any process\) modifying these files does not strictly adhere to the intended data dictionary format and instead introduces arbitrary Python commands, those commands would be executed when widgets-en.py processes the file. This underscores the necessity for AI agents to perform validated, secure modifications. 
 492: 
 493: The script also handles dynamic updates. For instance, an "SDXL models" checkbox \(XL\_models\_widget\) typical y has a cal back function \(update\_XL\_options\). When this checkbox's state changes, the cal back re-invokes read\_model\_data with different file paths or data keys to update the model, VAE, ControlNet, and LoRA widgets with options relevant to either SD 1.5 or SDXL assets.1 An AI agent intending to use SDXL assets must ensure this checkbox's state is appropriately set or understand that \_xl-models-data.py and specific keys within \_loras-data.py \(like sdxl\_loras\) contain the relevant SDXL entries. 
 494: 
 495: **4.4. Download Orchestration Engine: scripts/en/downloading-en.py** The scripts/en/downloading-en.py script is the central engine for orchestrating asset downloads. It processes inputs derived from UI widget selections or, crucial y for AI agents, from direct programmatic instructions.1 
 496: 
 497: **4.4.1. PREFIX\_MAP: Mapping Prefixes to Directories** A key component within downloading-en.py is the PREFIX\_MAP dictionary. This dictionary maps short textual prefixes \(e.g., 'model', 'lora', 'vae', 'extension'\) to their corresponding local directory path variables \(e.g., model\_dir, lora\_dir\) and an optional short-tag used in some UI modes.1 
 498: 
 499: These directory path variables \(model\_dir, lora\_dir, etc.\) are not hardcoded. Instead, their values are typical y read from the settings.json file, which is populated by modules/webui\_utils.py during the setup phase. For most asset types \(models, LoRAs, VAEs, etc.\), these paths resolve to specific subdirectories within the centralized SHARED\_MODEL\_BASE \(e.g., sd\_models\_shared/Stable-diffusion, sd\_models\_shared/loras\). 
 500: 
 501: Extensions, however, are general y saved into UI-specific extension folders \(e.g., A1111/extensions\).1 
 502: 
 503: Understanding this mapping is essential for an AI agent constructing programmatic download commands, as the prefix dictates the asset type and its ultimate storage location. 
 504: 
 505: **Table 2: PREFIX\_MAP Specification \(Illustrative\)** **Prefix Key \(from Associated **
 506: 
 507: **Resolves To **
 508: 
 509: **Short Tag \(if any\) Primary Asset **
 510: 
 511: **PREFIX\_MAP\) **
 512: 
 513: **Directory **
 514: 
 515: **\(Conceptual **
 516: 
 517: **Type **
 518: 
 519: **Variable \(e.g., **
 520: 
 521: **Path, e.g., **
 522: 
 523: **model\_dir\) **
 524: 
 525: **SHARED\_MODEL**
 526: 
 527: **\_BASE/Stable-dif**
 528: 
 529: **fusion\) **
 530: 
 531: 'model' 
 532: 
 533: model\_dir 
 534: 
 535: SHARED\_MODEL\_ '$ckpt' 
 536: 
 537: Checkpoint 
 538: 
 539: BASE/Stable-diffu
 540: 
 541: models 
 542: 
 543: sion 
 544: 
 545: 'vae' 
 546: 
 547: vae\_dir 
 548: 
 549: SHARED\_MODEL\_ '$vae' 
 550: 
 551: VAE models 
 552: 
 553: BASE/vae 
 554: 
 555: 'lora' 
 556: 
 557: lora\_dir 
 558: 
 559: SHARED\_MODEL\_ '$lora' 
 560: 
 561: LoRA models 
 562: 
 563: BASE/loras 
 564: 
 565: 'embed' 
 566: 
 567: embed\_dir 
 568: 
 569: SHARED\_MODEL\_ '$emb' 
 570: 
 571: Textual Inversion 
 572: 
 573: BASE/embeddings 
 574: 
 575: Embeds 
 576: 
 577: 'extension' 
 578: 
 579: extension\_dir 
 580: 
 581: UI\_SPECIFIC\_PAT '$ext' 
 582: 
 583: WebUI Extensions 
 584: 
 585: H/extensions 
 586: 
 587: \(Git\) 
 588: 
 589: 'control' 
 590: 
 591: control\_dir 
 592: 
 593: SHARED\_MODEL\_ '$cnet' 
 594: 
 595: ControlNet 
 596: 
 597: BASE/ControlNet 
 598: 
 599: models 
 600: 
 601: 'upscale' 
 602: 
 603: upscale\_dir 
 604: 
 605: SHARED\_MODEL\_ '$ups' 
 606: 
 607: Upscaler models 
 608: 
 609: BASE/ESRGAN \(or 
 610: 
 611: similar upscaler 
 612: 
 613: path\) 
 614: 
 615: *\(Note: Exact directory variables and short tags are based on the example in.1 The list may be* *more extensive in the actual script.\) *
 616: 
 617: **4.4.2. Input Formatting for download\(line\): Enabling Programmatic Downloads** The download\(line\) function within downloading-en.py is the primary entry point for initiating downloads. It processes a single string argument, line, which can contain one or more comma-separated download instructions.1 Two main formats are understood: 1. **Widget-Generated Format \(from handle\_submodels\)**: 
 618: 
 619: ○ **Syntax**: URL DESTINATION\_PATH FILENAME \(space-separated components\).1 
 620: 
 621: ○ **Example**: https://huggingface.co/XpucT/Anime/resolve/main/Anime\_v2.safetensors 
 622: 
 623: /root/sd\_models\_shared/Stable-diffusion Anime\_V2.safetensors 
 624: 
 625: ○ In this format, DESTINATION\_PATH must be the ful absolute path to the target 
 626: 
 627: directory, and FILENAME must be the exact desired filename including its extension. This format is typical y generated internal y based on UI widget selections. While an AI could construct this, it requires pre-calculation of absolute destination paths, making it less convenient than the custom format. 
 628: 
 629: 2. **Custom Download / Empowerment Mode Format \(Most flexible and recommended** **for AI agents\)**: 
 630: 
 631: ○ **Syntax**: prefix:URL \[filename.ext\] or prefix:URL.1 
 632: 
 633: ○ **Components**: 
 634: 
 635: ■ prefix:: One of the keys from the PREFIX\_MAP dictionary \(e.g., model:, vae:, lora:, extension:\), fol owed by a colon. This prefix informs the script about the type of asset and, implicitly, where to save it based on PREFIX\_MAP 
 636: 
 637: lookups. 
 638: 
 639: ■ URL: The actual download URL. This can be a direct link, a Civitai model page URL \(which wil be resolved by CivitaiAPI.py\), or a GitHub repository URL \(specifical y for the extension: prefix\). 
 640: 
 641: ■ \[filename.ext\] \(Optional, enclosed in square brackets \`\`\): This part explicitly specifies the desired filename \(including its extension\) for the downloaded asset. For extensions \(using extension: prefix\), this specifies the desired local folder name for the cloned repository. **It is highly recommended that** **AI agents always use this \[filename.ext\] tag** to ensure precise control over naming and to avoid ambiguity, especial y for assets where the URL 
 642: 
 643: does not clearly indicate the desired name or for extensions.1 
 644: 
 645: ○ **Examples for AI Agent Construction**: 
 646: 
 647: ■ Adding a new LoRA: 
 648: 
 649: lora:https://civitai.com/api/download/models/123456\[my\_new\_lora.safetenso rs\] 
 650: 
 651: ■ Adding a new WebUI Extension: 
 652: 
 653: extension:https://github.com/some-user/some-extension-repo 
 654: 
 655: ■ Adding a new Model using a Civitai Model Page URL: model:https://civitai.com/models/7890?modelVersionId=101112\[my\_awesom e\_model.safetensors\] \(The system wil resolve this to a direct download link\). 
 656: 
 657: ■ Adding a new VAE: 
 658: 
 659: vae:https://huggingface.co/username/repo/resolve/main/my\_vae.pt\[custom\_
 660: 
 661: vae\_name.pt\] 
 662: 
 663: ○ **Multiple Downloads**: Multiple download instructions can be combined in a single line string, separated by commas or spaces.1 Example: lora:URL1\[name1.safetensors\], model:URL2\[name2.ckpt\] 
 664: 
 665: extension:URL3\[ext\_folder\_name\] 
 666: 
 667: The fol owing table provides a clear specification for the AI agent on how to construct these download strings. 
 668: 
 669: **Table 3: download\(line\) Input Format Specification for AI Agents **
 670: 
 671: **Format Type **
 672: 
 673: **Syntax \(with **
 674: 
 675: **Example **
 676: 
 677: **Key Considerations **
 678: 
 679: **placeholders\) **
 680: 
 681: **Instantiation for AI **
 682: 
 683: **for AI Agent **
 684: 
 685: Custom/Empowerment prefix:URL\[filename.extlora:https://civitai.com/ Most flexible and \(Standard Asset\) 
 686: 
 687: \] 
 688: 
 689: api/download/models/Lrecommended. **Always **
 690: 
 691: ORA\_ID\[custom\_lora\_n **use \[filename.ext\] for **
 692: 
 693: ame.safetensors\] 
 694: 
 695: **precise naming **
 696: 
 697: **control. ** prefix must be 
 698: 
 699: a valid key from 
 700: 
 701: PREFIX\_MAP. URL can 
 702: 
 703: be a direct link or a 
 704: 
 705: Civitai model page 
 706: 
 707: URL. Ensure correct 
 708: 
 709: extension. 
 710: 
 711: Custom/Empowerment extension:GIT\_REPO\_U extension:https://githu Used for cloning Git \(WebUI Extension\) 
 712: 
 713: RL\[local\_folder\_name\] b.com/user/my-webui- repositories as extension\[MyLocalExte extensions. 
 714: 
 715: nsionFolderName\] 
 716: 
 717: \[local\_folder\_name\] 
 718: 
 719: specifies the directory 
 720: 
 721: name where the repo 
 722: 
 723: wil be cloned within 
 724: 
 725: the UI's extensions 
 726: 
 727: folder. 
 728: 
 729: Custom/Empowerment prefix1:URL1\[name1\], model:URL\_A\[model\_a. Al ows batching \(Multiple Assets\) 
 730: 
 731: prefix2:URL2\[name2\] safetensors\],vae:URL\_ multiple downloads in \(comma-separated\) 
 732: 
 733: B\[vae\_b.pt\] 
 734: 
 735: a single command 
 736: 
 737: string. Each instruction 
 738: 
 739: fol ows the individual 
 740: 
 741: format rules. 
 742: 
 743: **4.4.3. URL Canonicalization and Filename Extraction Logic** downloading-en.py \(and potential y Manager.py\) incorporates logic to process and clean URLs and to determine filenames: 
 744: 
 745: ● \_clean\_url\(url\): This internal function standardizes URLs. For example, it transforms Hugging Face /blob/ URLs into direct /resolve/ URLs and GitHub /blob/ URLs into /raw/ 
 746: 
 747: URLs. Crucial y, for Civitai URLs, it invokes CivitaiAPI.validate\_download\(url\) to obtain the actual direct download link and validated metadata \(like a suggested filename if not provided\).1 This al ows AI agents to confidently use Civitai model page URLs. 
 748: 
 749: ● \_extract\_filename\(url\): This function determines the filename for the download. Its logic prioritizes: 
 750: 
 751: 1. A filename explicitly provided within square brackets \`ìn the input URL string \(e.g., ...\[my\_file.safetensors\]\). This has the highest precedence and is the recommended method for AI agents to ensure specific naming.1 
 752: 
 753: 2. If nò\` tag is found, and the URL is a Civitai or Google Drive link, the function may return None, indicating that the filename wil be determined by the CivitaiAPI or the gdown tool, respectively.1 
 754: 
 755: 3. Otherwise, it typical y defaults to using the last segment of the URL's path as the filename \(e.g., Path\(urlparse\(url\).path\).name\).1 
 756: 
 757: This logic reinforces the best practice for AI agents to always provide an explicit \[filename.ext\] 
 758: 
 759: to control the naming of downloaded assets. 
 760: 
 761: **4.4.4. Protocol for Git Repository Cloning \(Extensions\)** When the extension: prefix is used in a download instruction, the provided Git repository URL 
 762: 
 763: and the optional local folder name \(from the \[local\_folder\_name\] tag\) are added to an internal list, typical y named extension\_repo.1 After al file-based downloads \(models, LoRAs, etc.\) are processed, downloading-en.py iterates through this extension\_repo list. For each entry, it executes a git clone --depth 1 --recursive <URL> <local\_folder\_name> command. The target directory for these clones is the extension\_dir specific to the active WebUI \(e.g., A1111/extensions\), as configured in settings.json by webui\_utils.py.1 This means the AI agent does not need to implement Git cloning logic itself; it only needs to provide the correctly formatted extension:URL\[name\] string. 
 764: 
 765: **4.5. Core Download and File Operations: modules/Manager.py** The modules/Manager.py script provides the low-level, backend functions for performing the actual file downloads from various sources and handling basic file operations.1 It abstracts the complexities of different download protocols and tools. downloading-en.py relies on functions within Manager.py \(e.g., manual\_download in downloading-en.py cal s download\_file\_platform\_aware, which likely utilizes or resides in Manager.py\) to execute the transfers.1 
 766: 
 767: Key functionalities of Manager.py include: 
 768: 
 769: ● Invoking command-line tools like aria2c \(for accelerated, multi-connection downloads\), gdown \(for Google Drive links\), curl \(for general URL fetching\), and git clone \(for repository cloning, specifical y for extensions\).1 
 770: 
 771: ● A significant post-download operation handled by Manager.py \(or cal ed by downloading-en.py after Manager.py's functions\) is \_unpack\_zips\(\). If any downloaded file is a .zip archive, this function wil automatical y extract its contents into the same directory and then delete the original .zip file.1 AI agents must be aware of this behavior when verifying downloads of zipped assets, as they should look for the extracted contents rather than the .zip file itself. 
 772: 
 773: This module's design al ows downloading-en.py \(and by extension, an AI agent interacting with it\) to focus on *what* assets to download and *where* they should conceptual y go \(via prefixes\), rather than the specific *how* of downloading from different types of URLs or handling archive extraction. 
 774: 
 775: **4.6. Civitai API Integration: modules/CivitaiAPI.py **
 776: 
 777: The modules/CivitaiAPI.py script is dedicated to enhancing interactions with the Civitai platform.1 Its primary functions are: 
 778: 
 779: ● **URL Resolution**: Resolving user-friendly Civitai model page URLs \(e.g., https://civitai.com/models/MODEL\_ID?modelVersionId=MODEL\_VERSION\_ID\) into direct, downloadable file links. This is typical y achieved through the validate\_download\(url\) function, which is cal ed by \_clean\_url in downloading-en.py when a Civitai URL is detected.1 
 780: 
 781: ● **Metadata Fetching**: Retrieving associated metadata for Civitai models, which can include information like preview image URLs and their suggested filenames. This metadata can be used to enhance the user experience or provide default naming if not specified by the user/agent.1 
 782: 
 783: This module significantly simplifies the task for AI agents \(and human users\) by al owing them to use the more common and easily discoverable Civitai model page URLs for downloads, abstracting away the need to manual y find direct API download endpoints. 
 784: 
 785: **4.7. Path and Configuration Management: modules/webui\_utils.py &** **settings.json **
 786: 
 787: The modules/webui\_utils.py script plays a crucial role in centralizing the definition and management of file system paths within the drfOrk/AnxietyLightning environment.1 Its output, often saved to a settings.json file, serves as a configuration source for other scripts. 
 788: 
 789: **4.7.1. Centralized Asset Storage: SHARED\_MODEL\_BASE **
 790: 
 791: A key concept managed by webui\_utils.py is SHARED\_MODEL\_BASE. This is defined as a platform-aware path \(e.g., HOME / 'sd\_models\_shared'\) that serves as the root directory for al shared, model-related assets like checkpoints, LoRAs, VAEs, embeddings, and ControlNet models.1 The use of a shared base path ensures that these assets are stored efficiently and can be consistently accessed by different Stable Diffusion WebUIs \(e.g., A1111, ComfyUI, Forge\) that might be launched by the system. 
 792: 
 793: The \_set\_webui\_paths\(ui\) function within webui\_utils.py is responsible for setting up the specific subdirectory structure under SHARED\_MODEL\_BASE \(e.g., creating sd\_models\_shared/Stable-diffusion, sd\_models\_shared/loras, sd\_models\_shared/vae\). It also determines and sets UI-specific paths, such as the extension\_dir \(where WebUI extensions are cloned\) and output\_dir \(for generated images\).1 
 794: 
 795: These resolved paths \(e.g., the absolute path to SHARED\_MODEL\_BASE/loras\) are then saved into the settings.json file.1 Subsequently, downloading-en.py reads settings.json to populate the directory path values in its PREFIX\_MAP, thereby ensuring that downloaded assets are directed to the correct, central y managed locations.1 
 796: 
 797: For an AI agent, SHARED\_MODEL\_BASE and its subdirectories represent the ground truth for where downloaded assets \(excluding extensions, which go to UI-specific paths\) wil ultimately reside. Verification of successful downloads must target these specific paths. For example, if an AI agent issues the command model:URL\[mymodel.safetensors\], it should expect mymodel.safetensors to be placed in the directory associated with the model\_dir entry in 
 798: 
 799: PREFIX\_MAP, which webui\_utils.py wil have configured to be something like SHARED\_MODEL\_BASE/Stable-diffusion. This predictability is fundamental for automation. 
 800: 
 801: **4.8. WebUI Launch Protocol: scripts/launch.py **
 802: 
 803: The scripts/launch.py script is responsible for the final stage of the workflow: configuring and launching the user-selected Stable Diffusion WebUI.1 It ensures that the chosen WebUI is started with the correct configurations, particularly pointing it to the appropriate model directories located within SHARED\_MODEL\_BASE.1 This script likely reads configuration details from files in the \_configs\_/ directory \(which contains UI-specific settings like config.json or ui-config.json\) and also from the global settings.json file \(for paths\). 
 804: 
 805: While an AI agent does not directly interact with launch.py for the purpose of downloading assets, the success of the agent's download operations is a prerequisite for launch.py to function correctly. If models or other essential assets are not downloaded to their expected locations or with the correct names, the WebUI launched by launch.py may fail to find them, leading to operational issues. Thus, the AI's adherence to the download protocols ensures that launch.py and the subsequently launched WebUI can operate as intended. 
 806: 
 807: **5. Operational Workflow for AI Agent Automation** **5.1. End-to-End Automation Sequence **
 808: 
 809: The automation of asset management by an AI agent within the drf0rk/AnxietyLightning system can fol ow an end-to-end sequence, adapted from the general workflow described in the project documentation 1, with a focus on AI-specific actions: 1. **\(Offline/Pre-Run\) Prepare Asset Definitions or Download Instructions**: 
 810: 
 811: ○ **Option A \(For Predefined Assets to appear in UI\)**: The AI agent reads the content of the relevant \_\*-data.py file \(e.g., \_models-data.py\) from its local copy of the drfOrk/sdAlgenLightning repository. It then programmatical y modifies this content by adding or updating asset definitions \(Python dictionaries\) according to the specified syntax. Crucial y, these modified \_\*-data.py files *must be committed* *and pushed to the GitHub fork* from which the scripts/setup.py script in the target runtime environment is configured to pul project files. 
 812: 
 813: ○ **Option B \(For Custom/Ad-Hoc Assets\)**: The AI agent prepares one or more formatted download strings, adhering to the prefix:URL\[filename.ext\] syntax, for direct input into scripts/en/downloading-en.py. This method is suitable for assets that do not need to be permanently listed in the UI widgets. 
 814: 
 815: 2. **\(Runtime\) Initiate Notebook Execution**: The AI agent triggers the execution of the main Jupyter notebook \(e.g., ANXETY\_sdAlgen\_EN.ipynb\). This typical y involves programmatical y sending commands to execute notebook cel s in sequence. 
 816: 
 817: 3. **Run scripts/setup.py**: The AI ensures that the notebook cel containing the command 
 818: 
 819: %run scripts/setup.py \(or its equivalent\) is executed. This step is vital as it deploys the project files \(potential y including the AI's modifications from Option A if pushed to the fork\) into the current runtime and initializes paths in settings.json. 
 820: 
 821: 4. **Configure widgets-en.py Parameters \(Optional, primarily if using Option A and** **needing UI reflection\)**: 
 822: 
 823: ○ If the AI has modified \_\*-data.py files \(Option A\) and wants these changes to be reflected in the standard download process triggered by widget values, it may need to programmatical y set Python variables in the notebook's global scope that correspond to UI widget selections \(e.g., model = 
 824: 
 825: 'NameOfNewlyAddedModel', XL\_models = True or False\). These variables would then be read by scripts/widgets-en.py and subsequently by scripts/en/downloading-en.py. 
 826: 
 827: 5. **Run scripts/widgets-en.py**: The AI ensures the cel running %run scripts/en/widgets-en.py \(or its language equivalent\) executes. This script loads data from \_\*-data.py files and initializes the UI elements. This step is less critical if the AI is exclusively using direct download strings \(Option B\) for downloading-en.py. 
 828: 
 829: 6. **Trigger Download via scripts/en/downloading-en.py**: 
 830: 
 831: ○ If using Option B \(direct download strings\): The AI agent programmatical y sets the value of a specific Python variable in the notebook's global scope \(e.g., empowerment\_output\_widget.value, or an equivalent variable that downloading-en.py is designed to read for custom input\) to its prepared download string\(s\). 
 832: 
 833: ○ The AI then ensures the notebook cel running %run scripts/en/downloading-en.py is executed. This script wil process either the widget-derived values \(potential y influenced by the AI in step 4\) or the direct empowerment string to initiate and manage the downloads. 
 834: 
 835: 7. **\(Optional but Recommended\) Verification**: After downloading-en.py has completed, the AI agent should perform verification checks. This involves confirming the existence of the downloaded files in their expected locations within SHARED\_MODEL\_BASE \(or UI-specific extension directories\) and checking for correct filenames. 
 836: 
 837: 8. **Launch WebUI via scripts/launch.py**: Final y, the AI ensures the cel running %run scripts/launch.py is executed. This wil start the Stable Diffusion WebUI, which should now have access to the newly downloaded assets. 
 838: 
 839: For AI automation, Option B \(providing direct download strings to downloading-en.py\) general y offers the most direct, flexible, and robust approach for ad-hoc or dynamic asset downloads. It bypasses the complexities of UI state management and the risks associated with programmatical y modifying and re-serializing Python code files \(\_\*-data.py\) for one-off downloads. Modifying \_\*-data.py files \(Option A\) is more appropriate when the goal is to persistently add new, selectable options to the Jupyter UI itself. 
 840: 
 841: **5.2. Programmatic Asset Download and Verification Workflow** **5.2.1. Constructing Download Instructions for downloading-en.py** To programmatical y download assets using the preferred direct input method for scripts/en/downloading-en.py, an AI agent should fol ow these steps: 1. **Identify Asset Type**: Determine the type of asset to be downloaded \(e.g., model, LoRA, 
 842: 
 843: VAE, extension\). 
 844: 
 845: 2. **Determine Prefix**: Consult the PREFIX\_MAP specification \(refer to Table 2 or the actual map in downloading-en.py\) to find the correct prefix: corresponding to the asset type. 
 846: 
 847: 3. **Obtain URL**: Secure the valid download URL for the asset. For Civitai assets, a model page URL is acceptable as CivitaiAPI.py wil resolve it. For extensions, this wil be the Git repository URL. 
 848: 
 849: 4. **Specify Filename/Folder Name**: Determine the desired local filename, including the correct extension \(e.g., \[my\_model.safetensors\]\). For extensions, this wil be the target local directory name for the cloned repository \(e.g., \[MyExtensionFolder\]\). This explicit naming is crucial for predictability and avoiding conflicts. 
 850: 
 851: 5. **Assemble Instruction String**: Construct the download instruction string in the format prefix:URL\[filename.ext\]. If multiple assets need to be downloaded, multiple such instructions can be concatenated, separated by commas. 
 852: 
 853: **5.2.2. Verifying Download Integrity and Final File Locations** After the downloading-en.py script has executed, robust AI automation requires verification of the download process: 
 854: 
 855: 1. **Determine Expected Path**: 
 856: 
 857: ○ Using the prefix from the download instruction, identify the corresponding directory variable \(e.g., lora\_dir for lora:\) from the PREFIX\_MAP. 
 858: 
 859: ○ Understand that this directory variable resolves to an absolute path, typical y SHARED\_MODEL\_BASE / subfolder\_name / \(e.g., sd\_models\_shared/loras/\). The actual absolute path for SHARED\_MODEL\_BASE and its subfolders is defined by webui\_utils.py and recorded in settings.json. 
 860: 
 861: ○ The final expected path for the downloaded file wil be SHARED\_MODEL\_BASE / 
 862: 
 863: subfolder\_name / filename.ext \(using the filename.ext specified in the 
 864: 
 865: \[filename.ext\] tag\). For extensions, it wil be UI\_SPECIFIC\_EXTENSION\_PATH / 
 866: 
 867: local\_folder\_name. 
 868: 
 869: 2. **Perform File Check**: The AI agent should perform a file existence check at this calculated absolute path. 
 870: 
 871: 3. **Handle Special Cases \(e.g., ZIP files\)**: Be aware that Manager.py includes functionality \(\_unpack\_zips\(\)\) to automatical y extract .zip archives upon download and then delete the archive itself.1 Therefore, if a .zip file was downloaded, the AI should verify the presence of the extracted contents \(e.g., a folder or files that were inside the zip\) and the absence of the .zip file. 
 872: 
 873: 4. **Utilize Verification Scripts \(If Available\)**: The project includes a scripts/download-result.py script, which is intended to display downloaded files.1 If the output of this script is machine-parsable, an AI agent could potential y execute it and parse its output as an additional verification step. 
 874: 
 875: Verification is a critical step to ensure that the download operation completed successful y and the asset is available in the expected location for subsequent use by the WebUI. The detail regarding automatic unzipping is particularly important, as a naive check for the .zip file itself would lead to an incorrect failure report if the file was successful y downloaded and 
 876: 
 877: extracted. 
 878: 
 879: **6. Jupyter Notebook Orchestration Layer **
 880: 
 881: **6.1. The Role of ANXETY\_sdAlgen\_EN.ipynb as the Primary** **Orchestrator **
 882: 
 883: The main Jupyter Notebook, typical y named ANXETY\_sdAlgen\_EN.ipynb \(or a language-specific variant like ANXETY\_sdAlgen\_RU.ipynb or the inferred sdAlgenLightning.ipynb\), serves as the top-level entry point and orchestrator for the entire drf0rk/AnxietyLightning system.1 It contains a sequence of cel s that, when executed in order, perform al necessary operations: setting up the environment, initializing UI elements, downloading assets, and final y launching the selected Stable Diffusion WebUI. 
 884: 
 885: For an AI agent, interaction with the system wil often involve programmatical y triggering the execution of these notebook cel s in their prescribed sequence. Alternatively, if operating at a lower level or integrating parts of the system into a different framework, the AI might need to replicate the orchestration logic embedded within this notebook. The notebook effectively acts as the "conductor" for the various scripts, ensuring they are run in the correct order and with the appropriate context. 
 886: 
 887: **6.2. Script Execution Sequence via %run Magic Command** The Jupyter notebook utilizes the %run magic command to execute the various Python scripts that constitute the system's workflow \(e.g., scripts/setup.py, scripts/en/widgets-en.py, scripts/en/downloading-en.py, scripts/launch.py\).1 The %run command executes the specified script within the context of the notebook's kernel. 
 888: 
 889: By default, %run executes the script in a new, empty namespace, but it can be configured to run in the notebook's interactive namespace, al owing scripts to access and potential y modify variables defined in the notebook's global scope. Scripts like setup.py are designed to have side effects, such as modifying sys.path or creating/updating the settings.json file, which then affect the execution environment for subsequent scripts. 
 890: 
 891: If an AI agent needs to pass data to a script being executed via %run \(for example, setting the empowerment\_output\_widget.value string in the notebook's scope before running downloading-en.py\), it must ensure that the variable is defined in a scope accessible to the script. The project documentation implies that downloading-en.py is capable of picking up such global y set values.1 A thorough understanding of %run's behavior, particularly regarding namespace interactions and variable scope, can be important for an AI agent needing to debug issues or implement fine-grained control over the execution environment. 
 892: 
 893: **7. Troubleshooting and Diagnostics for AI Agents** **7.1. Common Error Signatures and Programmatic Detection** AI agents interacting with the drf0rk/AnxietyLightning system should be equipped to detect, 
 894: 
 895: diagnose, and potential y remediate common errors by parsing logs and validating system states. Information on common issues can be found in project documentation and community discussions.1 
 896: 
 897: **Table 4: AI-Centric Troubleshooting Matrix **
 898: 
 899: ****
 900: 
 901: **Observable **
 902: 
 903: **Potential **
 904: 
 905: **Likely Root Cause **
 906: 
 907: **Recommended **
 908: 
 909: **Symptom/Error **
 910: 
 911: **Programmatic **
 912: 
 913: **\(referencing system AI-Driven **
 914: 
 915: **Pattern \(Log **
 916: 
 917: **Check/Validation by behavior\) **
 918: 
 919: **Action/Escalation **
 920: 
 921: **Snippet/Description\) AI **
 922: 
 923: ModuleNotFoundError: AI checks list of 
 924: 
 925: A required Python 
 926: 
 927: AI attempts to instal 
 928: 
 929: No module named 
 930: 
 931: instal ed Python 
 932: 
 933: package is missing 
 934: 
 935: the missing package 
 936: 
 937: 'some\_package' in 
 938: 
 939: packages against 
 940: 
 941: from the environment. \(e.g., via pip instal \). If Python logs during 
 942: 
 943: known dependencies. setup.py may have 
 944: 
 945: fails or lacks 
 946: 
 947: script execution. 1 
 948: 
 949: failed to instal al 
 950: 
 951: permissions, escalate 
 952: 
 953: dependencies, or the to human operator. 
 954: 
 955: base environment is 
 956: 
 957: incomplete. 
 958: 
 959: FileNotFoundError: 
 960: 
 961: AI verifies file 
 962: 
 963: Download failed 
 964: 
 965: AI re-triggers 
 966: 
 967: \[Errno 2\] No such file existence at the exact silently; AI used an download using the 
 968: 
 969: or directory: 
 970: 
 971: path 
 972: 
 973: incorrect filename in explicit 
 974: 
 975: '/path/to/some\_model.sSHARED\_MODEL\_BASEthe download prefix:URL\[filename.ext
 976: 
 977: afetensors' when 
 978: 
 979: /subfolder/filename.ext. command; file saved to \] format, ensuring WebUI tries to load a Checks if filename.ext an unexpected correct prefix and 
 980: 
 981: model. 1 
 982: 
 983: used in download 
 984: 
 985: location due to 
 986: 
 987: filename. Verifies path 
 988: 
 989: command matches 
 990: 
 991: incorrect prefix or path components from 
 992: 
 993: expected name. 
 994: 
 995: resolution. 
 996: 
 997: PREFIX\_MAP and 
 998: 
 999: settings.json. 
1000: 
1001: SyntaxError: invalid 
1002: 
1003: AI attempts to parse 
1004: 
1005: AI agent \(or other 
1006: 
1007: AI attempts to revert 
1008: 
1009: syntax \(or similar\) in 
1010: 
1011: the content of recently process\) has written the \_\*-data.py file to a logs when 
1012: 
1013: modified \_\*-data.py 
1014: 
1015: syntactical y incorrect last known good 
1016: 
1017: scripts/en/widgets-en. files \(e.g., using 
1018: 
1019: Python code to a 
1020: 
1021: version or to repair the 
1022: 
1023: py executes, 
1024: 
1025: ast.literal\_eval if 
1026: 
1027: \_\*-data.py file. 
1028: 
1029: syntax if the error is 
1030: 
1031: specifical y around the possible, or a simpler 
1032: 
1033: simple \(e.g., missing 
1034: 
1035: exec\(\) cal . 
1036: 
1037: regex for basic 
1038: 
1039: comma, quote\). If fix 
1040: 
1041: structure\). 
1042: 
1043: fails, escalate to 
1044: 
1045: human operator with 
1046: 
1047: file details. 
1048: 
1049: aria2c error codes 
1050: 
1051: AI parses logs for 
1052: 
1053: Invalid URL; network 
1054: 
1055: For 404, AI validates 
1056: 
1057: \(e.g., non-zero exit 
1058: 
1059: specific error 
1060: 
1061: connectivity issues; 
1062: 
1063: URL. For 
1064: 
1065: status\) or HTTP errors messages from 
1066: 
1067: permissions error on network/transient 
1068: 
1069: \(e.g., 404, 403, 413 1\) download tools. AI can download server; file errors, AI implements in logs from 
1070: 
1071: perform a network 
1072: 
1073: too large for 
1074: 
1075: retry logic with backoff. 
1076: 
1077: downloading-en.py or connectivity test from intermediate storage For persistent errors or Manager.py. 
1078: 
1079: the environment. 
1080: 
1081: or quota \(e.g., HTTP 
1082: 
1083: 403/413, AI escalates 
1084: 
1085: 413\); download 
1086: 
1087: to human with URL and 
1088: 
1089: interrupted. 
1090: 
1091: error details. 
1092: 
1093: FileNotFoundError for AI lists contents of 
1094: 
1095: Core project files are AI executes the special 
1096: 
1097: a core script \(e.g., 
1098: 
1099: scripts/ and modules/ missing or corrupted in protocol outlined in modules/Manager.py directories within the the source GitHub fork, Section 7.3: Prompt or 
1100: 
1101: cloned project. Checks or setup.py failed to 
1102: 
1103: human operator to 
1104: 
1105: scripts/downloading-e setup.py logs for git 
1106: 
1107: download/place them verify fork integrity and 
1108: 
1109: n.py\) when setup.py 
1110: 
1111: clone errors. 
1112: 
1113: correctly due to 
1114: 
1115: potential y restore files 
1116: 
1117: attempts to run it, or 
1118: 
1119: network or permission from 
1120: 
1121: when a notebook cel 
1122: 
1123: issues during its own anxety-solo/sdAIgen. 
1124: 
1125: tries to %run it. 
1126: 
1127: execution. 
1128: 
1129: NameError: name 
1130: 
1131: AI checks if al 
1132: 
1133: A required Python 
1134: 
1135: AI ensures notebook 
1136: 
1137: 'some\_variable' is not prerequisite notebook variable was not cel s are executed 
1138: 
1139: defined in logs when a cel s defining 
1140: 
1141: defined in the scope sequential y. If AI is 
1142: 
1143: script runs. 1 
1144: 
1145: necessary variables 
1146: 
1147: accessible to the 
1148: 
1149: setting variables 
1150: 
1151: were executed in the script, often due to 
1152: 
1153: programmatical y, it 
1154: 
1155: correct order. 
1156: 
1157: out-of-order cel 
1158: 
1159: verifies they are in the 
1160: 
1161: execution in the 
1162: 
1163: global notebook scope 
1164: 
1165: notebook. 
1166: 
1167: before the relevant 
1168: 
1169: %run command. 
1170: 
1171: **7.2. Diagnosing Failures in Downloads, Pathing, or Script Execution** Beyond specific error messages, AI agents can employ diagnostic strategies: 
1172: 
1173: ● **Download Failures**: 
1174: 
1175: ○ Thoroughly parse logs from downloading-en.py and Manager.py for any output from aria2c, curl, gdown, or git. 
1176: 
1177: ○ Attempt to validate URLs programmatical y before initiating downloads \(e.g., a simple HTTP HEAD request to check for existence and permissions, though this may not always be feasible or indicative for al URL types\). Rely on CivitaiAPI.py's validation for Civitai URLs. 
1178: 
1179: ○ Implement basic network connectivity checks from the runtime environment if widespread download issues occur. 
1180: 
1181: ● **Pathing Failures**: 
1182: 
1183: ○ Programmatical y resolve expected absolute paths for downloaded assets by combining SHARED\_MODEL\_BASE \(from settings.json\), the relevant subfolder indicated by the PREFIX\_MAP, and the specified filename. 
1184: 
1185: ○ Before attempting file operations \(like moving or checking existence\), verify that parent directories exist. 
1186: 
1187: ○ If paths seem incorrect, re-verify the PREFIX\_MAP logic and the contents of settings.json \(which webui\_utils.py should have populated correctly\). 
1188: 
1189: ● **Script Execution Failures**: 
1190: 
1191: ○ Parse Python tracebacks meticulously to identify the failing script, the exact line number, and the type of error \(e.g., SyntaxError, ImportError, AttributeError, KeyError\). 
1192: 
1193: ○ If exec\(\) in scripts/widgets-en.py is implicated, the primary suspect is a syntactical y incorrect or malformed \_\*-data.py file. The AI should flag the specific file path reported by read\_model\_data. 
1194: 
1195: ○ If scripts/setup.py itself fails early in its execution, this is a critical failure, as the entire environment setup \(including deployment of other scripts and path configurations\) may be incomplete. 
1196: 
1197: **7.3. Special Instruction for AI Agents: Handling Missing/Corrupted** **Core Files **
1198: 
1199: A critical scenario arises if the core files of the drf0rk/AnxietyLightning project itself are missing or corrupted. The scripts/setup.py script is designed to download these core project files \(other scripts in scripts/, modules in modules/, etc.\) from the designated drf0rk/AnxietyLightning GitHub fork.1 If these files are compromised *within the fork itself*, or if setup.py is unable to retrieve them due to persistent network issues or permissions problems related to the fork, the entire system may become non-functional. 
1200: 
1201: Detection by AI Agent: 
1202: 
1203: An AI agent can detect this critical failure state through several indicators: 
1204: 
1205: ● Execution logs from scripts/setup.py show errors related to git clone operations for the project repository or file copying/placement errors for essential scripts and modules. 
1206: 
1207: ● Subsequent attempts to %run other core scripts \(e.g., scripts/en/widgets-en.py, scripts/en/downloading-en.py\) fail with FileNotFoundError for the script file itself, indicating it was not deployed by setup.py. 
1208: 
1209: ● Python ImportError occurs when scripts try to import modules expected to be in the modules/ directory \(e.g., import Manager fails\). 
1210: 
1211: AI Action Protocol: 
1212: 
1213: Upon detecting such a condition, where critical project files appear to be missing from the runtime environment and scripts/setup.py is consistently failing to rectify this from the configured drf0rk/AnxietyLightning fork, the AI agent must be programmed to escalate the issue to a human operator. 
1214: 
1215: The prompt to the human operator should: 
1216: 
1217: 1. Clearly state the suspected missing or corrupted core project files \(e.g., listing specific paths like modules/Manager.py, scripts/downloading-en.py, or entire directories if indicated\). 
1218: 
1219: 2. Report the failure of scripts/setup.py to retrieve or deploy these files from the current drf0rk/AnxietyLightning GitHub fork. 
1220: 
1221: 3. Include the fol owing specific instruction for the human operator:"Please verify the integrity and presence of the affected files \(e.g., \[AI should list suspected missing/corrupted files/directories here, such as modules/Manager.py, 
1222: 
1223: scripts/downloading-en.py\]\) in the primary drf0rk/AnxietyLightning GitHub repository. If issues are identified in that fork, or if this problem persists despite the fork appearing correct, consider manual y providing or restoring these essential system files from the canonical original repository: https://github.com/anxety-solo/sdAIgen. This action may help resolve inconsistencies or missing components that are preventing the system from initializing correctly." 
1224: 
1225: This escalation protocol provides a crucial safety net. When the AI's primary source of truth for core system components \(the drf0rk/AnxietyLightning fork\) appears to be compromised or inaccessible, it leverages human intervention. Pointing the human operator to the ultimate origin repository \(anxety-solo/sdAIgen\) offers a potential source for obtaining stable, known-good versions of fundamental project files, which might be necessary if the fork has diverged negatively or suffered data loss for these critical components. 
1226: 
1227: **8. Conclusion: Key Imperatives for AI Agent **
1228: 
1229: **Integration **
1230: 
1231: Successful and robust integration of an AI agent with the drf0rk/AnxietyLightning system hinges on a precise understanding of its architecture, data formats, and operational sequences. Several key imperatives emerge from this technical analysis: 
1232: 
1233: ● **Dual Asset Addition Mechanisms**: The AI agent must differentiate between the two primary methods for adding assets: 
1234: 
1235: 1. Modifying \_\*-data.py files \(and ensuring these changes are pushed to the source GitHub fork before setup.py runs\) for adding persistent, predefined options to the UI widgets. This requires careful handling of Python syntax. 
1236: 
1237: 2. Generating direct command strings for scripts/en/downloading-en.py using the prefix:URL\[filename.ext\] format for flexible, ad-hoc, or dynamic downloads that do not require UI representation. This is general y the more robust and direct method for programmatic, one-time downloads. 
1238: 
1239: ● **Precision in Download Commands**: The paramount importance of correctly using the prefix:URL\[filename.ext\] format for programmatic downloads cannot be overstated. The AI agent should *always* specify the \[filename.ext\] component to ensure precise control over naming and to facilitate reliable verification. The prefix must be valid according to the PREFIX\_MAP. 
1240: 
1241: ● **Understanding Asset Destinations**: The role of modules/webui\_utils.py in defining SHARED\_MODEL\_BASE and other critical paths \(via settings.json\) is fundamental. The AI agent must use this information to determine the final locations of downloaded assets for verification purposes. Awareness of special handling, such as the auto-extraction of 
1242: 
1243: .zip files by Manager.py, is also necessary for correct verification. 
1244: 
1245: ● **Respect for Orchestration and Dependencies**: The AI agent must respect the execution sequence orchestrated by the main Jupyter notebook \(ANXETY\_sdAlgen\_EN.ipynb\), particularly the critical role of scripts/setup.py in deploying al project files from the designated GitHub fork. Any AI-driven changes to these files must be propagated to the fork to be effective. 
1246: 
1247: ● **Awareness of Executable Data Files**: The use of exec\(\) in scripts/widgets-en.py to process \_\*-data.py files means these files are effectively executable code. AI agents modifying them must ensure strict adherence to the Python dictionary syntax to prevent runtime errors or potential security vulnerabilities. 
1248: 
1249: Furthermore, the AI agent's design should incorporate robust error handling, comprehensive log parsing capabilities, and rigorous validation of al inputs it generates and outputs it receives. The ability to detect common error patterns and, where appropriate, attempt automated recovery or escalate to human operators \(as outlined in Section 7.3 for critical file issues\) wil be essential for reliable, autonomous operation within the drf0rk/AnxietyLightning ecosystem. Adherence to these principles wil enable the AI agent to effectively and safely leverage the powerful automation capabilities of this Stable Diffusion management system. 
1250: 
1251: **Works cited **
1252: 
1253: 1. sdAIgenLightning FileDocs.pdf 
1254: 
1255: 
1256: # Document Outline
1257: 
1258: + AnxietyLightning: A Technical Guide for AI Agent Integration   
1259: 	+ 1. Introduction   
1260: 		+ 1.1. Purpose of this Guide  
1261: 		+ 1.2. Project Overview: drf0rk/AnxietyLightning  
1262: 		+ 1.3. Core Capabilities for AI-Driven Automation  
1263: 		+ 1.4. Acknowledgment of Original Repository: https://github.com/anxety-solo/sdAIgen  
1264: 
1265: 	+ 2. System Architecture and Data Flow   
1266: 		+ 2.1. High-Level Architectural Blueprint  
1267: 		+ 2.2. Key Software Components and Their Interdependencies  
1268: 		+ 2.3. Data Flow for Asset Population and Management  
1269: 
1270: 	+ 3. File and Directory Structure for Programmatic Access   
1271: 		+ 3.1. Root Directory Organization  
1272: 		+ 3.2. Detailed Analysis of Critical Directories and Files  
1273: 
1274: 	+ 4. Core Scripts and Module Interactions: A Deep Dive   
1275: 		+ 4.1. Environment Initialization and Project Deployment: scripts/setup.py  
1276: 		+ 4.2. Asset Data Definition: scripts/\_\*-data.py Files   
1277: 			+ 4.2.1. Structure and Syntax  
1278: 			+ 4.2.2. Programmatic Modification Protocols for AI Agents  
1279: 
1280: 		+ 4.3. UI Widget Population Logic: scripts/widgets-en.py   
1281: 			+ 4.3.1. Data Ingestion from \_\*-data.py \(via read\_model\_data and exec\(\)\)  
1282: 
1283: 		+ 4.4. Download Orchestration Engine: scripts/en/downloading-en.py   
1284: 			+ 4.4.1. PREFIX\_MAP: Mapping Prefixes to Directories  
1285: 			+ 4.4.2. Input Formatting for download\(line\): Enabling Programmatic Downloads  
1286: 			+ 4.4.3. URL Canonicalization and Filename Extraction Logic  
1287: 			+ 4.4.4. Protocol for Git Repository Cloning \(Extensions\)  
1288: 
1289: 		+ 4.5. Core Download and File Operations: modules/Manager.py  
1290: 		+ 4.6. Civitai API Integration: modules/CivitaiAPI.py  
1291: 		+ 4.7. Path and Configuration Management: modules/webui\_utils.py & settings.json   
1292: 			+ 4.7.1. Centralized Asset Storage: SHARED\_MODEL\_BASE  
1293: 
1294: 		+ 4.8. WebUI Launch Protocol: scripts/launch.py  
1295: 
1296: 	+ 5. Operational Workflow for AI Agent Automation   
1297: 		+ 5.1. End-to-End Automation Sequence  
1298: 		+ 5.2. Programmatic Asset Download and Verification Workflow   
1299: 			+ 5.2.1. Constructing Download Instructions for downloading-en.py  
1300: 			+ 5.2.2. Verifying Download Integrity and Final File Locations  
1301: 
1302: 
1303: 	+ 6. Jupyter Notebook Orchestration Layer   
1304: 		+ 6.1. The Role of ANXETY\_sdAlgen\_EN.ipynb as the Primary Orchestrator  
1305: 		+ 6.2. Script Execution Sequence via %run Magic Command  
1306: 
1307: 	+ 7. Troubleshooting and Diagnostics for AI Agents   
1308: 		+ 7.1. Common Error Signatures and Programmatic Detection  
1309: 		+ 7.2. Diagnosing Failures in Downloads, Pathing, or Script Execution  
1310: 		+ 7.3. Special Instruction for AI Agents: Handling Missing/Corrupted Core Files  
1311: 
1312: 	+ 8. Conclusion: Key Imperatives for AI Agent Integration   
1313: 		+ Works cited
```

## File: Notebook/LightningAnxiety.ipynb
```
  1: {
  2:   "cells": [
  3:     {
  4:       "cell_type": "markdown",
  5:       "id": "4731600d-b776-48c4-88e0-8c20295abf71",
  6:       "metadata": {
  7:         "id": "4731600d-b776-48c4-88e0-8c20295abf71"
  8:       },
  9:       "source": [
 10:         "1. Setup Environment 🔽\n",
 11:         "\n",
 12:         "This cell downloads the initial setup.py script from your fork and then executes it, instructing the setup process to pull all subsequent project files from your repository."
 13:       ]
 14:     },
 15:     {
 16:       "cell_type": "code",
 17:       "execution_count": null,
 18:       "id": "fa348b8d-7e1e-48b4-b5d7-f1b336a708a9",
 19:       "metadata": {
 20:         "cellView": "form",
 21:         "id": "fa348b8d-7e1e-48b4-b5d7-f1b336a708a9"
 22:       },
 23:       "outputs": [],
 24:       "source": [
 25:         "# @title 1. Setup Environment (Final Path Correction)\n",
 26:         "import os\n",
 27:         "import sys\n",
 28:         "from pathlib import Path\n",
 29:         "\n",
 30:         "# --- DYNAMIC PLATFORM DETECTION & PATH SETUP ---\n",
 31:         "# This logic ensures the notebook and the scripts it runs agree on the correct home directory.\n",
 32:         "def get_platform_home():\n",
 33:         "    \"\"\"Determines the correct project HOME based on the runtime environment.\"\"\"\n",
 34:         "    if 'google.colab' in sys.modules:\n",
 35:         "        print(\"Platform: Google Colab\")\n",
 36:         "        return Path('/content')\n",
 37:         "    if os.path.exists('/kaggle'):\n",
 38:         "        print(\"Platform: Kaggle\")\n",
 39:         "        return Path('/kaggle/working')\n",
 40:         "    if os.environ.get('LIGHTNING_AI') or os.path.exists('/teamspace'):\n",
 41:         "        print(\"Platform: Lightning AI\")\n",
 42:         "        base_path = Path('/teamspace/studios/this_studio')\n",
 43:         "        if not base_path.exists():\n",
 44:         "            base_path = Path.home() / 'workspace'\n",
 45:         "        return base_path\n",
 46:         "    # Fallback for local or unrecognized environments\n",
 47:         "    print(\"Platform: Local / Unknown\")\n",
 48:         "    return Path.cwd()\n",
 49:         "\n",
 50:         "# Define the single source of truth for the project's home directory for this entire session\n",
 51:         "PROJECT_HOME = get_platform_home()\n",
 52:         "print(f\"✅ Project HOME directory set to: {PROJECT_HOME}\")\n",
 53:         "\n",
 54:         "# --- Configuration ---\n",
 55:         "lang = 'en'\n",
 56:         "branch = 'main'\n",
 57:         "fork_repo = 'drf0rk/AnxietyLightning'\n",
 58:         "\n",
 59:         "# --- Script Execution ---\n",
 60:         "anxety_path = PROJECT_HOME / 'ANXETY'\n",
 61:         "scripts_dir_temp = anxety_path / 'scripts'\n",
 62:         "setup_script_path = scripts_dir_temp / 'setup.py'\n",
 63:         "\n",
 64:         "os.makedirs(scripts_dir_temp, exist_ok=True)\n",
 65:         "\n",
 66:         "setup_url = f'https://raw.githubusercontent.com/{fork_repo}/{branch}/scripts/setup.py'\n",
 67:         "print(f\"🔄 Downloading setup script from {fork_repo}...\")\n",
 68:         "!curl -sLo {setup_script_path} {setup_url}\n",
 69:         "print(\"✅ Setup script downloaded.\")\n",
 70:         "\n",
 71:         "# Run the setup script to detect the platform and create settings.json\n",
 72:         "%run {setup_script_path} --lang={lang} --branch={branch} --fork={fork_repo}\n",
 73:         "\n",
 74:         "# --- Set Definitive Paths for Subsequent Cells ---\n",
 75:         "print(\"\\n✅ Setting up definitive paths for the notebook session...\")\n",
 76:         "modules_path = anxety_path / 'modules'\n",
 77:         "if str(modules_path) not in sys.path:\n",
 78:         "    sys.path.insert(0, str(modules_path))\n",
 79:         "\n",
 80:         "import json_utils as js\n",
 81:         "settings_path = anxety_path / 'settings.json'\n",
 82:         "\n",
 83:         "# --- THIS IS THE CORRECTED LOGIC ---\n",
 84:         "# Read the base 'scr_path' (e.g., /content/ANXETY) and then append '/scripts' to it.\n",
 85:         "base_scr_path = Path(js.read(settings_path, 'ENVIRONMENT.scr_path'))\n",
 86:         "scripts_dir = base_scr_path / 'scripts'\n",
 87:         "# --- END CORRECTION ---\n",
 88:         "\n",
 89:         "print(f\"✔️ Scripts directory for this session is set to: {scripts_dir}\")"
 90:       ]
 91:     },
 92:     {
 93:       "cell_type": "markdown",
 94:       "id": "6d2b405e-8fb7-497a-8f15-de2b6e5d91a9",
 95:       "metadata": {
 96:         "id": "6d2b405e-8fb7-497a-8f15-de2b6e5d91a9"
 97:       },
 98:       "source": [
 99:         "2. Widgets 🔽\n",
100:         "\n",
101:         "This cell will load the interactive widgets. Since setup.py (executed in the previous cell) has already downloaded the patched widgets-en.py (or widgets-ru.py) to scripts_dir, this command will now use your modified version with the LoRA dropdown."
102:       ]
103:     },
104:     {
105:       "cell_type": "code",
106:       "execution_count": null,
107:       "id": "3ffca5a8-6603-4463-b057-f3a6b41a9ae1",
108:       "metadata": {
109:         "cellView": "form",
110:         "id": "3ffca5a8-6603-4463-b057-f3a6b41a9ae1"
111:       },
112:       "outputs": [],
113:       "source": [
114:         "# @title 2. Widgets\n",
115:         "# This cell uses the 'scripts_dir' and 'lang' variables that were correctly defined in Cell 1.\n",
116:         "\n",
117:         "# The f-string constructs the full path to the script.\n",
118:         "# We print the path first for easy debugging to ensure it's correct.\n",
119:         "run_path = f\"{scripts_dir}/{lang}/widgets-{lang}.py\"\n",
120:         "\n",
121:         "print(f\"✅ Attempting to run script from: {run_path}\")\n",
122:         "%run {run_path}"
123:       ]
124:     },
125:     {
126:       "cell_type": "markdown",
127:       "id": "a538fedf-c7b8-478b-8cfd-3a68ee8bd743",
128:       "metadata": {
129:         "id": "a538fedf-c7b8-478b-8cfd-3a68ee8bd743"
130:       },
131:       "source": [
132:         "3. Downloading 🔽\n",
133:         "\n",
134:         "This cell initiates the downloading process for models, VAEs, extensions, and other necessary components. It will use the patched downloading-en.py (or downloading-ru.py) from your fork, ensuring downloads go to your centralized model storage location."
135:       ]
136:     },
137:     {
138:       "cell_type": "code",
139:       "execution_count": null,
140:       "id": "456ba90a-3a39-49d1-bd97-6ad4967ef838",
141:       "metadata": {
142:         "cellView": "form",
143:         "id": "456ba90a-3a39-49d1-bd97-6ad4967ef838"
144:       },
145:       "outputs": [],
146:       "source": [
147:         "# @title 3. Downloading\n",
148:         "# This cell uses the 'scripts_dir' and 'lang' variables defined in Cell 1.\n",
149:         "\n",
150:         "# The f-string constructs the full path to the script.\n",
151:         "# We print the path first for easy debugging.\n",
152:         "run_path = f\"{scripts_dir}/{lang}/downloading-{lang}.py\"\n",
153:         "\n",
154:         "print(f\"✅ Attempting to run script from: {run_path}\")\n",
155:         "%run {run_path}"
156:       ]
157:     },
158:     {
159:       "cell_type": "markdown",
160:       "id": "09187f0b-5108-4ec9-b251-d4bff537d110",
161:       "metadata": {
162:         "id": "09187f0b-5108-4ec9-b251-d4bff537d110"
163:       },
164:       "source": [
165:         "4. Start 🔽\n",
166:         "\n",
167:         "This cell launches the Stable Diffusion WebUI. It will execute the patched launch.py script from your fork, applying any platform-specific optimizations and arguments you've included."
168:       ]
169:     },
170:     {
171:       "cell_type": "code",
172:       "execution_count": null,
173:       "id": "35260036-3430-453d-8244-d81ccea04b32",
174:       "metadata": {
175:         "cellView": "form",
176:         "id": "35260036-3430-453d-8244-d81ccea04b32"
177:       },
178:       "outputs": [],
179:       "source": [
180:         "# @title 4. Start (Corrected Path Logic)\n",
181:         "from pathlib import Path\n",
182:         "import sys\n",
183:         "\n",
184:         "# Add the modules path to ensure json_utils can be imported\n",
185:         "anxety_path = Path.home() / 'ANXETY'\n",
186:         "modules_path = anxety_path / 'modules'\n",
187:         "if str(modules_path) not in sys.path:\n",
188:         "    sys.path.insert(0, str(modules_path))\n",
189:         "\n",
190:         "import json_utils as js\n",
191:         "\n",
192:         "# Read the correct scripts_dir path that was saved by setup.py\n",
193:         "settings_path = anxety_path / 'settings.json'\n",
194:         "scripts_dir = Path(js.read(settings_path, 'ENVIRONMENT.scr_path'))\n",
195:         "\n",
196:         "print(f\"✅ Running launch script from: {scripts_dir}\")\n",
197:         "# Launch the WebUI. The -l flag provides more detailed logging for tunnels.\n",
198:         "%run {scripts_dir}/launch.py -l"
199:       ]
200:     },
201:     {
202:       "cell_type": "markdown",
203:       "id": "b83974dc-0f5f-4a5b-8d52-3361c74a9458",
204:       "metadata": {
205:         "id": "b83974dc-0f5f-4a5b-8d52-3361c74a9458"
206:       },
207:       "source": [
208:         "Utilities\n",
209:         "5. Run Cleanup Utility 🔽\n",
210:         "\n",
211:         "This cell runs the new Cleanup Utility GUI script, allowing you to manage your environment. This script is downloaded from your fork via the initial setup."
212:       ]
213:     },
214:     {
215:       "cell_type": "code",
216:       "execution_count": null,
217:       "id": "5896fe1b-7db1-40a6-a0a5-1779a53248c4",
218:       "metadata": {
219:         "cellView": "form",
220:         "id": "5896fe1b-7db1-40a6-a0a5-1779a53248c4"
221:       },
222:       "outputs": [],
223:       "source": [
224:         "# @title 5. Run Cleanup Utility\n",
225:         "\n",
226:         "from pathlib import Path\n",
227:         "\n",
228:         "# This cell is now platform-agnostic.\n",
229:         "scripts_dir = Path.home() / 'ANXETY' / 'scripts'\n",
230:         "\n",
231:         "# Run the cleanup utility GUI\n",
232:         "%run {scripts_dir}/auto-cleaner.py"
233:       ]
234:     },
235:     {
236:       "cell_type": "code",
237:       "execution_count": null,
238:       "id": "f8a56c35-0d86-4826-a5c7-ba901a5708e9",
239:       "metadata": {
240:         "id": "f8a56c35-0d86-4826-a5c7-ba901a5708e9"
241:       },
242:       "outputs": [],
243:       "source": [
244:         "from pathlib import Path\n",
245:         "import shutil\n",
246:         "import os\n",
247:         "import sys\n",
248:         "\n",
249:         "# --- Start of Directory Management ---\n",
250:         "BASE_DIR = Path(\"/teamspace/studios/this_studio\")\n",
251:         "if os.getcwd() != str(BASE_DIR):\n",
252:         "    print(f\"🔄 Changing directory from {os.getcwd()} to {BASE_DIR}\")\n",
253:         "    os.chdir(BASE_DIR)\n",
254:         "# --- End of Directory Management ---\n",
255:         "\n",
256:         "# --- VERY IMPORTANT WARNING ---\n",
257:         "# This cell will DELETE almost everything in your Lightning AI instance.\n",
258:         "# It will only preserve this notebook file and 'main.py'.\n",
259:         "# Ensure you understand what is being deleted before running.\n",
260:         "# This operation is IRREVERSIBLE.\n",
261:         "\n",
262:         "print(\"!!! DANGER: YOU ARE ABOUT TO DELETE ALMOST ALL FILES !!!\")\n",
263:         "print(\"!!! PLEASE READ CAREFULLY BEFORE PROCEEDING !!!\")\n",
264:         "print(\"\\nThis cell will delete all folders and files in your current studio instance, EXCEPT:\")\n",
265:         "print(\" - This notebook file (e.g., 'LightningAnxiety (1) (1) (2).ipynb')\")\n",
266:         "print(\" - The 'main.py' file (if it exists in the root)\")\n",
267:         "print(\"\\nTHIS WILL REQUIRE YOU TO RERUN THE ENTIRE NOTEBOOK FROM THE FIRST CELL FOR A FRESH START.\")\n",
268:         "print(\"If you have any custom files you wish to keep, MOVE THEM OUTSIDE THIS STUDIO INSTANCE NOW.\")\n",
269:         "print(\"Proceed only if you want a completely blank studio environment.\")\n",
270:         "print(\"\\nType 'YES_DELETE_ALL' (case-sensitive) to confirm deletion and execute, then press Enter.\")\n",
271:         "print(\"Anything else will abort the operation.\")\n",
272:         "\n",
273:         "confirmation = input(\"Confirmation: \")\n",
274:         "\n",
275:         "if confirmation.strip() == \"YES_DELETE_ALL\": # Case-sensitive comparison\n",
276:         "    # Get the home/studio path\n",
277:         "    # On Lightning AI, this is typically /teamspace/studios/this_studio\n",
278:         "    HOME_PATH = Path.home()\n",
279:         "\n",
280:         "    # Get the current notebook's filename\n",
281:         "    # Use a more robust way to find the notebook file name, as __file__ is not always reliable in notebooks\n",
282:         "    notebook_filename = \"LightningAnxiety (1) (1) (2).ipynb\" # Explicitly set your notebook filename here for reliability\n",
283:         "    notebook_path = HOME_PATH / notebook_filename\n",
284:         "\n",
285:         "    main_py_path = HOME_PATH / \"main.py\"\n",
286:         "\n",
287:         "    # Define items to EXCLUDE from deletion\n",
288:         "    EXCLUDE_LIST = [\n",
289:         "        notebook_path,\n",
290:         "        main_py_path\n",
291:         "    ]\n",
292:         "\n",
293:         "    print(f\"\\n--- Starting Comprehensive Deletion in {HOME_PATH} ---\")\n",
294:         "    deleted_count = 0\n",
295:         "    skipped_count = 0\n",
296:         "\n",
297:         "    for item in HOME_PATH.iterdir():\n",
298:         "        # Convert item to absolute path for consistent comparison with EXCLUDE_LIST\n",
299:         "        abs_item = item.resolve()\n",
300:         "        if abs_item in EXCLUDE_LIST:\n",
301:         "            print(f\"ℹ️ Skipping protected item: {item.name}\")\n",
302:         "            skipped_count += 1\n",
303:         "            continue\n",
304:         "\n",
305:         "        print(f\"🗑️ Attempting to delete: {item.name} ({item})...\")\n",
306:         "        try:\n",
307:         "            if item.is_dir():\n",
308:         "                shutil.rmtree(item)\n",
309:         "            else:\n",
310:         "                item.unlink() # Delete file\n",
311:         "            print(f\"✅ Successfully deleted: {item.name}\")\n",
312:         "            deleted_count += 1\n",
313:         "        except Exception as e:\n",
314:         "            print(f\"❌ Error deleting {item.name} ({item}): {e}\")\n",
315:         "\n",
316:         "    print(\"\\n--- Comprehensive Cleanup Process Complete ---\")\n",
317:         "    print(f\"Summary: {deleted_count} items deleted, {skipped_count} items skipped (protected).\")\n",
318:         "    print(\"Please restart your runtime and run the notebook from the first cell for a fresh start.\")\n",
319:         "else:\n",
320:         "    print(\"\\nOperation aborted. No folders were deleted.\\n\")\n",
321:         "\n",
322:         "# --- Ensure we are back in BASE_DIR at the end of the cell ---\n",
323:         "if os.getcwd() != str(BASE_DIR):\n",
324:         "    os.chdir(BASE_DIR)\n",
325:         "# --- End of Directory Management ---\n"
326:       ]
327:     },
328:     {
329:       "cell_type": "code",
330:       "execution_count": null,
331:       "id": "60190e9e-4d90-47ff-804f-6efeb6c1ad6a",
332:       "metadata": {
333:         "id": "60190e9e-4d90-47ff-804f-6efeb6c1ad6a"
334:       },
335:       "outputs": [],
336:       "source": []
337:     }
338:   ],
339:   "metadata": {
340:     "kernelspec": {
341:       "display_name": "base",
342:       "language": "python",
343:       "name": "python3"
344:     },
345:     "language_info": {
346:       "codemirror_mode": {
347:         "name": "ipython",
348:         "version": 3
349:       },
350:       "file_extension": ".py",
351:       "mimetype": "text/x-python",
352:       "name": "python",
353:       "nbconvert_exporter": "python",
354:       "pygments_lexer": "ipython3",
355:       "version": "3.10.14"
356:     },
357:     "colab": {
358:       "provenance": []
359:     }
360:   },
361:   "nbformat": 4,
362:   "nbformat_minor": 5
363: }
```

## File: scripts/en/downloading-en.py
```python
  1: # ~ download.py | by ANXETY ~ (Final Self-Aware Path Correction)
  2: 
  3: import os
  4: import re
  5: import sys
  6: import json
  7: import time
  8: import shlex
  9: import shutil
 10: import subprocess
 11: from pathlib import Path
 12: from datetime import timedelta
 13: from urllib.parse import urlparse
 14: from IPython import get_ipython
 15: from IPython.display import clear_output
 16: from IPython.utils import capture
 17: 
 18: # --- Self-Aware Path Determination ---
 19: try:
 20:     SCRIPTS = Path(__file__).parent.parent
 21: except NameError:
 22:     SCRIPTS = Path.cwd() / 'ANXETY' / 'scripts'
 23: 
 24: modules_path = SCRIPTS.parent / 'modules'
 25: if str(modules_path) not in sys.path:
 26:     sys.path.insert(0, str(modules_path))
 27: 
 28: import json_utils as js
 29: from webui_utils import handle_setup_timer
 30: from CivitaiAPI import CivitAiAPI
 31: from Manager import m_download
 32: 
 33: # --- Load settings and paths from the single source of truth ---
 34: SETTINGS_PATH = SCRIPTS.parent / 'settings.json'
 35: settings = js.read(SETTINGS_PATH)
 36: env_settings = settings.get('ENVIRONMENT', {})
 37: widget_settings = settings.get('WIDGETS', {})
 38: webui_settings = settings.get('WEBUI', {})
 39: 
 40: # Define all necessary paths from the loaded settings
 41: UI = webui_settings.get('current')
 42: WEBUI_PATH = Path(webui_settings.get('webui_path'))
 43: extension_dir = Path(webui_settings.get('extension_dir'))
 44: model_dir = Path(webui_settings.get('model_dir'))
 45: vae_dir = Path(webui_settings.get('vae_dir'))
 46: lora_dir = Path(webui_settings.get('lora_dir'))
 47: control_dir = Path(webui_settings.get('control_dir'))
 48: 
 49: # Get widget values
 50: XL_models = widget_settings.get('XL_models', False)
 51: inpainting_model = widget_settings.get('inpainting_model', False)
 52: model_selections = widget_settings.get('model', ('none',))
 53: vae_selections = widget_settings.get('vae', ('none',))
 54: lora_selections = widget_settings.get('lora', ('none',))
 55: controlnet_selections = widget_settings.get('controlnet', ('none',))
 56: latest_webui = widget_settings.get('latest_webui', True)
 57: latest_extensions = widget_settings.get('latest_extensions', True)
 58: 
 59: # --- The rest of the script logic ---
 60: # (The remainder of this script is correct and does not need to be changed)
 61: 
 62: ipyRun = get_ipython().run_line_magic
 63: 
 64: if not WEBUI_PATH.exists():
 65:     print(f"⌚ Unpacking Stable Diffusion | WEBUI: {UI}...")
 66:     ipyRun('run', f'"{SCRIPTS / "UIs" / UI}.py"')
 67:     handle_setup_timer(str(WEBUI_PATH), env_settings.get('start_timer'))
 68:     print(f"🚀 Unpacking {UI} Complete!")
 69: else:
 70:     print(f"🔧 Current WebUI: {UI} | Already installed.")
 71: 
 72: if latest_webui or latest_extensions:
 73:     action = 'WebUI and Extensions' if latest_webui and latest_extensions else ('WebUI' if latest_webui else 'Extensions')
 74:     print(f"⌚️ Updating {action}...")
 75:     with capture.capture_output():
 76:         if latest_webui:
 77:             subprocess.run(['git', '-C', str(WEBUI_PATH), 'pull'])
 78:         if latest_extensions:
 79:             for entry in os.listdir(str(extension_dir)):
 80:                 dir_path = os.path.join(str(extension_dir), entry)
 81:                 if os.path.isdir(dir_path) and os.path.exists(os.path.join(dir_path, '.git')):
 82:                     subprocess.run(['git', '-C', dir_path, 'pull'])
 83:     print(f"✨ Update {action} Complete!")
 84: 
 85: model_files_path = SCRIPTS / ('_xl-models-data.py' if XL_models else '_models-data.py')
 86: loras_data_path = SCRIPTS / '_loras-data.py'
 87: with open(model_files_path, 'r', encoding='utf-8') as f: exec(f.read(), globals())
 88: with open(loras_data_path, 'r', encoding='utf-8') as f: exec(f.read(), globals())
 89: 
 90: model_list = globals().get('sdxl_models_data' if XL_models else 'sd15_model_data', {})
 91: vae_list = globals().get('sdxl_vae_data' if XL_models else 'sd15_vae_data', {})
 92: lora_list_to_use = globals().get('lora_data', {}).get('sdxl_loras' if XL_models else 'sd15_loras', {})
 93: controlnet_list_data = globals().get('controlnet_list', {})
 94: 
 95: def handle_submodels(selections, model_dict, dst_dir, inpainting=False):
 96:     download_list = []
 97:     if not isinstance(selections, (list, tuple)): return download_list
 98:     cleaned_selections = [re.sub(r'^\d+\.\s*', '', sel) for sel in selections]
 99:     for selection_name in cleaned_selections:
100:         if selection_name == 'none': continue
101:         if selection_name == 'ALL':
102:             for model_group_key in model_dict:
103:                 model_group_items = model_dict[model_group_key]
104:                 items_to_process = model_group_items if isinstance(model_group_items, list) else [model_group_items]
105:                 for item in items_to_process:
106:                     name = item.get('name') or os.path.basename(item['url'])
107:                     if not inpainting and "inpainting" in name.lower():
108:                         continue
109:                     download_list.append(f"\"{item['url']}\" \"{dst_dir}\" \"{name}\"")
110:             continue
111:         if selection_name in model_dict:
112:             model_group = model_dict[selection_name]
113:             items_to_process = model_group if isinstance(model_group, list) else [model_group]
114:             for model_info in items_to_process:
115:                 name = model_info.get('name') or os.path.basename(model_info['url'])
116:                 if not inpainting and "inpainting" in name.lower():
117:                     continue
118:                 download_list.append(f"\"{model_info['url']}\" \"{dst_dir}\" \"{name}\"")
119:     return download_list
120: 
121: print('📦 Processing asset download selections...')
122: line_entries = []
123: line_entries.extend(handle_submodels(model_selections, model_list, model_dir, inpainting_model))
124: line_entries.extend(handle_submodels(vae_selections, vae_list, vae_dir))
125: line_entries.extend(handle_submodels(lora_selections, lora_list_to_use, lora_dir))
126: line_entries.extend(handle_submodels(controlnet_selections, controlnet_list_data, control_dir))
127: 
128: download_line = ', '.join(filter(None, line_entries))
129: 
130: if download_line:
131:     print("Starting asset downloads...")
132:     m_download(download_line, log=True)
133: else:
134:     print("No additional assets selected for download.")
135: 
136: print('\r🏁 Download processing complete!')
137: ipyRun('run', f'"{SCRIPTS}/download-result.py"')
```

## File: scripts/en/widgets-en.py
```python
  1: # ~ widgets.py | by ANXETY ~ (Final Self-Aware Path Correction)
  2: 
  3: import ipywidgets as widgets
  4: from pathlib import Path
  5: import os
  6: import sys
  7: 
  8: # --- Self-Aware Path Determination ---
  9: # A script can always find its own location. This is the most reliable method.
 10: try:
 11:     # This works when the script is run directly and __file__ is defined.
 12:     # From .../scripts/en/widgets-en.py, going up two parents gets us to .../scripts/
 13:     SCRIPTS = Path(__file__).parent.parent
 14: except NameError:
 15:     # This is a fallback for environments where __file__ is not defined.
 16:     # It assumes the working directory is the PROJECT_HOME set by Cell 1's logic.
 17:     # This is less ideal but necessary for some notebook execution contexts.
 18:     SCRIPTS = Path.cwd() / 'ANXETY' / 'scripts'
 19: 
 20: # Add modules path to sys.path now that we have a reliable base
 21: modules_path = SCRIPTS.parent / 'modules'
 22: if str(modules_path) not in sys.path:
 23:     sys.path.insert(0, str(modules_path))
 24: 
 25: import json_utils as js
 26: from webui_utils import update_current_webui
 27: from widget_factory import WidgetFactory
 28: 
 29: # Define all other paths relative to the now-known SCRIPTS path
 30: SETTINGS_PATH = SCRIPTS.parent / 'settings.json'
 31: CSS = SCRIPTS.parent / 'CSS'
 32: JS = SCRIPTS.parent / 'JS'
 33: ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name', 'local')
 34: 
 35: # --- The rest of the script is now guaranteed to find its files ---
 36: # (The remainder of the file is the same as the correct version you already have)
 37: 
 38: factory = WidgetFactory()
 39: factory.load_css(CSS / 'main-widgets.css')
 40: factory.load_js(JS / 'main-widgets.js')
 41: HR = widgets.HTML('<hr>')
 42: 
 43: def read_model_data(file_path, data_key_in_file, prefixes=['none']):
 44:     """Reads data from a file, extracts a dictionary, and returns a numbered list of its keys."""
 45:     local_vars = {}
 46:     if not file_path.exists():
 47:         print(f"Warning: Data file not found at {file_path}. Skipping.")
 48:         return prefixes
 49:     with open(file_path, 'r', encoding='utf-8') as f:
 50:         try:
 51:             exec(f.read(), {}, local_vars)
 52:         except Exception as e:
 53:             print(f"Error executing data file {file_path}: {e}")
 54:             return prefixes
 55:     
 56:     data_dict = local_vars
 57:     for key_part in data_key_in_file.split('.'):
 58:         data_dict = data_dict.get(key_part, {})
 59:         if not isinstance(data_dict, dict):
 60:             return prefixes
 61:     
 62:     names = list(data_dict.keys())
 63:     numbered_names = [f"{i+1}. {name}" for i, name in enumerate(names)]
 64:     return prefixes + numbered_names
 65: 
 66: webui_selection = {
 67:     'A1111': "--xformers --no-half-vae", 'ComfyUI': "--use-sage-attention --dont-print-server",
 68:     'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory",
 69:     'Classic': "--persistent-patches --cuda-stream --pin-shared-memory",
 70:     'ReForge': "--xformers --cuda-stream --pin-shared-memory", 'SD-UX': "--xformers --no-half-vae"
 71: }
 72: 
 73: # Data file paths
 74: sd15_models_path = SCRIPTS / '_models-data.py'
 75: sdxl_models_path = SCRIPTS / '_xl-models-data.py'
 76: loras_data_path = SCRIPTS / '_loras-data.py'
 77: 
 78: model_header = factory.create_header('Model Selection (Ctrl+Click for multiple)')
 79: model_options = read_model_data(sd15_models_path, 'sd15_model_data')
 80: model_widget = factory.create_select_multiple(model_options, 'Models:', ('none',))
 81: inpainting_model_widget = factory.create_checkbox('Inpainting Models', False, ['inpaint'], layout={'width': 'auto'})
 82: XL_models_widget = factory.create_checkbox('SDXL', False, ['sdxl'], layout={'width': 'auto'})
 83: switch_model_widget = factory.create_hbox([inpainting_model_widget, XL_models_widget])
 84: 
 85: vae_header = factory.create_header('VAE Selection')
 86: vae_options = read_model_data(sd15_models_path, 'sd15_vae_data', ['none', 'ALL'])
 87: vae_widget = factory.create_select_multiple(vae_options, 'VAEs:', ('none',))
 88: 
 89: lora_header = factory.create_header('LoRA Selection')
 90: lora_options = read_model_data(loras_data_path, 'lora_data.sd15_loras', ['none', 'ALL'])
 91: lora_widget = factory.create_select_multiple(lora_options, 'LoRAs:', ('none',))
 92: 
 93: controlnet_header = factory.create_header('ControlNet Selection')
 94: controlnet_options = read_model_data(sd15_models_path, 'controlnet_list', ['none', 'ALL'])
 95: controlnet_widget = factory.create_select_multiple(controlnet_options, 'ControlNets:', ('none',))
 96: 
 97: additional_header = factory.create_header('Additional Settings')
 98: latest_webui_widget = factory.create_checkbox('Update WebUI', True)
 99: latest_extensions_widget = factory.create_checkbox('Update Extensions', True)
100: change_webui_widget = factory.create_dropdown(list(webui_selection.keys()), 'WebUI:', 'Forge', layout={'width': 'auto'})
101: commandline_arguments_widget = factory.create_text('Arguments:', webui_selection.get('Forge', ''))
102: 
103: save_button = factory.create_button('Save & Close', ['button', 'button_save'])
104: GDrive_button = factory.create_button('', layout={'width': '48px', 'height': '48px'}, class_names=['gdrive-btn'])
105: if ENV_NAME != 'Google Colab': GDrive_button.layout.display = 'none'
106: 
107: model_col = factory.create_vbox([model_header, model_widget, switch_model_widget])
108: vae_col = factory.create_vbox([vae_header, vae_widget])
109: lora_col = factory.create_vbox([lora_header, lora_widget])
110: cnet_col = factory.create_vbox([controlnet_header, controlnet_widget])
111: download_box = factory.create_vbox([model_col, vae_col, lora_col, cnet_col], class_names=['container'])
112: additional_box = factory.create_vbox([additional_header, factory.create_hbox([latest_webui_widget, latest_extensions_widget, change_webui_widget]), commandline_arguments_widget], class_names=['container'])
113: WIDGET_LIST = factory.create_vbox([factory.create_hbox([download_box, GDrive_button]), additional_box, save_button], class_names=['mainContainer'])
114: factory.display(WIDGET_LIST)
115: 
116: def on_xl_toggle(change):
117:     is_xl = change.new
118:     model_path = sdxl_models_path if is_xl else sd15_models_path
119:     model_key = 'sdxl_models_data' if is_xl else 'sd15_model_data'
120:     vae_key = 'sdxl_vae_data' if is_xl else 'sd15_vae_data'
121:     lora_key = 'lora_data.sdxl_loras' if is_xl else 'lora_data.sd15_loras'
122:     cnet_key = 'controlnet_list'
123:     model_widget.options = read_model_data(model_path, model_key)
124:     vae_widget.options = read_model_data(model_path, vae_key, ['none', 'ALL'])
125:     lora_widget.options = read_model_data(loras_data_path, lora_key, ['none', 'ALL'])
126:     controlnet_widget.options = read_model_data(model_path, cnet_key, ['none', 'ALL'])
127:     model_widget.value, vae_widget.value, lora_widget.value, controlnet_widget.value = ('none',), ('none',), ('none',), ('none',)
128: 
129: def on_webui_change(change):
130:     commandline_arguments_widget.value = webui_selection.get(change.new, '')
131: 
132: SETTINGS_KEYS = [
133:     'XL_models', 'model', 'inpainting_model', 'vae', 'lora', 'controlnet',
134:     'latest_webui', 'latest_extensions', 'change_webui', 'commandline_arguments'
135: ]
136: def save_settings():
137:     widget_values = {key: globals()[f"{key}_widget"].value for key in SETTINGS_KEYS}
138:     js.save(SETTINGS_PATH, 'WIDGETS', widget_values)
139:     if ENV_NAME == 'Google Colab':
140:         js.save(SETTINGS_PATH, 'mountGDrive', getattr(GDrive_button, 'toggle', False))
141:     update_current_webui(change_webui_widget.value)
142: 
143: def load_settings():
144:     if js.key_exists(SETTINGS_PATH, 'WIDGETS'):
145:         widget_data = js.read(SETTINGS_PATH, 'WIDGETS')
146:         for key in SETTINGS_KEYS:
147:             if key in widget_data and f"{key}_widget" in globals():
148:                 globals()[f"{key}_widget"].value = widget_data.get(key, ('none',))
149:     if ENV_NAME == 'Google Colab':
150:         GDrive_button.toggle = js.read(SETTINGS_PATH, 'mountGDrive', False)
151:         GDrive_button.add_class('active') if GDrive_button.toggle else GDrive_button.remove_class('active')
152: 
153: def on_save_click(b):
154:     save_settings()
155:     factory.close([WIDGET_LIST], ['hide'], delay=0.8)
156: 
157: XL_models_widget.observe(on_xl_toggle, 'value')
158: change_webui_widget.observe(on_webui_change, 'value')
159: save_button.on_click(on_save_click)
160: load_settings()
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
  1: # ~ ReForge.py | by ANXETY ~ (Corrected with Centralized Pathing)
  2: 
  3: import os
  4: import sys
  5: from pathlib import Path
  6: import asyncio
  7: import subprocess
  8: 
  9: # --- Add modules to path to import utils ---
 10: # This robustly finds the ANXETY folder regardless of the platform
 11: try:
 12:     # On Colab, home is /root, but the files are in /content.
 13:     project_home = Path('/content') if os.path.exists('/content') else Path.home()
 14:     anxety_path = project_home / 'ANXETY'
 15:     if not anxety_path.exists(): # Fallback for Lightning AI or other structures
 16:         anxety_path = Path.cwd() / 'ANXETY'
 17:     
 18:     modules_path = anxety_path / 'modules'
 19:     if str(modules_path) not in sys.path:
 20:         sys.path.insert(0, str(modules_path))
 21: 
 22:     import json_utils as js
 23:     from Manager import m_download
 24: except ImportError as e:
 25:     print(f"FATAL ERROR: Could not import core modules in ReForge.py. Pathing issue: {e}")
 26:     sys.exit(1)
 27: 
 28: 
 29: # --- Get All Paths from the Single Source of Truth: settings.json ---
 30: SETTINGS_PATH = anxety_path / 'settings.json'
 31: settings = js.read(SETTINGS_PATH)
 32: env_settings = settings.get('ENVIRONMENT', {})
 33: webui_settings = settings.get('WEBUI', {})
 34: 
 35: # Constants now defined from the central settings file
 36: UI = 'ReForge'
 37: HOME = Path(env_settings.get('home_path'))
 38: WEBUI = HOME / UI # Construct the correct path
 39: VENV = Path(env_settings.get('venv_path'))
 40: FORK_REPO = env_settings.get('fork')
 41: BRANCH = env_settings.get('branch')
 42: EXTS = Path(webui_settings.get('extension_dir'))
 43: 
 44: CD = os.chdir
 45: ipySys = get_ipython().system
 46: 
 47: # --- The rest of the script now uses the correct paths ---
 48: 
 49: async def _download_file(url, directory, filename):
 50:     """Downloads a single file."""
 51:     os.makedirs(directory, exist_ok=True)
 52:     file_path = os.path.join(directory, filename)
 53:     if os.path.exists(file_path): os.remove(file_path)
 54:     process = await asyncio.create_subprocess_shell(
 55:         f"curl -sLo \"{file_path}\" \"{url}\"",
 56:         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
 57:     )
 58:     await process.communicate()
 59: 
 60: async def download_files(file_list):
 61:     """Downloads multiple files asynchronously."""
 62:     tasks = []
 63:     for file_info in file_list:
 64:         parts = file_info.split(',')
 65:         url = parts[0].strip()
 66:         directory = parts[1].strip() if len(parts) > 1 else str(WEBUI)
 67:         filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
 68:         tasks.append(_download_file(url, directory, filename))
 69:     await asyncio.gather(*tasks)
 70: 
 71: async def download_configuration():
 72:     """Downloads configuration files and clones extensions."""
 73:     url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
 74:     # Corrected python version to be dynamic
 75:     py_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
 76:     configs = [
 77:         f"{url_cfg}/{UI}/config.json",
 78:         f"{url_cfg}/{UI}/ui-config.json",
 79:         f"{url_cfg}/styles.csv",
 80:         f"{url_cfg}/user.css",
 81:         f"{url_cfg}/card-no-preview.png,{str(WEBUI / 'html')}",
 82:         f"{url_cfg}/notification.mp3",
 83:         f"{url_cfg}/gradio-tunneling.py,{str(VENV / 'lib' / py_version / 'site-packages' / 'gradio_client')},tunnel.py"
 84:     ]
 85:     await download_files(configs)
 86:     
 87:     extensions_list = [
 88:         'https://github.com/anxety-solo/webui_timer timer',
 89:         'https://github.com/anxety-solo/anxety-theme',
 90:         'https://github.com/anxety-solo/sd-civitai-browser-plus Civitai-Browser-Plus',
 91:         'https://github.com/gutris1/sd-image-viewer Image-Viewer',
 92:         'https://github.com/gutris1/sd-image-info Image-Info',
 93:         'https://github.com/gutris1/sd-hub SD-Hub',
 94:         'https://github.com/Bing-su/adetailer',
 95:         'https://github.com/Haoming02/sd-webui-mosaic-outpaint',
 96:         'https://github.com/continue-revolution/sd-webui-segment-anything',
 97:         'https://github.com/kainatquaderee/sd-webui-reactor-Nsfw_freedom',
 98:         'https://github.com/a2569875/lora-prompt-tool',
 99:         'https://github.com/Uminosachi/sd-webui-inpaint-anything',
100:         'https://github.com/redmercy69/sd-webui-stripper',
101:         'https://github.com/diffus-me/sd-webui-facefusion',
102:         'https://github.com/glucauze/sd-webui-faceswaplab',
103:         'https://github.com/IntellectzProductions/sd-webui-faceswap',
104:         'https://github.com/yownas/sd-webui-faceswapper',
105:         'https://github.com/leeguandong/sd_webui_outpainting',
106:         'https://github.com/thoraxe69/sd-webui-roop',
107:     ]
108:     
109:     os.makedirs(EXTS, exist_ok=True)
110:     CD(EXTS)
111:     tasks = [asyncio.create_subprocess_shell(f"git clone --depth 1 {cmd}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) for cmd in extensions_list]
112:     await asyncio.gather(*tasks)
113: 
114: def unpack_webui():
115:     """Unpacks the WebUI zip file and cleans up model-related directories."""
116:     REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
117:     zip_path = f"{HOME}/{UI}.zip"
118:     m_download(f"\"{REPO_URL}\" \"{HOME}\" \"{UI}.zip\"")
119:     ipySys(f"unzip -q -o \"{zip_path}\" -d \"{WEBUI}\"")
120:     ipySys(f"rm -rf \"{zip_path}\"")
121:     
122:     model_dirs_to_clean = ['models', 'VAE', 'Lora', 'embeddings', 'ControlNet']
123:     for d_name in model_dirs_to_clean:
124:         d_path = WEBUI / d_name
125:         if d_path.exists() and d_path.is_dir():
126:             print(f"   Deleting stub directory: {d_path}")
127:             shutil.rmtree(d_path)
128: 
129: if __name__ == '__main__':
130:     from IPython.utils import capture
131:     with capture.capture_output():
132:         unpack_webui()
133:         asyncio.run(download_configuration())
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
  1: # ~ launch.py | by ANXETY ~ (Multi-Platform Restoration)
  2: 
  3: from TunnelHub import Tunnel
  4: import json_utils as js
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
 23: # ===================== DYNAMIC PLATFORM DETECTION & OPTIMIZATION =====================
 24: 
 25: def detect_and_optimize_platform():
 26:     """Detect platform and apply all necessary optimizations."""
 27:     platform = os.environ.get('DETECTED_PLATFORM')
 28:     if not platform:
 29:         try:
 30:             import google.colab
 31:             platform = 'colab'
 32:         except ImportError:
 33:             if os.path.exists('/kaggle'):
 34:                 platform = 'kaggle'
 35:             elif os.environ.get('LIGHTNING_AI'):
 36:                 platform = 'lightning'
 37:             else:
 38:                 platform = 'local'
 39:         os.environ['DETECTED_PLATFORM'] = platform
 40:     
 41:     print(f"✅ Launch script detected platform: {platform}")
 42: 
 43:     # Platform-specific optimizations and arguments
 44:     if platform == 'lightning':
 45:         print("⚡ Applying Lightning AI optimizations")
 46:         os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'
 47:         os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
 48:         
 49:         SHARED_MODEL_BASE = Path(js.read(SETTINGS_PATH, 'ENVIRONMENT.home_path')) / 'sd_models_shared'
 50:         
 51:         return [
 52:             '--xformers', '--no-half-vae', '--opt-split-attention', '--medvram',
 53:             '--disable-console-progressbars', '--api', "'--cors-allow-origins=*'",
 54:             '--listen', '--port=8080', '--share',
 55:             f'--ckpt-dir={SHARED_MODEL_BASE / "Stable-diffusion"}',
 56:             f'--embeddings-dir={SHARED_MODEL_BASE / "embeddings"}',
 57:             f'--lora-dir={SHARED_MODEL_BASE / "Lora"}',
 58:             f'--vae-dir={SHARED_MODEL_BASE / "vae"}',
 59:             f'--controlnet-dir={SHARED_MODEL_BASE / "ControlNet"}'
 60:         ]
 61:     elif platform == 'colab':
 62:         print(" APPLYING COLAB OPTIMIZATIONS...")
 63:         os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
 64:         return ['--share', '--xformers', '--enable-insecure-extension-access', '--opt-split-attention']
 65:     elif platform == 'kaggle':
 66:         print(" APPLYING KAGGLE OPTIMIZATIONS...")
 67:         os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
 68:         return ['--listen', '--port=8080', '--xformers', '--medvram', '--opt-split-attention']
 69:     else: # Local
 70:         return ['--xformers']
 71: 
 72: # ===================== SCRIPT SETUP =====================
 73: 
 74: CD = os.chdir
 75: ipySys = get_ipython().system
 76: 
 77: HOME = Path(js.read(os.path.join(Path.home(), 'ANXETY', 'settings.json'), 'ENVIRONMENT.home_path', str(Path.home())))
 78: SCR_PATH = HOME / 'ANXETY'
 79: SETTINGS_PATH = SCR_PATH / 'settings.json'
 80: 
 81: settings = js.read(SETTINGS_PATH)
 82: widget_settings = settings.get('WIDGETS', {})
 83: webui_settings = settings.get('WEBUI', {})
 84: env_settings = settings.get('ENVIRONMENT', {})
 85: 
 86: UI = webui_settings.get('current')
 87: WEBUI = Path(webui_settings.get('webui_path'))
 88: VENV = Path(env_settings.get('venv_path'))
 89: 
 90: # Apply optimizations and get launch arguments
 91: PLATFORM_ARGS = detect_and_optimize_platform()
 92: 
 93: # ===================== MAIN LAUNCH LOGIC =====================
 94: 
 95: # (The rest of the launch.py script remains largely the same as launch(2).py)
 96: # This includes the TunnelManager, helper functions, and the main execution block.
 97: # The key change is that PLATFORM_ARGS is now dynamically set.
 98: 
 99: def get_launch_command():
100:     """Construct launch command based on configuration."""
101:     base_args = widget_settings.get('commandline_arguments', '')
102:     password = 'ha4ez7147b5vdlu5u8f8flrllgn61kpbgbh6emil'
103:     
104:     common_args = ' --enable-insecure-extension-access --disable-console-progressbars --theme dark'
105:     if env_settings.get('env_name') == 'Kaggle':
106:         common_args += f" --encrypt-pass={password}"
107: 
108:     theme_accent_val = widget_settings.get('theme_accent', 'anxety')
109:     if theme_accent_val != 'anxety':
110:         common_args += f" --anxety {theme_accent_val}"
111: 
112:     final_args = " ".join(PLATFORM_ARGS)
113:     
114:     if UI == 'ComfyUI':
115:         return f"python3 main.py {base_args}"
116:     else: # A1111, Forge, ReForge, SD-UX, Classic
117:         # The base_args from the widget might duplicate things in PLATFORM_ARGS
118:         # A more robust solution would be to merge them, but for now we concatenate
119:         return f"python3 launch.py {final_args} {base_args} {common_args}"
120: 
121: 
122: # Main execution block from your reference file...
123: # This part is complex and should be copied over from your `launch(2).py` file.
124: # The `TunnelManager` class and the `if __name__ == '__main__':` block are essential.
125: # For brevity, I am not reproducing the entire TunnelManager class here, but you must ensure it is present.
126: 
127: if __name__ == '__main__':
128:     # The main execution flow from `launch(2).py` should be placed here.
129:     # It will now use the dynamically set `PLATFORM_ARGS` and the restored
130:     # dynamic `get_launch_command` function.
131:     print("Launch sequence initiated...")
132:     
133:     # Placeholder for the main execution logic from your `launch(2).py` file.
134:     # This includes parsing arguments, initializing TunnelManager, setting up tunnels,
135:     # and finally calling ipySys(LAUNCHER).
136:     
137:     # Example snippet of what should be here:
138:     args = argparse.ArgumentParser().parse_known_args()[0] # Simplified arg parsing
139:     
140:     print('Please Wait...\n')
141:     os.environ['PYTHONWARNINGS'] = 'ignore'
142: 
143:     # This will now use the dynamic LAUNCHER command
144:     LAUNCHER = get_launch_command()
145:     print(f"Executing launch command: {LAUNCHER}")
146:     
147:     # --- The rest of your tunneling and launch logic follows ---
148:     # ... (TunnelManager setup, `with tunnelingService:`, etc.) ...
149:     
150:     # A simplified version of the final call:
151:     try:
152:         CD(WEBUI)
153:         ipySys(LAUNCHER)
154:     except KeyboardInterrupt:
155:         pass
156:     except Exception as e:
157:         print(f"An error occurred during launch: {e}")
```

## File: scripts/setup.py
```python
  1: # ~ setup.py | by ANXETY ~ (Multi-Platform Restoration)
  2: 
  3: import sys
  4: from pathlib import Path
  5: import os
  6: 
  7: # VERY EARLY SYS.PATH MODIFICATION FOR CRITICAL IMPORTS
  8: _HOME_EARLY = Path.home()
  9: _ANXETY_PATH_EARLY = _HOME_EARLY / 'ANXETY'
 10: _MODULES_PATH_EARLY = _ANXETY_PATH_EARLY / 'modules'
 11: _SCRIPTS_PATH_EARLY = _ANXETY_PATH_EARLY / 'scripts'
 12: 
 13: _MODULES_PATH_EARLY.mkdir(parents=True, exist_ok=True)
 14: _SCRIPTS_PATH_EARLY.mkdir(parents=True, exist_ok=True)
 15: 
 16: if str(_MODULES_PATH_EARLY) not in sys.path:
 17:     sys.path.insert(0, str(_MODULES_PATH_EARLY))
 18: if str(_SCRIPTS_PATH_EARLY) not in sys.path:
 19:     sys.path.insert(0, str(_SCRIPTS_PATH_EARLY))
 20: # END VERY EARLY SYS.PATH MODIFICATION
 21: 
 22: from IPython.display import display, HTML, clear_output
 23: from urllib.parse import urljoin
 24: from tqdm import tqdm
 25: import nest_asyncio
 26: import importlib
 27: import argparse
 28: import asyncio
 29: import aiohttp
 30: import time
 31: import json
 32: 
 33: nest_asyncio.apply()
 34: 
 35: # ===================== DYNAMIC PLATFORM DETECTION =====================
 36: 
 37: def detect_platform():
 38:     """Detects the current runtime environment (Colab, Kaggle, Lightning, or Local)."""
 39:     try:
 40:         import google.colab
 41:         return 'colab'
 42:     except ImportError:
 43:         pass
 44: 
 45:     if os.path.exists('/kaggle'):
 46:         return 'kaggle'
 47: 
 48:     if (
 49:         os.environ.get('LIGHTNING_CLOUD_PROJECT_ID') or
 50:         os.environ.get('LIGHTNING_AI') or
 51:         os.path.exists('/teamspace')
 52:     ):
 53:         return 'lightning'
 54: 
 55:     return 'local'
 56: 
 57: CURRENT_PLATFORM = detect_platform()
 58: print(f"✅ Platform detected: {CURRENT_PLATFORM}")
 59: 
 60: # ===================== DYNAMIC PATH SETUP =====================
 61: 
 62: def get_home_path(platform):
 63:     """Returns the appropriate home directory based on the detected platform."""
 64:     if platform == 'lightning':
 65:         # Lightning AI uses a specific workspace directory
 66:         base_path = Path('/teamspace/studios/this_studio')
 67:         if not base_path.exists():
 68:             base_path = Path.home() / 'workspace'
 69:         base_path.mkdir(parents=True, exist_ok=True)
 70:         return base_path
 71:     elif platform == 'colab':
 72:         return Path('/content')
 73:     elif platform == 'kaggle':
 74:         return Path('/kaggle/working')
 75:     else: # local
 76:         return Path.cwd()
 77: 
 78: HOME = get_home_path(CURRENT_PLATFORM)
 79: SCR_PATH = HOME / 'ANXETY'
 80: SETTINGS_PATH = SCR_PATH / 'settings.json'
 81: 
 82: # ===================== UTILITIES =====================
 83: 
 84: def key_exists(filepath, key=None, value=None):
 85:     if not filepath.exists(): return False
 86:     try:
 87:         with open(filepath, 'r') as f: data = json.load(f)
 88:     except json.JSONDecodeError: return False
 89:     if key:
 90:         keys = key.split('.')
 91:         for k in keys:
 92:             if isinstance(data, dict) and k in data: data = data[k]
 93:             else: return False
 94:         return (data == value) if value is not None else True
 95:     return False
 96: 
 97: def save_environment_to_json(settings_path, data):
 98:     existing_data = {}
 99:     if settings_path.exists():
100:         try:
101:             with open(settings_path, 'r') as f: existing_data = json.load(f)
102:         except json.JSONDecodeError: existing_data = {}
103:     existing_data.update(data)
104:     with open(settings_path, 'w') as f: json.dump(existing_data, f, indent=4)
105: 
106: def get_start_timer():
107:     if SETTINGS_PATH.exists():
108:         try:
109:             with open(SETTINGS_PATH, 'r') as f:
110:                 settings = json.load(f)
111:                 return settings.get('ENVIRONMENT', {}).get('start_timer', int(time.time() - 5))
112:         except json.JSONDecodeError: return int(time.time() - 5)
113:     return int(time.time() - 5)
114: 
115: # ======================= MODULES =======================
116: 
117: def clear_module_cache(modules_folder):
118:     for module_name in list(sys.modules.keys()):
119:         module = sys.modules[module_name]
120:         if hasattr(module, '__file__') and module.__file__ and module.__file__.startswith(str(modules_folder)):
121:             del sys.modules[module_name]
122:     importlib.invalidate_caches()
123: 
124: def setup_module_folder(scr_folder):
125:     clear_module_cache(scr_folder)
126:     modules_folder = scr_folder / 'modules'
127:     modules_folder.mkdir(parents=True, exist_ok=True)
128:     if str(modules_folder) not in sys.path:
129:         sys.path.append(str(modules_folder))
130: 
131: # ===================== ENVIRONMENT SETUP =====================
132: 
133: def get_fork_info(fork_arg):
134:     if not fork_arg: return 'anxety-solo', 'sdAIgen'
135:     parts = fork_arg.split('/', 1)
136:     return parts[0], (parts[1] if len(parts) > 1 else 'sdAIgen')
137: 
138: def create_environment_data(platform, scr_folder, lang, fork_user, fork_repo, branch):
139:     platform_name_map = {
140:         'colab': 'Google Colab',
141:         'kaggle': 'Kaggle',
142:         'lightning': 'Lightning AI',
143:         'local': 'Local'
144:     }
145:     env_name = platform_name_map.get(platform, 'Unknown')
146:     
147:     return {
148:         'ENVIRONMENT': {
149:             'lang': lang,
150:             'fork': f"{fork_user}/{fork_repo}",
151:             'branch': branch,
152:             'env_name': env_name,
153:             'install_deps': key_exists(SETTINGS_PATH, 'ENVIRONMENT.install_deps', True),
154:             'home_path': str(HOME),
155:             'venv_path': str(HOME / 'venv'),
156:             'scr_path': str(scr_folder),
157:             'start_timer': get_start_timer(),
158:             'public_ip': ''
159:         }
160:     }
161: 
162: # ======================= DOWNLOAD LOGIC =====================
163: 
164: def generate_file_list(structure, base_url, base_path):
165:     def walk(struct, path_parts):
166:         items = []
167:         for key, value in struct.items():
168:             current_path = [*path_parts, key] if key else path_parts
169:             if isinstance(value, dict): items.extend(walk(value, current_path))
170:             else:
171:                 url_path = '/'.join(current_path)
172:                 for file in value:
173:                     url = f"{base_url}/{url_path}/{file}" if url_path else f"{base_url}/{file}"
174:                     file_path = base_path / '/'.join(current_path) / file
175:                     items.append((url, file_path))
176:         return items
177:     return walk(structure, [])
178: 
179: async def download_file(session, url, path):
180:     try:
181:         async with session.get(url) as resp:
182:             resp.raise_for_status()
183:             content = await resp.read()
184:             path.parent.mkdir(parents=True, exist_ok=True)
185:             path.write_bytes(content)
186:             return (True, url, path, None)
187:     except aiohttp.ClientResponseError as e:
188:         return (False, url, path, f"HTTP error {e.status}: {e.message}")
189:     except Exception as e:
190:         return (False, url, path, f"Error: {str(e)}")
191: 
192: async def download_files_async(scr_path, lang, fork_user, fork_repo, branch, log_errors):
193:     files_structure = {
194:         'CSS': ['main-widgets.css', 'download-result.css', 'auto-cleaner.css'],
195:         'JS': ['main-widgets.js'],
196:         'modules': ['json_utils.py', 'webui_utils.py', 'widget_factory.py',
197:                    'TunnelHub.py', 'CivitaiAPI.py', 'Manager.py', '__season.py'],
198:         'scripts': {
199:             'UIs': ['A1111.py', 'ComfyUI.py', 'Forge.py', 'Classic.py', 'ReForge.py', 'SD-UX.py'],
200:             lang: [f"widgets-{lang}.py", f"downloading-{lang}.py"],
201:             '': ['launch.py', 'auto-cleaner.py', 'download-result.py',
202:                  '_models-data.py', '_xl-models-data.py', '_loras-data.py']
203:         }
204:     }
205:     base_url = f"https://raw.githubusercontent.com/{fork_user}/{fork_repo}/{branch}"
206:     file_list = generate_file_list(files_structure, base_url, scr_path)
207:     async with aiohttp.ClientSession() as session:
208:         tasks = [download_file(session, url, path) for url, path in file_list]
209:         errors = []
210:         futures = asyncio.as_completed(tasks)
211:         for future in tqdm(futures, total=len(tasks), desc="Downloading files", unit="file"):
212:             result = await future
213:             if not result[0]: errors.append(result[1:])
214:         clear_output()
215:         if log_errors and errors:
216:             print("\nErrors occurred during download:")
217:             for url, path, error in errors: print(f"URL: {url}\nPath: {path}\nError: {error}\n")
218: 
219: # ===================== MAIN EXECUTION =====================
220: 
221: async def main_async(args=None):
222:     parser = argparse.ArgumentParser(description='ANXETY Download Manager')
223:     parser.add_argument('-l', '--lang', type=str, default='en', help='Language to be used')
224:     parser.add_argument('-b', '--branch', type=str, default='main', help='Branch to download from')
225:     parser.add_argument('-f', '--fork', type=str, default=None, help='Project fork (user/repo)')
226:     parser.add_argument('-s', '--skip-download', action='store_true', help='Skip downloading files')
227:     parser.add_argument('-L', '--log', action='store_true', help='Log download errors')
228:     args, _ = parser.parse_known_args(args)
229: 
230:     user, repo = get_fork_info(args.fork)
231: 
232:     if not args.skip_download:
233:         await download_files_async(SCR_PATH, args.lang, user, repo, args.branch, args.log)
234: 
235:     setup_module_folder(SCR_PATH)
236:     
237:     # This must come after setup_module_folder to ensure __season is importable
238:     from __season import display_info
239: 
240:     # Save environment data to settings.json
241:     env_data = create_environment_data(CURRENT_PLATFORM, SCR_PATH, args.lang, user, repo, args.branch)
242:     save_environment_to_json(SETTINGS_PATH, env_data)
243: 
244:     display_info(
245:         env=env_data['ENVIRONMENT']['env_name'],
246:         scr_folder=str(SCR_PATH),
247:         branch=args.branch,
248:         lang=args.lang,
249:         fork=args.fork
250:     )
251: 
252: if __name__ == '__main__':
253:     asyncio.run(main_async())
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
