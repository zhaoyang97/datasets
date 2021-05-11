# dataset settings

dataset_type = 'CocoDataset'
data_root = '../data/coco/'
annotations_root = '../data/coco/annotations/'
image_root = '../data/coco/'
# image_root = '/home/zhaoyang/container/data/TCTAnnotatedData/'

# img_scale = (1000, 600)
img_scale=(1333, 800)


img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=img_scale, keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=img_scale,
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=0,
    train=dict(
        type=dataset_type,
        ann_file=annotations_root + 'instances_train2017.json',
        img_prefix=image_root + 'train2017',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=annotations_root + 'instances_val2017.json',
        img_prefix=image_root + 'val2017',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        # ann_file=annotations_root + 'instances_val2017.json',
        # img_prefix=image_root + 'val2017',
        ann_file=data_root + 'annotations/image_info_test-dev2017.json',
        img_prefix=data_root + 'test2017/',
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='bbox')
