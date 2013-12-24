LongestCocoa
============

Programmers who write Objective-C must **REALLY** love its descriptive and verbose naming style. 

SoWhatIsTheLongestMethodOrConstantNamesInCocoaFramework? Here are some superb ones:

* outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange

Run `python longest.py` to discover the longest 10 names for each identifier type. Below is the output from `python longest.py iphoneos`.

Longest Names For iPhoneOS armv7
================

Longest Objective-C Interface Names
----------------
* [55] AVAssetResourceLoadingContentInformationRequestInternal
* [49] AVMutableVideoCompositionLayerInstructionInternal
* [47] AVAssetResourceLoadingContentInformationRequest
* [45] UICollectionViewFlowLayoutInvalidationContext
* [45] AVAsynchronousVideoCompositionRequestInternal
* [44] AVAssetWriterInputPixelBufferAdaptorInternal
* [44] AVMutableVideoCompositionInstructionInternal
* [43] AVVideoCompositionCoreAnimationToolInternal
* [43] AVAssetReaderVideoCompositionOutputInternal
* [43] AVMetadataMachineReadableCodeObjectInternal

Longest Objective-C Protocol Names
----------------
* [44] UIViewControllerTransitionCoordinatorContext
* [44] GKFriendRequestComposeViewControllerDelegate
* [44] AVCaptureAudioDataOutputSampleBufferDelegate
* [44] AVCaptureVideoDataOutputSampleBufferDelegate
* [43] GKTurnBasedMatchmakerViewControllerDelegate
* [42] ABPeoplePickerNavigationControllerDelegate
* [40] UIViewControllerInteractiveTransitioning
* [39] UIDocumentInteractionControllerDelegate
* [38] AVCaptureMetadataOutputObjectsDelegate
* [38] MFMessageComposeViewControllerDelegate

Longest Objective-C Property Names
----------------
* [56] automaticallyEnablesStillImageStabilizationWhenAvailable
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [49] outputObscuredDueToInsufficientExternalProtection
* [47] usesExternalPlaybackWhileExternalScreenIsActive
* [46] automaticallyEnablesLowLightBoostWhenAvailable
* [46] automaticallyConfiguresApplicationAudioSession
* [45] requiredPixelBufferAttributesForRenderContext
* [44] modalPresentationCapturesStatusBarAppearance
* [42] usesAirPlayVideoWhileAirPlayScreenIsActive
* [42] providesPresentationContextTransitionStyle

Longest Objective-C Method Names
----------------
* [128] initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:
* [120] drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:
* [115] layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:
* [113] decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:
* [112] drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:
* [111] getLineFragmentInsertionPointsForCharacterAtIndex:alternatePositions:inDisplayOrder:positions:characterIndexes:
* [108] migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:
* [104] videoComposition:shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:layerInstruction:asset:
* [101] animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:
* [98] strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:

Longest Objective-C Method Names (0/1 Parameter)
----------------
* [70] automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers
* [65] navigationControllerPreferredInterfaceOrientationForPresentation:
* [64] splitViewControllerPreferredInterfaceOrientationForPresentation:
* [63] pageViewControllerPreferredInterfaceOrientationForPresentation:
* [61] tabBarControllerPreferredInterfaceOrientationForPresentation:
* [60] backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:
* [60] setAutomaticallyEnablesStillImageStabilizationWhenAvailable:
* [59] generateIdentityVerificationSignatureWithCompletionHandler:
* [57] recommendedVideoSettingsForAssetWriterWithOutputFileType:
* [57] recommendedAudioSettingsForAssetWriterWithOutputFileType:

Longest C Function Names
----------------
* [63] CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback
* [62] CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType
* [62] CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers
* [62] MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics
* [61] CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes
* [58] CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes
* [58] CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS
* [57] ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering
* [57] vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12
* [57] vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGB8888

Longest Enum Names
----------------
* [41] NSPersistentStoreUbiquitousTransitionType
* [41] UIPageViewControllerNavigationOrientation
* [40] UIImagePickerControllerCameraCaptureMode
* [39] UIPageViewControllerNavigationDirection
* [38] UIImagePickerControllerCameraFlashMode
* [38] CBPeripheralManagerAuthorizationStatus
* [36] NSAttributedStringEnumerationOptions
* [36] NSURLSessionAuthChallengeDisposition
* [36] CBPeripheralManagerConnectionLatency
* [35] UIImagePickerControllerCameraDevice

Longest Enum Constant Names
----------------
* [64] kCFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod
* [63] NSPersistentStoreUbiquitousTransitionTypeInitialImportCompleted
* [63] NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication
* [61] kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualTo
* [61] NSAttributedStringEnumerationLongestEffectiveRangeNotRequired
* [58] kCMBufferQueueTrigger_WhenDurationBecomesLessThanOrEqualTo
* [58] kAudioSessionProperty_OverrideCategoryEnableBluetoothInput
* [57] kCMBufferQueueTrigger_WhenMaxPresentationTimeStampChanges
* [57] kAudioFileGlobalInfo_AvailableStreamDescriptionsForFormat
* [57] AVAudioSessionRouteChangeReasonNoSuitableRouteForCategory

Longest Variable Constant Names
----------------
* [96] kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange
* [81] kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection
* [74] MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification
* [71] kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection
* [66] kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight
* [64] kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS
* [64] kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged
* [64] AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly
* [64] kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS
* [62] NSPersistentStoreDidImportUbiquitousContentChangesNotification